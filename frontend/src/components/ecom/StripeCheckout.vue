<template>
    <div>

      <button @click="submit">Pay now!</button>
    </div>
  </template>
  <script>
  import { mapGetters, mapActions } from 'vuex';
  import axios from 'axios'
  let stripe = Stripe('pk_test_IO25CKyOll75V93WOyjViUyR00wcfxjKAf');

  export default {
    // components: {},
    data() { return {};},
    methods: {
        // ...mapActions(['getProductsApi']),
        async submit() {
          // https://stripe.com/docs/payments/accept-a-payment?integration=checkout#add-an-event-handler-to-the-checkout-button
          await axios
          .post(`/shop/create-checkout-session`)
          .then(resp => {
            console.log('checkout ', resp)
            stripe.redirectToCheckout({ sessionId: resp.data.id });
          })
      }

    },

    async created() { this.lineItems = await this.getProductsApi({route: 'all_active_products', product_id: 'xx'}); }

  };
  </script>