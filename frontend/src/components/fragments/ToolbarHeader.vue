<template>
    <v-toolbar dense rounded v-bind='$attrs' v-on='$listeners' :color="$attrs.color">
        <v-toolbar-title :class='$attrs.class'>{{ title }}</v-toolbar-title>
        <!-- <v-spacer></v-spacer> -->
        <slot />

   </v-toolbar>
</template>

<script>
    export default {
      components: {},
      props: {
        title: {
          type: String,
          default: "toolbar title"
        },
      },
    //   data: () => ({
        // innerValue: ""
    //   }),
    //   watch: {
    //     // Handles internal model changes.
    //     innerValue(newVal) {
    //       this.$emit("input", newVal);
    //     },
    //     // Handles external model changes.
    //     value(newVal) {
    //       this.innerValue = newVal;
    //     }
    //   },
    //   created() {
    //     if (this.value) {
    //       this.innerValue = this.value;
    //     }
    //   }
    };
    </script>
    