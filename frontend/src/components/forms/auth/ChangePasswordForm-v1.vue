<template>
  <div>
  <ValidationObserver ref="obs1" v-slot="{ invalid }">

    <v-row justify="center" class="mt-12">
      <v-col cols="12" sm="8" md="4">

    <v-card class="elevation-12 pb-8">

      <!-- <v-toolbar color="primary" class='font-weight-medium' style='color:#D92231;'>
        <v-toolbar-title>Change Password</v-toolbar-title>
      </v-toolbar> -->
      <ToolbarHeader title='Change Password' class='font-weight-bold' color='dark' />

      <v-card-text>
        Please enter a new password below.

        <v-form @keyup.native.enter="onSubmit()">

          <ValidationProvider immediate name="username" rules="required" v-slot="{ errors, valid }">
            <v-text-field 
              disabled
              label="Email"
              v-model="username"
              :error-messages="errors"
              :success="valid"
              required 
              prepend-icon='mdi-email-multiple-outline' />
          </ValidationProvider>

          <ValidationProvider name="password" rules="required" v-slot="{ errors, valid }">
            <v-text-field
              label="New Password"
              v-model="password"
              :error-messages="errors"
              :success="valid"
              :type="show1 ? 'text' : 'password'"
              :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
              required
              @click:append="show1 = !show1"
              prepend-icon='mdi-lock' />
          </ValidationProvider>
          
          <ValidationProvider
            name="confirm"
            rules="confirmed:password"
            v-slot="{ errors, valid }">
            <v-text-field
              label="Confirm New Password"
              v-model="confirm"
              :error-messages="errors"
              :success="valid"
              :type="show2 ? 'text' : 'password'"
              :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
              @click:append="show2 = !show2"
              prepend-icon='mdi-lock' />
          </ValidationProvider>
          
          <v-btn
            small
            class="float-right font-weight-bold"
            @click="onSubmit()"
            color="primary"
            :disabled="invalid"
            style='color:#D92231;'>
            Submit
          </v-btn>

        </v-form>
      </v-card-text>
    </v-card>

    </v-col>
  </v-row>
  </ValidationObserver>
</div>
</template>
<script>
import { ValidationObserver, ValidationProvider } from "vee-validate";
import { mapActions } from "vuex";
import ToolbarHeader from '@/components/fragments/ToolbarHeader'

export default {
  components: { ToolbarHeader, ValidationProvider, ValidationObserver },
  props: ["currentUsername"],

  data() {
    return {
      username: this.currentUsername || "",
      password: "",
      confirm: "",
      show1: false,
      show2: false
    };
  },
  methods: {
    // VEE-VALIDATE IN MAIN..JS REQUIRED FOR THIS FORM....
    // ...mapActions({ login: "auth/AUTH_CHANGE_PASS" }),
    ...mapActions({ login: "authChangePassword" }),

    onSubmit() {
      if (this.password === "" || this.confirm === "") {
          this.$store.dispatch('infoSnackBar', { color: 'yellow', statusText: 'Please complete all fields', data: {info: ''}});

      } else if (this.password !== this.confirm){
        this.$store.dispatch('infoSnackBar', {color: 'yellow', statusText: 'Please ensure passwords match', data: {info: ''}});
      
      } else {
        this.login({ username: this.username, password: this.password });
    }
    },
  }
};
</script>
