<template>
    <v-overlay :value="loadOverlay">
        <v-progress-circular indeterminate size="64">
        </v-progress-circular>
      </v-overlay>  
</template>
<script>
    import { mapActions, mapState } from "vuex";
    export default {
      components: {},

      data() {
        return {
        //   show: false,
        //   overlay: false,
        };
      },
      
    //   methods: {
        // ...mapActions({login: "authUser"}),
    // },
  
    computed: {

      ...mapState('auth', ['status']),

      loadOverlay() {
        if (status === 'loading') {
            return true
          } else if (status !== 'loading') {
            return false
          }
      }

    //   loadOverlay() {
    //     if (status === 'loading') {
    //         return true
    //       } else if (this.$store.state.status === 'success' || this.$store.state.status === "" || this.$store.state.status === 'error') {
    //         return false
    //       }
    //   }
    }
  
  
  };
  </script>
  
