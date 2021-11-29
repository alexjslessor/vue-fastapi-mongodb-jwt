<template>

  <v-card-actions class='mx-auto'>
    <v-toolbar-items>
    <!-- <v-toolbar-items v-if='cartSize' class='hidden-xs-only'> -->

          <v-menu offset-x right bottom open-on-hover min-width='240' close-delay='1300'>


            <!-- ICON -->
            <template v-slot:activator="{ on, attrs }">
              <v-btn icon class='pb-2' v-bind="attrs" v-on="on" :to="routeTo" >
                <v-badge left color="green" class='mt-4'>
                  <span slot="badge">{{ totalQty }}</span>
                  <v-icon color='white'>mdi-cart</v-icon>
                </v-badge>
              </v-btn>
            </template>



            <v-list>
              <v-subheader>Order</v-subheader>
              <v-divider></v-divider>

              <v-list-item v-for="(item, idx) in cartArray" :key="idx">

                <v-list-item-content>

                    <v-list-item-title>
                          {{ item.product_name }}
                    </v-list-item-title>

                  <v-list-item-subtitle>
                    {{ item.subtotal }}
                  </v-list-item-subtitle>
                </v-list-item-content>

                <v-list-item-action>
                    <v-list-item-title>x {{ item.quantity }}</v-list-item-title>
                </v-list-item-action>
                
              </v-list-item>
            </v-list>



            <v-divider></v-divider>


            
            <v-list>
              <v-list-item>
                <v-list-item-title>Total $(USD)</v-list-item-title>
                <br/>
                <!-- <v-list-item-action> -->
                    <v-btn color='primaryopposite' class='pr-2 font-weight-bold' style='color: white;'>
                      <v-icon color="grey lighten-1">mdi-cash</v-icon>
                      <v-list-item-subtitle class='font-weight-bold'>{{ totalPrice }}</v-list-item-subtitle>
                    </v-btn>
                <!-- </v-list-item-action> -->
              </v-list-item>
            </v-list>

          </v-menu>

    </v-toolbar-items>
  </v-card-actions>
</template>
<script>
export default {
props: {
  cartArray: {
      type: Array,
      required: false
    },
    routeTo: {
      type: String,
      required: false
    },
    totalQty: {
      type: Number,
      required: false
    },
    totalPrice: {
      type: Number,
      required: false
    },
  },
}
</script>