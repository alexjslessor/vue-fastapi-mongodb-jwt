// import {
//     // AUTH_REFRESH,
//     AUTH_CLEAR,
//     AUTH_CHANGE_PASS
//   } from "../actions/auth";
//   import axios from "axios";
//   import router from "@/router/index";
import { SET_STATUS } from '../mutation-types'

  const state = {
    status: "",
    username: localStorage.getItem("username") || "",
    isAdmin: window.localStorage.getItem("isAdmin") || null,
    isFirstLogin: window.localStorage.getItem("isFirstLogin") || null,
    isActive: window.localStorage.getItem("isActive") || null,
    accessToken: window.localStorage.getItem("accessToken") || null,
//     status: "",
//     username: localStorage.getItem("username") || ""
  };
  
  const getters = {
//     isAuthenticated: state => !!state.username,
//     authStatus: state => state.status,
//     getUsername: state => state.username
  };


const actions = {

    async registerUser({ dispatch }, credentials) {
        await axios
        .post('/auth/register', { email: credentials.username, password: credentials.password })
        .then(resp => {
          console.log(resp)
  
          if (JSON.parse(resp.data.is_verified)) {
              dispatch('infoSnackBar', { color: 'yellow', statusText: `Welcome ${credentials.username}!!`, data: {info: ''}});
          } 
  
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
          console.log('register error.response: ', error.response)
          dispatch('infoSnackBar', { color: 'yellow', statusText: error.response.data.detail, data: {info: ''}});
        })
      },


    async authUser({ commit }, creds) {
        commit('AUTH_REQUEST');
  
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
  
            commit("setSnackBar", {cardColor: 'loginsuccess', btnColor: 'secondary', content: `Welcome ${resp.data.email}`}, { root: true });
            commit('AUTH_SUCCESS', resp);
  
            router.push("/dashboard");
          }).catch(err => {
            console.log('auth err-1: ', err);
  
            commit('AUTH_ERROR', err);
  
            let err_msg = '(Login): Please try again.' + err.response.statusText + ": " + err.response.data.detail
            commit("setSnackBar", {cardColor: 'error',  btnColor: 'white',  content: err_msg}, { root: true });
            commit('AUTH_CLEAR');
            commit('REMOVE_STORAGE');
            // router.push("/login");
          })
        }).catch(err => {
          console.log('auth err-2: ', err.response);
          commit("setSnackBar",  {cardColor: 'error', btnColor: 'white', content: `Username/Password Incorrect, Please try again.`},  { root: true });
          commit('AUTH_ERROR', err);
          commit('REMOVE_STORAGE')
        })
      },


      authChangePassword({ commit }, credentials) {
        commit('AUTH_REQUEST');
  
        const url = "/users/me";
        const password = credentials.password;
        const email = credentials.username;
        const isFirstLogin = false;
  
        axiosInstance.patch(url, { password: password, email: email, is_first_login: isFirstLogin })
        .then(resp => {
          console.log('change password resp: ', resp)
  
          localStorage.setItem("username", resp.data.email);
          commit('AUTH_SUCCESS', resp);
          router.push('/dashboard');
  
          const success_msg = 'Password Changed Successfully.'
          commit("setSnackBar", {cardColor: 'loginsuccess',  btnColor: 'secondary',  content: success_msg}, { root: false });
        })
        .catch(err => {
          console.log('change password error: ', err)
          const err_msg = 'Please try again.'
          commit("setSnackBar", {cardColor: 'error',  btnColor: 'white',  content: err_msg}, { root: true });
          
          if (router.path != '/reset') {
            router.push('/reset');
          }
          
        });
    },


    async refreshAuth({ commit }) {
        /* If cookie expired, clear store, redirect with axiosInstance.*/
        // commit('AUTH_REQUEST');
        const err_msg = 'Please Log In.'
        commit("setSnackBar", {cardColor: 'error',  btnColor: 'white',  content: err_msg}, { root: true });
        commit('AUTH_CLEAR');
        commit('REMOVE_STORAGE');
    },

    async logoutUser({ dispatch, commit }) {
        /* If user is has valid cookie, logout.*/
        try {
            commit('AUTH_REQUEST');
            commit('AUTH_CLEAR');
            commit('REMOVE_STORAGE');
            dispatch('infoSnackBar', { color: 'green', statusText: `Logged Out Successfully`, data: {info: ''}});
        } catch(err) {
            console.log('err - Logout: ', err)
            let err_msg = `(Logout Error): Please Login: ${err}`
            commit("setSnackBar", {cardColor: 'error',  btnColor: 'white',  content: err_msg}, { root: true });
            commit('AUTH_CLEAR');
            commit('REMOVE_STORAGE');
        } finally {
            router.push("/login");
        }
    
      },

}
//   const actions = {
//     [AUTH_REQUEST]: ({ commit }, credentials) => {
//       return new Promise((resolve, reject) => {
//         commit(AUTH_REQUEST);
//         const url = "/api/auth/login";
//         const formData = new FormData();
//         formData.set("username", credentials.username);
//         formData.set("password", credentials.password);
//         axios
//           .post(url, formData, { withCredentials: true })
//           .then(() => {
//             let url = "/api/users/me";
//             axios
//               .get(url, { withCredentials: true })
//               .then(resp => {
//                 localStorage.setItem("username", resp.data.email);
//                 axios.defaults.withCredentials = true;
//                 commit(AUTH_SUCCESS, resp);
//                 resolve(resp);
//               })
//               .catch(err => {
//                 commit(AUTH_ERROR, err);
//                 commit("snackbar/setErr", err, { root: true });
//                 localStorage.removeItem("username");
//                 reject(err);
//               });
//           })
//           .catch(err => {
//             commit(AUTH_ERROR, err);
//             commit("snackbar/setErr", err, { root: true });
//             localStorage.removeItem("username");
//             reject(err);
//           });
//       });
//     },
  
//     [AUTH_LOGOUT]: ({ commit }) => {
//       return new Promise(resolve => {
//         commit(AUTH_REQUEST);
//         const url = "/api/auth/logout";
//         axios
//           .post(url, {}, { withCredentials: true })
//           .then(resp => {
//             commit(AUTH_CLEAR, resp);
//             localStorage.removeItem("username");
//             router.push({ path: "/" });
//             resolve(resp);
//           })
//           .catch(err => {
//             commit("snackbar/setErr", err, { root: true });
//             commit(AUTH_CLEAR);
//           });
//       });
//     },
//     // [AUTH_REFRESH]: ({ commit }) => {
//     //   return new Promise((resolve) => {
//     //     commit(AUTH_REQUEST);
//     //     const url = "/api/auth/refresh";
//     //     axios
//     //       .post(url, {}, { xsrfCookieName: "csrf_refresh_token", xsrfHeaderName: "X-CSRF-TOKEN", withCredentials: true })
//     //       .then((resp) => {
//     //         resolve(resp);
//     //       })
//     //       .catch((error) => {
//     //         console.log(error);
//     //         commit(AUTH_CLEAR);
//     //       });
//     //   });
//     // },
//     [AUTH_CHANGE_PASS]: ({ commit }, credentials) => {
//       return new Promise((resolve, reject) => {
//         commit(AUTH_REQUEST);
//         const url = "/api/users/me";
//         let password = credentials.password;
//         let email = credentials.username;
//         console.log(email, password);
//         axios
//           .patch(url, {
//             password: password,
//             email: email
//           })
//           .then(resp => {
//             localStorage.setItem("username", resp.data.email);
//             commit(AUTH_SUCCESS, resp);
//             resolve(resp);
//           })
//           .finally(() => {
//             router.push({ path: `/user/info` });
//           })
//           .catch(err => {
//             commit("snackbar/setErr", err, { root: true });
//             reject(err);
//           });
//       });
//     }
//   };
  
//   const mutations = {
//     [AUTH_REQUEST]: state => {
//       state.status = "loading";
//     },
//     [AUTH_SUCCESS]: (state, resp) => {
//       state.status = "success";
//       state.username = resp.data.email;
//     },
//     [AUTH_ERROR]: state => {
//       state.status = "error";
//     },
//     [AUTH_CLEAR]: state => {
//       state.accessToken = "";
//       state.refreshToken = "";
//       state.username = "";
//     }
//   };
  
  export default {
    // namespaced: true,
    state,
    mutations,
    getters,
    actions
  };
  