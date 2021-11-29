<template>
  <div class='mx-auto'>
    <v-card>
      <!-- <v-sheet elevation='6'> -->
    <v-tabs center-active 
            next-icon="mdi-arrow-right-bold-box-outline"
            prev-icon="mdi-arrow-left-bold-box-outline"
            show-arrows
            mobile-breakpoint="sm">
      
      <v-tab class="text-left">
        <slot name='one'>
        </slot >
      </v-tab>

      <v-tab class="text-left">
        <slot name='two'>
        </slot>
      </v-tab>
      
      <v-tab class="text-left">
        <slot name='three'>
        </slot>
      </v-tab>

    </v-tabs>
    <!-- <v-tabs mobile-breakpoint="sm">
      <v-tab class="text-left" :to="{ path: 'info' }">
        <v-icon left class="mr-1">mdi-information-outline</v-icon>Info
      </v-tab>
      <v-tab class="text-left" :to="{ path: 'changePassword' }">
        <v-icon left class="mr-1">mdi-lock-outline</v-icon>Change Password
      </v-tab>
    </v-tabs> -->

    <!-- </v-sheet> -->
  </v-card>

  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
};
</script>

<style>
.floating-menu {
  z-index: 1;
}
</style>
