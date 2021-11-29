<template>
    <ValidationProvider :name="$attrs.label" :rules="rules" v-slot="{ errors, valid }">
      <!-- <v-text-field
        v-model="innerValue"
        :error-messages="errors"
        :success="valid"
        v-bind="$attrs"
        v-on="$listeners"
        persistent-hint>
      </v-text-field> -->

      <v-file-input
      small-chips
      v-model="innerValue"
      :error-messages="errors"
      :success="valid"
      v-bind="$attrs"
      v-on="$listeners"
      persistent-hint>
  </v-file-input>

    </ValidationProvider>
  </template>
<script>
  import { ValidationProvider } from "vee-validate";
  export default {
    components: { ValidationProvider },
    
    props: {
      rules: {
        type: [Object, String],
        default: ""
      },
      // must be included in props
      value: {
        type: null
      }
    },
    data: () => ({
      innerValue: ""
    }),
    watch: {
      // Handles internal model changes.
      innerValue(newVal) {
        this.$emit("input", newVal);
      },
      // Handles external model changes.
      value(newVal) {
        this.innerValue = newVal;
      }
    },
    created() {
      try{
      if (this.value) {
        this.innerValue = this.value;
      }
    } catch(e) {
      console.log('VFile error: ', e)
    }
    }
  };
</script>