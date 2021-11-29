<template>
<v-app>
    <!-- <NavBar v-if="viewportSize === 'mobile'" /> -->
    <!-- <NavHover v-if="viewportSize === 'desktop'" /> -->
    <!-- <Appbar /> -->
    <!-- <Sidebar /> -->
    <NavTestOne :links='routerLinks' />

    <v-main>
      <v-container fluid>
        <transition name='fade'>
        <!-- <transition name="slide" enter-active-class="animated slideInRight delay" leave-active-class="animated slideOutLeft"> -->
          <router-view></router-view>
        </transition>
        
        <!-- <SpeedDial/> -->

      </v-container>

    </v-main>

    <snackbar/>

   <!-- <v-footer app> -->
    <!-- <span class="mx-auto">Pirate Bay&copy; {{ new Date().getFullYear() }}</span> -->
   <!-- </v-footer> -->

  </v-app>
</template>
<script>
// import { mapGetters, mapActions } from 'vuex'
// import Appbar from '@/components/navBars/Appbar'
// import Sidebar from '@/components/navBars/Sidebar'
import NavTestOne from '@/components/navBars/NavTestOne'
import snackbar from '@/components/fragments/snackbar'
import SpeedDial from '@/components/fragments/SpeedDial'

export default {
  name: 'App',
  components: {
    snackbar,
    // Appbar,
    // Sidebar,
    NavTestOne,
    SpeedDial,
  },

  // async beforeCreate() {
  //   await this.$store.dispatch('stripe/query_products', {query: 'all_products', filter: 'all'});
  // },
  
  computed: {

    routerLinks() {
      let links = [
      {
        to: "/",
        icon: "mdi-home",
        text: "Home",
        divider: true,
      }, 
      {
        to: "/shop",
        icon: "mdi-cart",
        text: "Shop",
        divider: true,
      },  
      {
        to: "/blog",
        icon: "mdi-book",
        text: "Blog",
        divider: true,
      },   
      {
        to: "/dashboard",
        icon: "mdi-monitor-dashboard",
        text: "Dashboard",
        divider: true,
      },    
    ]

    return links
    },

    viewportSize() {
      // https://material.io/design/layout/responsive-layout-grid.html#breakpoints
      const vw = Math.max(document.documentElement.clientWidth || 0, window.innerWidth || 0)
      // const vh = Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0)
      if (vw >= 599) {
        return 'desktop';
      } else if (vw < 599) {
        return 'mobile';
      }
      // console.log(vw, vh)
    }
  },


  
};
</script>
