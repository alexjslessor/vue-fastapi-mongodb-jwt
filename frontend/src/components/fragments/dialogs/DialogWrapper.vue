<template>

  <v-dialog v-model="innerValue">

    <template v-slot:activator="{ on, attrs }">
      <v-btn small color='primary' v-bind="attrs" v-on="on">
        {{ activatorBtnText }}
      </v-btn>
    </template>

    <v-layout row wrap>
      <v-flex xs12 sm12 md11 lg11 xl10 class='mx-auto'>

        <v-card>
          <v-card-text>

            <v-container fluid>
              <slot />
            </v-container>


            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn small color="primary" @click="innerValue = false">
                {{ btnText }}
              </v-btn>
            </v-card-actions>

          </v-card-text>

        </v-card>
      </v-flex>
    </v-layout>


  </v-dialog>
</template>
<script>
  export default {
    props: {

      activatorBtnText: {
        type: String,
        default: 'activatorBtnText',
        required: true
      },

      btnText: {
        type: String,
        default: 'Accept'
      },
      title: {
        type: String,
        default: 'Title Prop'
      },
      msg: {
        type: String,
        default: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id'
      },
      value: {
        type: null
      }
    },

    // data () {
    //   return {
    //     dialog: false,
    //   }
    // },
    data: () => ({
      innerValue: false
    }),

    watch: {
      // Handles internal model changes.
      innerValue(newVal) {
        this.$emit("dialog", newVal);
      },
      // Handles external model changes.
      value(newVal) {
        this.innerValue = newVal;
      }
    },

    created() {
      if (this.value) {
        this.innerValue = this.value;
      }
    }

  }
</script>