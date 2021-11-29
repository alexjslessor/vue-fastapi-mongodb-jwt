<template>

  <v-container>
    <v-flex xs12 sm12 md12 lg12 xl12 class='mx-auto pt-4'>

      <v-card elevation='20'>
        <v-card-text>
          <v-container pa-0>
            <v-row justify='space-between'>
              <v-col xs='12' xl='6'>
                <v-card outlined tile>

                  
                  <v-carousel cycle :show-arrows="false">
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
                          <!-- <v-list-item-title v-text="item.price"></v-list-item-title> -->
                          <v-list-item-subtitle class="title font-weight-bold text--primary">
                            Price: {{ item.price }}
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
                        <!-- <v-list-item-subtitle class="text--primary" v-text="item.product_description"></v-list-item-subtitle> -->
                        <v-list-item-content class='title font-weight-bold text-justify' v-text="item.product_description"></v-list-item-content>
                      </v-list-item>


                      <v-list-item class='mx-auto'>

                        <v-col md='12'>
                        <!-- <v-list-item-action> -->
                        <v-text-field dense >
                          <!-- <v-btn icon> -->
                          <v-icon small slot="append" color="green">
                            mdi-plus
                          </v-icon>
                          <!-- </v-btn> -->
                          <!-- <v-btn icon> -->
                          <v-icon small slot="prepend" color="red">
                            mdi-minus
                          </v-icon>
                          <!-- </v-btn> -->
                        </v-text-field>
                        <!-- </v-list-item-action> -->


                        <v-list-item-action >
                          <v-btn small color='secondary'>
                            <!-- <v-btn small color='secondary' @click='addToCart(item)'> -->
                            <v-icon small color='primary' class='pr-2'>mdi-cart</v-icon>
                            Add to Cart
                          </v-btn>
                        </v-list-item-action>
                        
                      </v-col>

                      </v-list-item>

                    </v-list-item-group>
                  </v-list>

                  <!-- <v-divider light color='white'></v-divider> -->
                  <!-- <v-spacer></v-spacer> -->

                  <v-tabs class='mt-4' fixed-tabs background-color="deep-purple accent-4" center-active dark>
                    <v-tab>One</v-tab>
                    <v-tab>Two</v-tab>
                    <v-tab>Three</v-tab>
                  </v-tabs>



                </v-card>
              </v-col>

            </v-row>
          </v-container>
        </v-card-text>
      </v-card>
    </v-flex>
  </v-container>


</template>
<script>
  import { mapActions, mapGetters } from 'vuex';
  export default {
    props: ['productId'],
    components: {
    },

    data() {
      return {
        item: {},
        // item: this.getProductById(pid),
        qty: 0,

      }
    },

    computed: {
      ...mapGetters(
        {
          getUserType: 'getUserType',
          getProductById: 'getProductById'
        }
      ),
    },

    methods: {
      ...mapActions({ query_db: 'stripe/query_db' }),
    },

    async created() {
      // await this.getProduct()
      this.item = await this.query_db({ query: 'product_id', filter: this.productId })

      console.log('obj item', this.item)

    },

  };
</script>