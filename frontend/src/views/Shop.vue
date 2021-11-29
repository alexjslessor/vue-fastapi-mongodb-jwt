<template>
  <div>
    <v-container fluid>
      <v-row>
        <!-- {{ getProductState }} -->
        <v-col>
          <!-- <ProductCard /> -->
          <ProductCard :cardData="getProductState" />
          <!-- <ProductCard :cardData='productsArr' /> -->
          <!-- <StripeProductCard :cardData='items'/> -->
          <!-- <StripeProductCard :cardData='getProducts'/> -->
          <!-- <StripeOneTime/> -->
          <!-- <StripeCheckout/> -->
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
  <script>
// import StripeProductCard from '@/components/StripeProductCard';
// import StripeOneTime from '@/components/StripeOneTime';
// import StripeCheckout from '@/components/StripeCheckout';
import ProductCard from "@/components/ecom/ProductCard";
import { mapGetters, mapActions } from "vuex";
export default {
  components: {
    ProductCard,
    // StripeProductCard,
    // StripeOneTime,
    // StripeCheckout,
  },
  data: () => ({
    productsArr: [],
  }),

  computed: {
    ...mapGetters({
      // getCart: 'stripe/getCart',
      getProductState: "stripe/getProductState",
    }),
  },

  // methods: {
  // ...mapActions(['query_products', 'stripe/query_db']),
  // },

  // async beforeCreate() {
  //     await this.$store.dispatch('stripe/query_products', {query: 'all_products', filter: 'all'});
  // }

  // async created() {
  //   //   // Commit products to product store
  //   // this.productsArr = await this.$store.dispatch('stripe/query_db', {query: 'all_products', filter: 'all'});
  //   await this.$store.dispatch('stripe/query_products', {query: 'all_products', filter: 'all'});
  //   }
};
</script>
    