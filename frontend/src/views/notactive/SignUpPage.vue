<template>
  <div>
    <p>Sign Up Page</p>
    <!-- <SignUpForm/> -->
    <ChangePasswordForm currentUsername='alexjslessor@gmail.com'/>
  </div>
</template>

<script>
// import SignUpForm from '@/components/forms/SignUpForm.vue'
import ChangePasswordForm from '@/components/forms/ChangePasswordForm'
export default {
  name: 'SignUpPage',
  components: {
    // SignUpForm,
    ChangePasswordForm,
  },
}
</script>
