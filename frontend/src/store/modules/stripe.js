import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";
import router from "@/router/index";
import fastapi from '../../api/fastapi'
import axiosHeaders from '../../main'
import { SET_SNACKBAR } from '../mutation-types'
// import { SET_STATUS } from '../mutation-types'

Vue.use(Vuex)

  const state = {
    cart: [],
    // productState: null,
    productState: [],
    // productState: window.localStorage.getItem("productState") || [],
    shipment: [],
    shippedOrders: [],
    // stripe: '',
    // elements: '',
    // card: '',
  };

  // - gets data from the state
  // - are computed properties
  // - are syncronous
  const getters = {
    // getProductState: state => JSON.parse(state.productState),
    getProductState: state => state.productState,
    getCartSize: state => state.cart.length,
    getCart: state => state.cart,

    cartTotalPrice(state) {
      let total = 0;
      state.cart.forEach(item => {
        total += item.price * item.quantity;
      });
      return total
    },
    total_cart_quantity(state) {
      let sum_qty = state.cart.reduce((accum, item) => accum + parseInt(item.quantity), null);
      return sum_qty;
    },

    getProductStateById: (state) => (id) => {
      // return state.products.filter(i => i.product_id === id)// return array
      return state.productState.find(i => i.product_id === id)// returns object
    },

    getProductStateIDX:(state) => (productObj) => {
      return state.productState.indexOf(productObj);
    }

  };
  // - updates state
  // - convention to use uppercase letters for mutations
  const mutations = {
    // SHIPPED_ORDERS(state, data) {
    //   state.shippedOrders = data;
    // },

    CLEAR_ITEMS(state, which_state) { 
      if (which_state === 'cart') {
        state.cart = [];
      } else if (which_state === 'shipment') {
        state.shipment = [];
      }
    },

    clearSnack(state) {
      state.content = "";
      (state.bottom = false), (state.btnColor = "");
      (state.color = ""), (state.visible = false);
    },

    REMOVE_PRODUCT_FROM_CART(state, product) {
      // ProductCard.vue
      state.cart = state.cart.filter(item => {
        return item.productId !== product.product_id;
      })
    },

    REMOVE_PRODUCT_FROM_CART_V2(state, obj) {
      // CannaCheckout.vue
      state.cart.splice(obj, 1);
    },

    ADD_TO_CART(state, item) {
      //p 351 complete_vue_webdev
      console.log('ADD_TO_CART: ', item);
      let product = state.cart.find(p => {
        if(p.productId == item.product_id) {
          // if(item.quantity == 0) {
            // p.quantity = 0
          // }
          p.quantity + item.quantity;
          p.subtotal += item.price;
          return p;
        }
      });
      // console.log('product find: ', state.cart);
      if(!product) {
        state.cart.push({
          productId: item.product_id,
          priceId: item.price_id,
          name: item.product_name,
          description: item.product_description,
          image: item.product_img,
          price: item.price,
          quantity: 1,
          subtotal: item.price,
        });
      }
    },

    UPDATE_CART(state, item) {
      // console.log('UPDATE_CART: ', item);
      let product = state.cart.find(p => {
        if(p.productId == item.product_id) {
          p.quantity = item.quantity;
          p.subtotal = (item.quantity * item.price);
          return p;
        }
      });
    },

    RESET_PRODUCT_STATE(state, item) {
      let product_state = state.productState.find(p => {
        console.log('p.productId', p.productId)
        console.log('item.product_id', item.product_id)

        if(p.product_id === item.productId) {
          p.quantity = 0;
          p.subtotal = 0;
          return p;
        }
      });
    },

    // PROD_CART_UPDATE(state, item) {
    //   console.log('up: ', item.quantity)
    //   let product = state.cart.find(p => {
    //     // if(p.productId == item.productId) {
    //     if(p.productId == item.product_id) {

    //       p.quantity = (p.quantity + item.quantity);
    //       p.subtotal = (p.quantity * item.price);
    //       return p;
    //     }
    //   });
    //   if(!product) {
    //     state.cart.push({
    //       productId: item.product_id,
    //       priceId: item.price_id,
    //       name: item.product_name,
    //       description: item.product_description,
    //       image: item.product_img,
    //       price: item.price,
    //       quantity: 1,
    //       subtotal: item.price,
    //     });
    //   }

    // },

    UPDATE_PROD_QTY(state, item) {
      // ProductCard.vue
      state.productState.splice(item, 0);

      let product = state.cart.find(p => {
        if(p.productId == item.product_id) {
          p.quantity = item.quantity;
          p.subtotal = item.subtotal
          return p;
        }
      });

      if(!product) {
        state.cart.push({
          productId: item.product_id,
          priceId: item.price_id,
          name: item.product_name,
          description: item.product_description,
          image: item.product_img,
          price: item.price,
          quantity: 1,
          subtotal: item.price,
        });
      }



    },

    SET_PRODUCT_STATE(state, resp) {
      state.productState = resp;
      window.localStorage.setItem("productState", resp);
      console.log('productState: ', state.productState);
    },



  }

  const actions = {

    remove_product_from_cart({ commit, state }, obj ) {
      commit('RESET_PRODUCT_STATE', obj);
      // splice item from cart.
      // commit('REMOVE_PRODUCT_FROM_CART', obj);
      commit('REMOVE_PRODUCT_FROM_CART_V2', obj.productId);
      // check if cart empty/
      if ( state.cart.length == 0 ) {
        // if cart empty redirect to /shop page.
        router.push('/shop');
      }
    },

    add_item_to_shipment({ commit }, item) {
      commit('ADD_ITEM_TO_SHIPMENT', item);
    },
    clearCartItems({ commit }) {
      commit('CLEAR_CART_ITEMS');
    },
    infoSnackBar({ commit }, info) {
      commit(SET_SNACKBAR, {cardColor: info.color, 
                            btnColor: '', 
                            content: info.statusText + ": " + info.data.info}, { root: true });
    },


    async query_db({ }, event) {
      // either commit to store or retturn
      const url = `/query_db/${event.query}/${event.filter}`;
      let resp = await axiosHeaders.get(url)
      return resp.data;
    },

    async read_products({ state, commit, dispatch }) {
        const url = `/read/stripe/product/all`;
        let resp = await axiosHeaders.get(url)
        console.log('read_products: ', resp)
        commit('SET_PRODUCT_STATE', resp.data);
    },

    // async query_products({ state, commit, dispatch }, event) {
    //   // if(!state.productState.length ) {
    //     console.log('event', event);
    //     const url = `/query_db/${event.query}/${event.filter}`;
    //     let resp = await axiosHeaders.get(url)
    //     // let resp = dispatch('query_db', event)
    //     console.log('query products: ', resp)
    //     commit('SET_PRODUCT_STATE', resp.data);
    //   // } else {
    //     // console.log('state already loaded')
    //   // }
    // },


    async postForm({ }, obj) {
      console.log('postform', obj)
      Array.from(obj.product_img_list).map(image => {
          const newForm = new FormData();
          newForm.append('name', obj.product_name);
          newForm.append('description', obj.product_description);
          newForm.append('price', obj.price);
          newForm.append('shipping_cost', obj.shipping_cost);
          newForm.append('img_list', image);
          return axios.post('/post_form', newForm);
      });
    },

    async uploadImages({ }, image_file) {
      console.log('image_file:   ', image_file);
      fastapi.postImageFormFastApi(image_file);
    },


    // async cartCheckout({ state }) {
    //   const cart_items = { cart: state.cart };
    //   await axios
    //       .post(`/cart-checkout`, { cart_items })
    //       .then(resp => {
    //           // console.log('checkout ', resp)
    //           this.payWithCard(this.stripe, this.card, resp.data.clientSecret);
    //       })
    // }
};



  export default {
    namespaced: true,
    state,
    mutations,
    getters,
    actions
  };

