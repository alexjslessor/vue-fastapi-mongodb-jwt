<template>
  <v-container>
    <v-flex xs12 sm12 md12 lg12 xl12 class='mx-auto pt-4'>

      <!-- {{ getCart }} -->
      <v-card elevation='20'>
        <v-card-text>
          <v-container pa-0>
            <v-row justify='space-between'>


              <v-col xs='12' xl='6'>
                <v-card outlined tile>
                  <v-carousel show-arrows-on-hover cycle interval='2000' :show-arrows="false">
                    <v-carousel-item v-for="(image, i) in item.product_img" :key="i" :src="image"></v-carousel-item>
                  </v-carousel>
                </v-card>
              </v-col>

              <v-col xs='12' xl='6'>
                <v-card elevation='11'>

                  <v-card-title class='headline font-weight-bold'>{{item.product_name }}</v-card-title>

                  <v-list flat two-line>
                    <v-list-item-group>


                      <v-list-item>

                        <v-list-item-content>
                          <v-list-item-subtitle class="title font-weight-bold text--primary">
                            <v-icon medium right>mdi-currency-usd</v-icon>
                            {{ item.price }}
                          </v-list-item-subtitle>
                        </v-list-item-content>


                        <v-list-item-action>

                          <v-col align="center" class="mx-0">
                            <v-rating :value="4.5" color="amber" dense half-increments readonly size="14"></v-rating>

                            <div class="grey--text ms-4">
                              4.5 (413)
                            </div>
                          </v-col>

                        </v-list-item-action>

                      </v-list-item>

                      <v-list-item>
                        <v-list-item-content class='title font-weight-bold text-justify' v-text="item.product_description"></v-list-item-content>
                      </v-list-item>



                    </v-list-item-group>
                  </v-list>


                  <v-card flat>
                    <v-container>
                      <v-row justify='space-between'>

                        <v-col align='center' xs='12' xl='4' class='mx-0'>

                          <v-text-field readonly persistent-hint v-model='item.quantity' hint='Qty' type='number'>
                            <v-btn x-small slot="append-outer" color="green" @click="updateQty(item, 'incr')">
                              <v-icon>mdi-plus</v-icon>
                            </v-btn>
                            <v-btn x-small slot="prepend" color="red" @click="updateQty(item, 'decr')">
                              <v-icon>mdi-minus</v-icon>
                            </v-btn>
                          </v-text-field>

                        </v-col>

                      </v-row>
                    </v-container>
                  </v-card>



                  <v-tabs centered fixed-tabs background-color="deep-purple accent-4" v-model="tab">
                    <v-tab href='#tabone' class='font-weight-bold'>Description</v-tab>
                    <v-tab href='#tabtwo' class='font-weight-bold'>Reviews</v-tab>
                    <v-tab href='#tabthree' class='font-weight-bold'>Additional Information</v-tab>
                  </v-tabs>

                  <v-tabs-items :value="tab">
                    <!-- <v-tabs-items v-model="tab"> -->
                    <v-tab-item value='tabone'>
                      {{ item.product_description}}
                    </v-tab-item>

                    <v-tab-item value='tabtwo'>
                      <VTextAreaValidation solo filled rows='3' label='Comment' />
                    </v-tab-item>

                    <v-tab-item value='tabthree'>
                    </v-tab-item>
                  </v-tabs-items>


                </v-card>
              </v-col>

            </v-row>
          </v-container>
        </v-card-text>
      </v-card>

      <!-- <p> {{ item }}</p> -->
    </v-flex>
  </v-container>
</template>
<script>
  import { mapActions, mapGetters } from 'vuex';
  import VTextAreaValidation from '@/components/forms/inputs/VTextAreaValidation'

  export default {
    props: ['productId'],

    components: { VTextAreaValidation },

    data() {
      return {
        tab: null,
        // item: {},
        item: null,
        counter: 0,

      }
    },

    computed: {
      ...mapGetters(
        {
          getUserType: 'auth/getUserType',
          getProductById: 'auth/getProductById',
          getCart: 'stripe/getCart',
          getProductStateById: 'stripe/getProductStateById',
        }
      ),
    },

    methods: {
      ...mapActions({ query_db: 'stripe/query_db' }),


      // isInCart(newItem) {
      //   const index = this.getCart.findIndex(function (cartItem, index) {
      //     return cartItem.productId === newItem.product_id
      //   })
      //   // console.log('index', index)
      //   return index
      // },

      updateQty(item, which) {
        console.log(item, which)
        if (which == 'incr' && item.quantity >= 0) {
          item.quantity++
        } else if (which == 'decr' && item.quantity >= 1) {
          item.quantity--
        }

        if (item.quantity >= 1) {

          item.subtotal = (item.quantity * item.price)
          // this.$store.commit('stripe/PROD_CART_UPDATE', item);
          this.$store.commit('stripe/UPDATE_PROD_QTY', item);

        } else {
          // console.log('decr remove')
          this.$store.commit('stripe/REMOVE_PRODUCT_FROM_CART', item);
        }
      },




    },

    async created() {
      this.item = this.getProductStateById(this.productId)
      // this.item = await this.query_db({ query: 'product_id', filter: this.productId })
      console.log('Product.vue item: ', this.item)
    },

  };
</script>