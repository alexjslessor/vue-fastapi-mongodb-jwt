<template>
    <!-- <ValidationProvider :name="$attrs.label" :rules="rules" v-slot="{ errors, valid }">
      <v-text-field
        v-model="innerValue"
        :error-messages="errors"
        :success="valid"
        v-bind="$attrs"
        v-on="$listeners"
        persistent-hint>
      </v-text-field>
    </ValidationProvider> -->

    <!-- <v-list-item :to="{ path: `/user/info` }"> -->
      <!-- <v-list-item v-if='getUsername' :to="{ path: `account` }">
      <v-list-item-icon>
        <v-icon>mdi-account-settings-outline</v-icon>
      </v-list-item-icon>
        <v-list-item-content>
          Account
        </v-list-item-content>
    </v-list-item> -->

    <v-list-item v-bind='$attrs' v-on='$listeners'>
        <v-list-item-icon >
          <v-icon v-text='itemIcon'></v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          {{ itemText }}
        </v-list-item-content>
      </v-list-item>

  </template>
<script>
//   import { ValidationProvider } from "vee-validate";
  export default {
    components: { },
    
    props: {
      itemText: {
        type: [Object, String],
        default: ""
      },
      itemIcon: {
          type: String,
          default: ''
      },

      // must be included in props
    //   value: {
        // type: null
    //   }
    },

    // data: () => ({
    //   innerValue: ""
    // }),

    // watch: {
    //   // Handles internal model changes.
    //   innerValue(newVal) {
    //     this.$emit("input", newVal);
    //   },
    //   // Handles external model changes.
    //   value(newVal) {
    //     this.innerValue = newVal;
    //   }
    // },

    // created() {
    //   if (this.value) {
    //     this.innerValue = this.value;
    //   }
    // }

  };
</script>