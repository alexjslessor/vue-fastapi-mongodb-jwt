<template>
<div>
  <v-container fluid class="mt-3 my-12">
    <!-- <v-container v-if='columnType == onecolumn' fluid class="mt-3 my-12"> -->
        <v-layout row wrap>
          <v-flex xs12 sm10 md9 lg8 xl8 class='mx-auto pt-3'>
            <slot />
          </v-flex>
        </v-layout>
    </v-container>

      <!-- <v-layout v-if='columnType == twocolumn' row wrap>
        <v-flex xs12 sm10 md9 lg8 xl8 class='mx-auto pt-3'>
          <slot />
        </v-flex>
      </v-layout> -->
</div>
</template>
<script>
export default {
    props: {
        layoutType: {
            type: String,
            required: false,
            default: 'onecolumn'
        },
    },

    data() {
      return {
        columnType: this.layoutType,
      }
    }


}
</script>