import axios from "axios";
import fleek from '@fleekhq/fleek-storage-js';   
// import axiosHeaders from '../../main'

const state = {
    img: null,
    imgList: [],
    imgPreviewList: [],
  };
  // get data from the state
  // are computed properties and syncronous
  const getters = {
    getImgStr: state => state.img,
    getImgList: state => state.imgList,
    getImgPreviewList: state => state.imgPreviewList,
  };
  //mutations update the state
  //convention to use uppercase letters for mutations
  const mutations = {
    CLEAR_IMAGE_STATE(state) {
      state.img = null;
      state.imgList = [];
      state.imgPreviewList = [];
    },
    DELETE_IMAGE_FROM_STATE(state, data) {
      state.imgList.splice(data, 1)
      state.imgPreviewList.splice(data, 1)
    },

    MULTI_FILE_TO_ARR(state, data) {
      // console.log('MULTI_FILE_TO_ARR: ', data)
      state.imgList.push(data)
    },

    MULTI_PREVIEW_TO_ARR(state, data) {
      // console.log('MULTI_PREVIEW_TO_ARR: ', data)
      state.imgPreviewList.push(data)
    },


    // uploadImg(state, data) {
    //   console.log('uploadImg: ', data)
    //   state.img = data;
    // },
    
    // UPDATE_IMG_LIST(state, data) {
    //   // let img = state.imgList.find(i => {
    //   //    if(i.name != item.name) return item;
    //   // });
    // },

  };
  const actions = {

    async multiFileAction( { state, commit }, event ) {
      Array.from(event).map(image => {
        commit('MULTI_FILE_TO_ARR', image)

        let url = URL.createObjectURL(image)
        commit('MULTI_PREVIEW_TO_ARR', url)
        // console.log('multi url: ', url)
      });
  },


    async singleFileAction( { commit }, event ) {
        // console.log('imageUpload: ', event)
        commit('uploadImg', event)
    },

    async fleekUploadMulti( { state, dispatch }, event) {
      console.log('fleekUpload: ', event)
      console.log('multiState: ', state.imgList)

      let urlArr = []
      for (let i = 0; i < state.imgList.length; i++) {
          console.log(i, state.imgList[i]);

          const input = {
            apiKey: 'RmOhy96hLwmuDBsOueAq5g==',
            apiSecret: 'ryBoPW0b7RYn4qasQYtlCwMBgb0kSD7AU4ZSTj5Br7s=',
            key: `productImg/${ state.imgList[i].name }`,
            data: state.imgList[i] 
          };
          const res = await fleek.upload(input);

          urlArr.push( res.publicUrl );
          // urlArr.push( state.imgList[i].name );
          // const res = {publicUrl: 'http://www.asdasd.com'}
          // const serv = await axios.post(`/ecom/update_db/${event.product_id}`, { image: res.publicUrl } );
          // console.log('serv complete: ', serv)
      }

      console.log('urlArr: ', urlArr)
      const postArr = await axios.post(`/ecom/update_db/${event.product_id}`, { images: urlArr } );
      console.log('post urlArr: ', postArr)

      // await dispatch('stripe/query_products', 
                    // {query: 'all_products', filter: 'all'},
                    // { root: true } );

    },

    // async fleekUploadFromState( { state }, event) {
    //   console.log('fleekUpload: ', event)
    //   const input = {
    //     apiKey: 'RmOhy96hLwmuDBsOueAq5g==',
    //     apiSecret: 'ryBoPW0b7RYn4qasQYtlCwMBgb0kSD7AU4ZSTj5Br7s=',
    //     key: `productImg/${state.img.name}`,
    //     data: state.img };
    //   const res = await fleek.upload(input);
    //   console.log('upload res: ', res)
    //   // const data = { update: res.publicUrl };
    //   // return await axios.post(`/ecom/update_db/${event.product_id}`, data );
    //   return await axios.post(`/ecom/update_db/${event.product_id}`, { update: res.publicUrl } );
    // },

    // async fleekUploadStr( { state, commit }, event) {
    //       console.log('fleekUpload: ', event)

    //       const input = {
    //         apiKey: 'RmOhy96hLwmuDBsOueAq5g==',
    //         apiSecret: 'ryBoPW0b7RYn4qasQYtlCwMBgb0kSD7AU4ZSTj5Br7s=',
    //         key: `productImg/${event.name}`,
    //         data: event,
    //       };
    //       const res = await fleek.upload(input);

    //       // commit('uploadImg', res.publicUrl)
    //       // commit('UPDATE_IMG_LIST', res.publicUrl)
    //       console.log('upload res: ', res)
    //       return await axios.post(`/update_db/${event.product_id}`, { data: res.publicUrl } );
    //   },
  };
  // const modules = {};
  export default {
    namespaced: true,
    state,
    mutations,
    getters,
    actions
  };