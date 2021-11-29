<template>
<div>
    <v-app-bar app dense clipped-left>
      
      <router-link to="/" style="cursor: pointer">
          <img src="@/assets/img/logo.png" width="47" height="32" />
      </router-link>
  
      <!-- <v-toolbar-title class="ml-2">Appbar Name</v-toolbar-title> -->
  
      <v-spacer></v-spacer>
  
      <CartIcon v-if='getCart.length >= 1' 
        :cartArray='getCart' 
        routeTo='/checkout' 
        :totalQty='total_cart_quantity'
        :totalPrice='cartTotalPrice' />
  
      <!-- <v-toolbar-title v-else='getCart.length == 0' class="mx-auto font-weight-bold"> -->
        <!-- {{ $route.name }} -->
      <!-- </v-toolbar-title> -->
  
      <v-spacer></v-spacer>
      <v-menu bottom offset-y>
        
        <template v-slot:activator="{ on, attrs }">
          <v-btn icon v-bind="attrs" v-on="on" class="pr-2">
            <v-icon color='primary'>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>
  
        <v-list>
          <ListItem v-if='!isLoggedIn' @click='login' itemText='Login' itemIcon='mdi-login-variant' />
          <ListItem v-if='isLoggedIn' itemText='Account' :to='{ path: `account` }' itemIcon='mdi-account-settings-outline' />
          <ListItem v-if='isLoggedIn' @click='logout' itemText='Logout' itemIcon='mdi-logout-variant' />
        </v-list>
  
      </v-menu>
    </v-app-bar>

<!-- ######################################## -->

<!-- <div> -->
  <!-- <v-card> -->
<v-navigation-drawer app clipped permanent expand-on-hover>
  <!-- <v-navigation-drawer app permanent v-model="drawer" :mini-variant.sync="mini"> -->
    <v-list nav dense>
      <div v-for="(link, i) in links" :key="i">

        <v-list-item exact v-if="!link.subLinks" :to="link.to" class="mt-1">
          <v-list-item-icon>
            <v-icon>{{ link.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-title v-text="link.text" />
        </v-list-item>

        <v-list-group
          v-else
          :key="link.text"
          :prepend-icon="link.icon"
          :value="false">

          <template v-slot:activator>
            <v-list-item-title>{{ link.text }}</v-list-item-title>
          </template>

          <v-list-item
            link
            exact
            v-for="sublink in link.subLinks"
            :to="sublink.to"
            :key="sublink.text"
            class="mb-1">

            <v-list-item-icon>
              <v-icon>{{ sublink.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-title>{{ sublink.text }}</v-list-item-title>
          </v-list-item>
        </v-list-group>
        <v-divider />
      </div>
    </v-list>
  </v-navigation-drawer>

  <!-- </v-card> -->
  <!-- </div> -->

</div>

</template>  
<script>
import { mapActions, mapGetters } from "vuex";
import CartIcon from '@/components/navBars/CartIcon';
import ListItem from '@/components/fragments/ListItem';
  
  export default {
    props: {
        links: {
            type: Array,
            required: true
        }
    },

    components: {
      CartIcon,
      ListItem,
    },

    data: () => ({
      // drawer: true,
      // mini: true,
  }),
  
    methods: {
          ...mapActions({ logoutUser: "auth/LOGOUT_ACTION" } ),

      login() {
          if (this.$router.currentRoute.name != 'Login' ) {
            this.$router.push( { name: 'Login' } );
          }
      },
      // login() {
      //     if (this.$router.currentRoute.path !== '/auth/login') {
      //       this.$router.push('/auth/login')
      //     }
      // },

      logout() {
        this.logoutUser()
      }
  
    },
    computed: {
      ...mapGetters({
        isLoggedIn: "auth/GET_USERNAME", 
        getCart: 'stripe/getCart',
        cartTotalPrice: 'stripe/cartTotalPrice',
        total_cart_quantity: 'stripe/total_cart_quantity',
      }),
    
    },
  
  
  };
  </script>
  