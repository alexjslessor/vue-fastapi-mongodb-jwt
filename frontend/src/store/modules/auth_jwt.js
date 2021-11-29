import axios from "axios";
import router from "@/router/index";
import qs from 'qs'
import { SET_STATUS, SET_SNACKBAR, CLEAR_SNACKBAR, GET_USERNAME } from '../mutation-types'
import { LOGIN_ACTION, LOGOUT_ACTION } from '../action-types'
import axiosHeaders from '../../main'

  const state = {
    authDisabled: null,
    content: "",
    bottom: false,
    color: "",
    visible: false,
    btnColor: "",

    status: "",
    username: window.localStorage.getItem("username") || "",
    isAdmin: window.localStorage.getItem("isAdmin") || null,
    isFirstLogin: window.localStorage.getItem("isFirstLogin") || null,
    isActive: window.localStorage.getItem("isActive") || null,
    accessToken: window.localStorage.getItem("accessToken") || null,
  };
  
  const getters = {
    isAuthenticated: state => !!state.username,
    [GET_USERNAME]: state => state.username,
    getIsActive: state => JSON.parse(state.isActive),
    getUserType: state => JSON.parse(state.isAdmin),
    getIsFirstLogin: state => JSON.parse(state.isFirstLogin),
    // getLoadingStatus: state => state.status,
  };

  const mutations = {
    
    [SET_STATUS](state, status) { 
      state.status = status;
    },

    AUTH_CLEAR(state) {
      state.accessToken = "";
      state.refreshToken = "";
      state.username = "";
      state.status = "";
      state.isAdmin = null;
      state.isFirstLogin = null;
      state.isActive = null;
    },

    REMOVE_STORAGE(state) { 
      window.localStorage.removeItem("username");
      window.localStorage.removeItem("isAdmin");
      window.localStorage.removeItem("isFirstLogin");
      window.localStorage.removeItem("isActive");
      window.localStorage.removeItem("accessToken");
    },

    AUTH_SUCCESS(state, resp) {
      state.status = "success";
      
      state.username = resp.data.email;
      window.localStorage.setItem("username", resp.data.email);

      state.isActive = resp.data.is_active;
      window.localStorage.setItem("isActive", resp.data.is_active);

      state.isAdmin = resp.data.is_superuser;
      window.localStorage.setItem("isAdmin", resp.data.is_superuser);
      
      state.isFirstLogin = resp.data.is_first_login;
      window.localStorage.setItem("isFirstLogin", resp.data.is_first_login);
      
      state.accessToken = resp.data.access_token;
      window.localStorage.setItem("accessToken", resp.data.access_token);
    },
    SET_JWT(state, resp) {
      state.accessToken = resp.data.access_token;
      window.localStorage.setItem("accessToken", resp.data.access_token);
    },

    [SET_SNACKBAR](state, snackConfig) {
      state.content = snackConfig.content;
      state.bottom = true;
      state.color = snackConfig.cardColor;
      state.btnColor = snackConfig.btnColor;
      state.visible = true
    },

    [CLEAR_SNACKBAR](state) {
      state.content = "";
      (state.bottom = false), (state.btnColor = "");
      (state.color = ""), (state.visible = false);
    },
};

const actions = {

    snackBar({ commit }, info) {
      commit(SET_SNACKBAR, {cardColor: info.color, 
                            btnColor: info.btnColor, 
                            content: info.statusText + ": " + info.data.info}, 
                            { root: false });
    },

    async [LOGIN_ACTION]({ commit, dispatch }, creds) {
        // commit('AUTH_REQUEST');
        commit(SET_STATUS, 'loading');

        const formData = new FormData();
        formData.set('username', creds.username);
        formData.set('password', creds.password);
        await axios
        .post(`/auth/jwt/login`, formData, {headers: { 'Content-Type': 'multipart/form-data' }})
        .then(response => {

          console.log('login response: ', response)
          commit('SET_JWT', response)
  
          axios
          .get('/users/me', { headers: {'Authorization': `Bearer ${window.localStorage.getItem('accessToken')}` } })
          .then(resp => {
            console.log('users_me: ', resp);
  
            dispatch("snackBar", { color: 'green', btnColor: 'white', statusText: `Welcome ${resp.data.email}`, data: {info: ''}});
            commit('AUTH_SUCCESS', resp);

            router.push("/dashboard");

          }).catch(err => {
            console.log('auth err-1: ', err);
  
            // commit('AUTH_ERROR', err);
            commit(SET_STATUS, 'error');

            let err_msg = '(Login): Please try again.' + err.response.statusText + ": " + err.response.data.detail
            // dispatch("snackBar", {cardColor: 'error',  btnColor: 'white',  content: err_msg} );
            dispatch("snackBar", { color: 'red', btnColor: 'white', statusText: `Welcome ${resp.data.email}`, data: {info: ''}});

            commit('AUTH_CLEAR');
            commit('REMOVE_STORAGE');
            // router.push("/login");
          })
        }).catch(err => {
          console.log('auth err-2: ', err.response);
          dispatch("snackBar", { color: 'red', btnColor: 'white', statusText: `Username/Password Incorrect, Please try again.`, data: {info: ''}});

          // commit('AUTH_ERROR', err);
          commit(SET_STATUS, 'error')
          commit('REMOVE_STORAGE')
        })
      },


    async refreshAuth({ dispatch, commit }) {
        /* If cookie expired, clear store, redirect with axiosHeaders.*/
        // commit('AUTH_REQUEST');
        const err_msg = 'Please Log In.'
        dispatch("snackBar", { color: 'Error', btnColor: 'white', statusText: err_msg, data: {info: ''}});

        commit('AUTH_CLEAR');
        commit('REMOVE_STORAGE');
    },


    async [LOGOUT_ACTION]({ dispatch, commit }) {
        /* If user is has valid cookie, logout.*/
        try {
            commit(SET_STATUS, 'loading');
            // commit('AUTH_REQUEST');
            commit('AUTH_CLEAR');
            commit('REMOVE_STORAGE');
            dispatch("snackBar", { color: 'green', btnColor: 'white', statusText: `Logged Out Successfully`, data: {info: ''}});
        } catch(err) {

          commit('AUTH_CLEAR');
          commit('REMOVE_STORAGE');

          console.log('err - Logout: ', err)

          let err_msg = `(Logout Error): Please Login: ${err}`
          dispatch("auth/snackBar", {color: 'error',  btnColor: 'white',  statusText: err_msg, data: {info: ''}});
            
        } finally {
            router.push("/login");
        }
    
      },


      async registerUser({ dispatch }, credentials) {
        await axios
        .post('/auth/register', { email: credentials.username, password: credentials.password })
        .then(resp => {
          console.log(resp)

          if ( resp.status == 201 ) {
              dispatch('snackBar', 
              { color: 'green', btnColor: 'white', statusText: `Welcome ${credentials.username}!!`, 
              data: {info: ''}});
          } else if(resp.status == 400 ) {
            dispatch('snackBar', 
              { color: 'red', btnColor: 'white', statusText: `Signup Error, please try again`, 
              data: {info: ''}});
          }

          // if (JSON.parse(resp.data.is_verified)) {
              // dispatch('snackBar', { color: 'green', statusText: `Welcome ${credentials.username}!!`, data: {info: ''}});
          // } 
  
          // else {
          //   axios
          //   .post('/auth/request-verify-token', { email: resp.data.email } )
          //   .then(resp => {
          //     console.log('resp: ', resp);
          //   })
          //   .catch(error => {
          //     console.log('error verify-token: ', error.response)
          //   })
          // }
  
        })
        .catch(error => {
          console.log('register error response: ', error.response)
          dispatch('snackBar', { color: 'yellow', statusText: error.response.data.detail, data: {info: ''}});
        })
      },




      changePassword({ commit, dispatch }, credentials) {
        commit(SET_STATUS, 'loading');
        const url = "/users/me";
        const password = credentials.password;
        const email = credentials.username;
        const isFirstLogin = false;
  
        // axios.patch(url, { password: password, email: email })
        axiosHeaders.patch(url, { email: email, password: password, is_first_login: isFirstLogin })
        .then(resp => {
          console.log('resp: ', resp)
  
          if( resp.status == 200 ) {
            dispatch('snackBar', {cardColor: 'green', statusText: `Sucess`, data: {info: `${resp.data.message}` }});
          } else if( resp.status == 400 ) {
            dispatch('snackBar', {cardColor: 'red', statusText: `Error`, data: {info: `${resp.data.message}` }});
          }
          // window.localStorage.setItem("username", resp.data.email);
          // commit('AUTH_SUCCESS', resp);
          // router.push('/dashboard');
  
          // const success_msg = 'Password Changed Successfully.'
          // dispatch("snackBar", { color: 'green', btnColor: 'white', statusText: success_msg, data: {info: ''}});

        })
        .catch(err => {
          console.log('error: ', err)
        })
    },

    //   changePassword({ commit, dispatch }, credentials) {

    //     commit(SET_STATUS, 'loading');

    //     const url = "/users/me";
    //     const password = credentials.password;
    //     const email = credentials.username;
    //     const isFirstLogin = false;
  
    //     axiosHeaders.patch(url, { password: password, email: email, is_first_login: isFirstLogin })
    //     .then(resp => {
    //       console.log('change password resp: ', resp)
  
    //       window.localStorage.setItem("username", resp.data.email);
    //       commit('AUTH_SUCCESS', resp);
    //       router.push('/dashboard');
  
    //       const success_msg = 'Password Changed Successfully.'
    //       dispatch("snackBar", { color: 'green', btnColor: 'white', statusText: success_msg, data: {info: ''}});

    //     })
    //     .catch(err => {
    //       console.log('change password error: ', err)
    //       const err_msg = 'Please try again.'
    //       // dispatch("snackBar", {cardColor: 'error',  btnColor: 'white',  content: err_msg } );
    //       dispatch("snackBar", { color: 'error', btnColor: 'white', statusText: `Error Changing Password`, data: {info: ''}});
    //       if (router.path != '/reset') {
    //         router.push('/reset');
    //       }
    //     });
    // },

    async forgotPassword({ }, credentials) {
      const url = '/auth/forgot-password'
      await axiosHeaders.post(url, { email: credentials.email })
      .then(resp => {
        console.log(resp)

      })
    },

    finalizeForgotPassword({ }, hash) {
      console.log('finalize login hash: --', hash)
      const q = qs.parse(hash.replace('?', ''));
      return q.toString()
      // console.log('finalize login q: --', q);
      // const query = new URLSearchParams();

      // query.append("code", q.code);
      // query.append("state", q.state);
      // query.append('realmId', q.realmId)
      // const url = "/oauth/callback?" + query.toString();

      // axios
      // .get(`/get_auth_token/${q.code}/${q.realmId}/${q.state}`)
      // .then(resp => {
      //   console.log('tokens: --', resp)
      //   commit('SET_OAUTH_TOKENS', resp)
      // });
    },

    async resetPassword({ dispatch }, credentials) {
      console.log('resetPassword Token: ', credentials.token);
      
      const url = '/auth/reset-password'
      await axios.post(url, { token: credentials.token, 
                              password: credentials.password 
                            })
      .then(resp => {
        console.log(resp)

        if( resp.status == 200 ) {
          const success_msg = 'Password Changed Successfully!'
          dispatch("snackBar", { color: 'green', btnColor: 'white', statusText: success_msg, data: {info: ''}});
        }

      })
    },


}

  export default {
    namespaced: true,
    state,
    mutations,
    getters,
    actions
  };
  