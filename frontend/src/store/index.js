import Vue from 'vue'
import Vuex from 'vuex'
import auth_jwt from './modules/auth_jwt'
import stripe from './modules/stripe'
import blog from './modules/blog'
import imgHandler from './modules/imgHandler'

Vue.use(Vuex)

export default new Vuex.Store({

  modules: {
    debug: true,
    auth: auth_jwt,
    stripe: stripe,
    blog: blog,
    imgHandler: imgHandler,
  }

});

