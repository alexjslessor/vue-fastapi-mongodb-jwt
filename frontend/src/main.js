import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import axios from 'axios'
import "./vee-validate";
import { TiptapVuetifyPlugin } from 'tiptap-vuetify'
import './assets/reset.css';
// require("animate.css/animate.compat.css");

axios.defaults.baseURL = process.env.VUE_APP_URL;

const axiosHeaders = axios.create({
  baseURL: process.env.VUE_APP_URL,
  headers: { 'Authorization': `Bearer ${window.localStorage.getItem('accessToken')}` }
})
axiosHeaders.interceptors.response.use(function (response) {
  return response
}, function (error) {
  console.log('error: ', error)
  if (error.response.status == 401) {
      store.dispatch('auth/refreshAuth')
  }
  return Promise.reject(error)
})
export default axiosHeaders


Vue.use(TiptapVuetifyPlugin, {
  vuetify,
  iconsGroup: 'md'
})


Vue.config.productionTip = false;
Vue.prototype.$ECOM_AUTH = process.env.VUE_APP_ECOM_PUBLIC;

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
