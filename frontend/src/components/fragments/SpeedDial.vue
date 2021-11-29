<template>
      <v-speed-dial
        v-model="fab"
        :top="top"
        :bottom="bottom"
        :right="right"
        :left="left"
        :direction="direction"
        :transition="transition">

        <template v-slot:activator>

          <v-btn v-model="fab" color="blue darken-2" fab>
            
            <v-icon v-if="fab">
              mdi-close
            </v-icon>
            
            <v-icon v-else>
              mdi-account-circle
            </v-icon>

          </v-btn>

        </template>

        <v-btn fab dark small color="green">
          <v-icon>mdi-pencil</v-icon>
        </v-btn>
        
        <v-btn fab dark small color="indigo">
          <v-icon>mdi-plus</v-icon>
        </v-btn>

        <!-- <v-btn fab dark small color="red"> -->
            <!-- <DialogForm/> -->
          <!-- <v-icon>mdi-delete</v-icon> -->
        <!-- </v-btn> -->

      </v-speed-dial>
    <!-- </v-card> -->
  </template>

  <script>
// import DialogForm from '@/components/fragments/DialogForm';
export default {
    components: {
      // DialogForm,
    },
      data: () => ({
        direction: 'top',//direction dial opens
        fab: false,
        fling: false,
        hover: false,
        tabs: null,
        top: false,
        right: true,
        bottom: true,
        left: false,
        transition: 'slide-y-reverse-transition',
      }),
  
      computed: {
        activeFab () {
          switch (this.tabs) {
            case 'one': return { class: 'purple', icon: 'account_circle' }
            case 'two': return { class: 'red', icon: 'edit' }
            case 'three': return { class: 'green', icon: 'keyboard_arrow_up' }
            default: return {}
          }
        },
      },
  
      watch: {
        top (val) {
          this.bottom = !val
        },
        right (val) {
          this.left = !val
        },
        bottom (val) {
          this.top = !val
        },
        left (val) {
          this.right = !val
        },
      },
    }
  </script>