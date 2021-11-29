<template>
  <v-app dark>
    <v-content>
      <v-container>
        <player-title-bar></player-title-bar>
        template
      </v-container>
    </v-content>
  </v-app>
</template>
  
  <script>
import PlayerTitleBar from "@/components/videoplayers/PlayerTitleBar.vue"; // IMPORT the component

export default {
  components: {
    PlayerTitleBar,
  },
  data() {
    return {};
  },
};
</script>