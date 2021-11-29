<template>
  <div>
    <ChangePasswordForm :currentUsername='loggedInUser'/>
  </div>
</template>
<script>
import ChangePasswordForm from '@/components/forms/ChangePasswordForm'
import { mapGetters } from 'vuex';
export default {
  components: {
    ChangePasswordForm,
  },

  computed: {
    ...mapGetters({loggedInUser: 'getUsername'}),
  }
}
</script>
