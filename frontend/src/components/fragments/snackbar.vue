<template>
  <v-snackbar
    outlined
    :value="visible"
    @input="clearSnack()"
    :color="color"
    :bottom="bottom"
    >
    {{ content }}
    <template v-slot:action="{ attrs }">
      <v-btn
        text
        dark
        v-bind="attrs"
        :color="btnColor"
        timeout="-1"
        @click="clearSnack()">
        Close
      </v-btn>
    </template>
  </v-snackbar>
</template>

<script>
import { mapState, mapMutations } from "vuex";
export default {
  data() {
    return {};
  },

  computed: {
    ...mapState('auth', [
      "content",
      "bottom",
      "color",
      "visible",
      "btnColor"
    ])
  },
  
  methods: {
    ...mapMutations({
      clearSnack: 'auth/CLEAR_SNACKBAR'
    })
  }
  // computed: {
  //   ...mapState("snackbar", [
  //     "content",
  //     "bottom",
  //     "color",
  //     "visible",
  //     "btnColor"
  //   ])
  // },

  // methods: {
  //   ...mapMutations({
  //     clearSnack: "snackbar/clearSnack"
  //   })
  // }


};
</script>
