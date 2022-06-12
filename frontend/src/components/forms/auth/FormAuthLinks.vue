<template>
 <!-- https://github.com/SelfhostedPro/Yacht/blob/master/frontend/src/views/Applications.vue -->
  <div class="">

        <router-link :to="{ name: 'Login' }" style="cursor: pointer">
        <!-- <router-link to="/login" style="cursor: pointer"> -->
          <span>Login</span>
        </router-link>
        
        <v-spacer></v-spacer>

        <router-link :to="{ name: 'SignUp' }" style="cursor: pointer">
        <!-- <router-link to="/signup" style="cursor: pointer"> -->
          <span>Sign Up</span>
        </router-link>
  </div>
</template>

<script>
export default {}
</script>

<style lang="css"></style>
