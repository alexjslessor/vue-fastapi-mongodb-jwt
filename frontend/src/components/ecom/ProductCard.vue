<template>
  <v-container fluid>

    <v-data-iterator :items="cardData" :items-per-page.sync="itemsPerPage" :page.sync="page" :search="search" :sort-by="sortBy.toLowerCase()" :sort-desc="sortDesc" hide-default-footer>

      <template v-slot:header>
        <v-toolbar dark dense rounded color="secondary" class="mb-4">

          <template>
          <!-- <template v-if="$vuetify.breakpoint.xsAndUp"> -->
            <v-spacer></v-spacer>

            <v-text-field v-model="search" style='width: 50%;' clearable dense solo-inverted hide-details prepend-inner-icon="mdi-magnify" label="Search"></v-text-field>

            <v-spacer></v-spacer>

            <v-btn-toggle v-model="sortDesc" mandatory>
              <v-btn x-small depressed color="primary" :value="false">
                <v-icon color='secondary'>mdi-arrow-up</v-icon>
              </v-btn>

              <v-btn x-small depressed color="primary" :value="true">
                <v-icon color='secondary'>mdi-arrow-down</v-icon>
              </v-btn>
            </v-btn-toggle>

          </template>

        </v-toolbar>
      </template>


      <template v-slot:default="props">
        <v-layout row wrap>
          <v-layout column wrap v-for=" item in props.items" :key='item.product_id'>
            <v-flex xs12 sm11 md5 lg4 xl4 class='mx-auto pt-3'>

              <!-- <v-hover v-slot:default="{ hover }"> -->

                <v-container fluid>

                  <!-- <v-subheader>{{ type }}</v-subheader> -->

                      <v-hover v-slot:default="{ hover }">

                        <v-card rounded tile
                                :elevation="hover ? 20 : 1"
                                :class="{ 'on-hover': hover }">

                          <v-carousel :show-arrows="false">

                            <v-carousel-item 
                            v-for="(image, i) in item.product_img" 
                            :key="i" 
                            :src="image" 
                            height="300px" 
                            width='400px'
                            @click.native='goToProduct(item.product_id)'>
                            </v-carousel-item>
                          </v-carousel>


                        <v-card-title>
                          <span class="title font-weight-bold">{{ item.product_name }}</span>
                          <v-spacer></v-spacer>
                          <v-icon medium right>
                            mdi-currency-usd
                          </v-icon>
                          <span class="title font-weight-light">{{ item.price.toFixed(2) }}</span>
                        </v-card-title>


                        <v-card-actions class='float-center'>
                          <!-- ipad pro = 7 -->
                            <v-col cols='9' xs='8' sm='6' md='5' lg='5' xl='5'  class='mx-auto pa-2'>

                            <v-text-field readonly 
                                          persistent-hint 
                                          v-model='item.quantity' 
                                          hint='Qty'
                                          type='number'>
                              <v-btn x-small slot="append-outer" color="primary" @click="updateQty(item, 'incr')">
                                <v-icon>mdi-plus</v-icon>
                              </v-btn>
                              <v-btn x-small slot="prepend" color="purp" @click="updateQty(item, 'decr')">
                                <v-icon>mdi-minus</v-icon>
                              </v-btn>
                            </v-text-field>

                          </v-col>
                          <!-- {{ item }} -->
                          <!-- <v-spacer></v-spacer> -->
                          <!-- <v-btn class="float-right" color='black' @click='addToCart(item)'>
                            <v-icon small color='primary' class='pr-2'>mdi-cart</v-icon>
                            Add to Cart
                          </v-btn> -->
                        </v-card-actions>


                      </v-card>
                      </v-hover>
                    <!-- </v-col> -->
                  <!-- </v-row> -->
                </v-container>


            </v-flex>
          </v-layout>
        </v-layout>
      </template>

      <!-- FOOTER -->
      <template v-slot:footer>
        <v-container>

          <v-flex xs12 sm12 md10 lg10 xl9 class='mx-auto pt-3'>

        <v-row class="mt-4" align="center" justify="center">
          <span class="grey--text">Items per page</span>
          <v-menu offset-y>

            <template v-slot:activator="{ on, attrs }">
              <v-btn dark text color="primary" class="ml-2" v-bind="attrs" v-on="on">
                {{ itemsPerPage }}
                <v-icon>mdi-chevron-down</v-icon>
              </v-btn>
            </template>

            <v-list>
              <v-list-item v-for="(number, index) in itemsPerPageArray" :key="index" @click="updateItemsPerPage(number)">
                <v-list-item-title>{{ number }}</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>

          <v-spacer></v-spacer>

          <span class="mr-4 grey--text">
            Page {{ page }} of {{ numberOfPages }}
          </span>

          <v-btn fab dark small color="primary" class="mr-1" @click="formerPage">
            <v-icon>mdi-chevron-left</v-icon>
          </v-btn>

          <v-btn fab dark small color="primary" class="ml-1" @click="nextPage">
            <v-icon>mdi-chevron-right</v-icon>
          </v-btn>
        </v-row>
        </v-flex>
        </v-container>
      </template>


    </v-data-iterator>
  </v-container>

</template>
<script>
import { mapGetters, mapActions } from 'vuex'
  export default {
    component: {  },

    props: {
      cardData: {
        type: Array,
        required: false
      },
    },

    data() {
      return {
        itemsPerPageArray: [4, 8, 12],
        search: '',
        filter: {},
        sortDesc: false,
        page: 1,
        itemsPerPage: 12,
        sortBy: 'product_name',

        select_items: [
          { key_display: 'Product Name', key_name: 'product_name' },
          { key_display: 'Product Description', key_name: 'product_description' },
        ],

        types: ['Places to Be', 'Places to See'],
        cards: ['Good', 'Best', 'Finest'],

        socials: [
          {
            icon: 'mdi-facebook',
            color: 'indigo',
          },
          {
            icon: 'mdi-linkedin',
            color: 'cyan darken-1',
          },
          {
            icon: 'mdi-instagram',
            color: 'red lighten-3',
          },
        ],


      }
    },

    computed: {
      ...mapGetters({
          getCart: 'stripe/getCart', 
          getProductState: 'stripe/getProductState'
      }),

      numberOfPages() {
        // return Math.ceil(this.items.length / this.itemsPerPage)
        return Math.ceil(this.cardData.length / this.itemsPerPage)
      },

      filteredKeys() {
        return this.keys.filter(key => key !== 'product_name')
      },
    },


    methods: {

      getImage() {
        const min = 550
        const max = 560
        return Math.floor(Math.random() * (max - min + 1)) + min
      },

      // goToProduct(productId) {
      //   if (this.$router.currentRoute.name === 'Shop') {
      //     this.$router.push(`/${productId}/shop`);
      //   }
      // },

      goToProduct(productId) {
        if (this.$router.currentRoute.name === 'Shop') {
          this.$router.push(`/${productId}/shop`);
        }
      },

      // addToCart(item) {
        // console.log('item:  ', item);
        // this.$store.commit('stripe/ADD_TO_CART', item);
      // },

      updateQty(item, which) {
        console.log(item, which)
        if(which == 'incr' && item.quantity >= 0) {
            item.quantity++
          } else if(which == 'decr' && item.quantity >= 1) {
            item.quantity--
        }

        if(item.quantity >= 1) {

          item.subtotal = (item.quantity * item.price)
          // this.$store.commit('stripe/PROD_CART_UPDATE', item);
          this.$store.commit('stripe/UPDATE_PROD_QTY', item);
        
        } else {
          // console.log('decr remove')
          this.$store.commit('stripe/REMOVE_PRODUCT_FROM_CART', item);
        }
      },


      nextPage() {
        if (this.page + 1 <= this.numberOfPages) this.page += 1
      },
      formerPage() {
        if (this.page - 1 >= 1) this.page -= 1
      },
      updateItemsPerPage(number) {
        this.itemsPerPage = number
      },
    },




  }
</script>
<style scoped>
  /* .v-card--reveal {
    align-items: center;
    bottom: 0;
    justify-content: center;
    opacity: .5;
    position: absolute;
    width: 100%;
  } */

.v-card {
  -webkit-transition: all 0.2s ease-in-out;
  transition: opacity .02s ease-in-out;

  border-radius: 0px;
  /* background: linear-gradient(145deg, #131313, #101010); */
  box-shadow:  7px 7px 6px #010101, -7px -7px 6px #1d1d1d;
}

.v-card:not(.on-hover) {
  opacity: 0.9;
 }

/* .show-btns {
  color: rgba(255, 255, 255, 1) !important;
} */

/* .neumorph-card {
  border-radius: 0px;
  background: linear-gradient(145deg, #131313, #101010);
  box-shadow:  7px 7px 6px #070707, 
               -7px -7px 6px #1d1d1d;
} */
</style>