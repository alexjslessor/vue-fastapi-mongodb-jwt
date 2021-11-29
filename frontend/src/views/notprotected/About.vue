<template>
    <div>
    <v-row class='mx-auto' justify='center'>

    <v-col cols='10'>

        <v-card class="pa-4" flat height="300px" img="https://cdn.vuetifyjs.com/images/toolbar/map.jpg">

        <v-toolbar dense floating>

          <v-text-field
            hide-details
            prepend-icon="mdi-magnify"
            single-line
          ></v-text-field>
    
          <v-btn icon>
            <v-icon>mdi-crosshairs-gps</v-icon>
          </v-btn>
    
          <v-btn icon>
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </v-toolbar>
      </v-card>
  </v-col>
</v-row>
</div>
</template>
<script>
  import { mapActions } from 'vuex';
  export default {

    methods: mapActions(['finalizeLogin']),
    // "http://localhost:8080/callback?code=AB11613499141vBzraIsUQTWp8VJAtAbwBju3k6XpH0dI0Gzdq&state=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdXRoZW50aWNhdGlvbl9iYWNrZW5kIjoiand0IiwiYXVkIjoiZmFzdGFwaS11c2VyczpvYXV0aC1zdGF0ZSIsImV4cCI6MTYxMzUwMjMyNH0.ZDrz-S9jVqJBPN45FthnD8hqzjFO_taNTMekb6ROfJQ&realmId=null"
    created() {
      console.log('window location About: ', window.location)
      this.finalizeLogin(window.location.search);
    }
  };
</script>