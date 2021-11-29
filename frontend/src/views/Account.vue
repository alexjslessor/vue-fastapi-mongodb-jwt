<template>
    <div>
        <ChangePassword :currentUsername='getUsername'/>
    </div>
</template>
<script>
  import { mapActions, mapGetters } from 'vuex';
  import ChangePassword from '@/components/forms/auth/ChangePassword'
  export default {
    components: {
        ChangePassword
    },

    computed: {
    
      ...mapGetters({
        getUsername: 'auth/GET_USERNAME'
      }),

  }
    // methods: mapActions(['finalizeLogin']),
    // // "http://localhost:8080/callback?code=AB11613499141vBzraIsUQTWp8VJAtAbwBju3k6XpH0dI0Gzdq&state=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdXRoZW50aWNhdGlvbl9iYWNrZW5kIjoiand0IiwiYXVkIjoiZmFzdGFwaS11c2VyczpvYXV0aC1zdGF0ZSIsImV4cCI6MTYxMzUwMjMyNH0.ZDrz-S9jVqJBPN45FthnD8hqzjFO_taNTMekb6ROfJQ&realmId=null"
    // created() {
    //   console.log('window location About: ', window.location)
    //   this.finalizeLogin(window.location.search);
    // }
  };
</script>