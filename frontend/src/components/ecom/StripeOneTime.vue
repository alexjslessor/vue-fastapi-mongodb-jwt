<template>
    <div>
      <stripe-checkout
        ref="checkoutRef"
        mode="payment"
        pk="pk_test_IO25CKyOll75V93WOyjViUyR00wcfxjKAf"
        :line-items="lineItems"
        :success-url="successURL"
        :cancel-url="cancelURL"
        @loading="v => loading = v"
      />
      <button @click="submit">Pay now!</button>
    </div>
  </template>
  <script>
  import { StripeCheckout } from '@vue-stripe/vue-stripe';
  import { mapGetters, mapActions } from 'vuex';
  export default {
    components: {
      StripeCheckout,
    },
    data () {
    //   this.publishableKey = process.env.STRIPE_PUBLISHABLE_KEY;
      return {
        // publishableKey: process.env.STRIPE_PUBLISHABLE_KEY,
        successURL: 'http://localhost:8080/order_history',
        cancelURL: 'http://localhost:8080/dashboard',
        loading: false,
        // lineItems: [],
        lineItems: [
          {
            price: 'price_1GufTqLnbk9JaPUlw0sQVPx8', // The id of the one-time price you created in your Stripe dashboard
            quantity: 1,
          },
        ],
      };
    },
    methods: {
        ...mapActions(['getProductsApi']),

      async submit() {
        // You will be redirected to Stripe's secure checkout page
        await this.$refs.checkoutRef.redirectToCheckout();
      },
    },

    async created() { this.lineItems = await this.getProductsApi({route: 'all_active_products', product_id: 'xx'}); }

  };
  </script>