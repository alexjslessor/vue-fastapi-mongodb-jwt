<template>

<v-container fluid class="mt-3 my-12">
  <v-layout column wrap>
    <v-flex xs6 sm6 md6 lg6 xl6 v-for="(product, idx) in cardData" :key="idx">

      <p>{{ product }}</p>

      <v-hover v-slot:default="{ hover }">
        <v-card
          class="mx-auto mb-5"
          color="black lighten-4"
          max-width="600">

          <v-img :src="product.product_img" @click.native=''>
          <!-- <v-img :src="post.images[0]" @click.native=''> -->
            <v-expand-transition>
              <div
                v-if="hover"
                class="d-flex transition-fast-in-fast-out red darken-2 v-card--reveal display-3 white--text"
                style="height: 100%;">
              </div>
            </v-expand-transition>
          </v-img>
          
          <v-card-actions>
            <v-btn @click='addToCart(product)'>Add to Cart</v-btn>
            <v-spacer></v-spacer>
            <v-row alignment="center" justify="end">
              <v-text-field style='color: black;' type='number'>
                <v-icon slot="append" color="red"> mdi-plus</v-icon>
                <v-icon
                  slot="prepend"
                  color="green">
                  mdi-minus
                </v-icon>
              </v-text-field>
            </v-row>
          </v-card-actions>

      </v-card>
      </v-hover>
      
    </v-flex>

  </v-layout>
</v-container>

</template>
<script>
    export default {
      props: {
        cardData: {
          type: Array,
          required: false
        },
      },
      data() {
        return {
          rating: 4.3,
          ascending: false,
          quantity: 0,
        };
      },
  
      methods: {
  
        goToProduct(productId) {
          // this component is used for the individual product page as well.
          // if statement prevents warning on sku specific product page.
          if (this.$router.currentRoute.name === 'Shop') {
              this.$router.push(`/shop/${productId}`);
          } else { }
        },

        addToCart(product) {
          console.log('item:  ', product);
          this.$store.dispatch('addProductToCart', product);
        },
    },
};
</script>
<style>
  .v-card--reveal {
    align-items: center;
    bottom: 0;
    justify-content: center;
    opacity: .5;
    position: absolute;
    width: 100%;
  }
  </style>
