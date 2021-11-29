import axios from "axios";
import axiosHeaders from '../../main'

const state = {
    title: '',
    headline: '',
    img: null,
    content: ''
  };

  // getters get data from the state
  // Getters are computed properties
  // syncronous
  const getters = {
    getPostTitle: state => state.title,
    getPostHeadline: state => state.headline,
    getPostImg: state => state.img,
    getPostContent: state => state.content,
  };

  //mutations update the state
  //convention to use uppercase letters for mutations
  const mutations = {

    CLEAR_BLOG_STATE(state) {
      state.title = '';
      state.content = '';
    },
    updateTitle(state, data) {
        state.title = data;
    },
    updateHeadline(state, data) {
      state.headline = data;
  },
    updateImage(state, data) {
      console.log('image: ', data)
      
      state.img = data;
    },
    updateContent(state, data) {
      state.content = data;
    }

  };

  const actions = {

    // createPost( { state } ) {

    //   const newBlogPost = {
    //     title: state.title, 
    //     headline: state.headline, 
    //     content: state.content}

    //   // console.log('newPost: ', newBlogPost)

    //   // axios.post('/post_blog_form', newBlogPost)
    //   // .then(resp => {
    //   //   console.log('post json: ', resp)
    //   // })

    //   Array.from(state.img).map(image => {

    //       const postImage = new FormData();
    //       postImage.append('headline_image', image)

    //       axios.post('/post_blog_form', newBlogPost )
    //       .then(resp => {
    //         console.log('json: ', resp)
    //         // axios.post('/post_blog_form', postImage).then(resp => { console.log('form: ', resp) })
    //       })
    //   });

    // },

      createPost( { state } ) {
        // console.log('create post state action')
        // Array.from(state.img).map(image => {
            const newForm = new FormData();  
            newForm.append('title', state.title)
            newForm.append('headline', state.headline)
            newForm.append('headline_image', state.img)
            // newForm.append('headline_image', image)
            // newForm.append('imageList', image)
            newForm.append('content', state.content)
            // console.log('newForm: ', newForm)
            return axios.post('/post_blog_form', newForm);
        // });
    },

    async readPost({}, pid) {
      return await axios.get(`/single_post/${pid}`)
    },

    async query_db({ }, event) {
      // either commit to store or retturn
      const url = `/blog/query_db/${event.query}/${event.filter}`;
      let resp = await axiosHeaders.get(url)
      return resp.data;
    },


  };

  export default {
    namespaced: true,
    state,
    mutations,
    getters,
    actions
  };