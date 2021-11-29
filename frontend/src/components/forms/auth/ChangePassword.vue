<template>
  <div>
  <ValidationObserver ref="changePasswordForm" v-slot="{ invalid, validated }">

    <v-row justify="center" class="mt-12">
      <v-col cols="12" sm="8" md="4">

    <v-card class="elevation-12 pb-8">

      <ToolbarHeader title='Change Password' class='font-weight-bold' color='primary' />

      <v-card-text>
        
        {{ instructionText }}

        <!-- <v-form @keyup.native="onSubmit()"> -->
          <v-form>
          <!-- <VTextFieldWithValidation immediate rules="required" label="Username" hint='Username' v-model="username" prepend-icon='mdi-email-multiple-outline'/> -->
          <ValidationProvider immediate name="username" rules="required|email" v-slot="{ errors, valid }">
            <v-text-field 
              required 
              disabled
              label="Email"
              v-model="username"
              :error-messages="errors"
              :success="valid"
              prepend-icon='mdi-email-multiple-outline' />
          </ValidationProvider>

          <!-- <VTextFieldWithValidation 
          rules="required" 
          :type="show1 ? 'text' : 'password'" 
          :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'" 
          @click:append="show1 = !show1"
          label="password" 
          v-model="password" 
          prepend-icon='mdi-lock'/> -->
          <ValidationProvider name="password" rules="required" v-slot="{ errors, valid }">
            <v-text-field
              required
              label="New Password"
              v-model="password"
              :error-messages="errors"
              :success="valid"
              :type="show1 ? 'text' : 'password'"
              :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
              @click:append="show1 = !show1"
              prepend-icon='mdi-lock' />
          </ValidationProvider>



          <!-- <VTextFieldWithValidation 
          rules="confirmed:password" 
          :type="show2 ? 'text' : 'password'" 
          :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'" 
          @click:append="show2 = !show2"
          label="confirm" 
          v-model="confirm" 
          prepend-icon='mdi-lock'/> -->
          <ValidationProvider name="confirm" rules="required|confirmed:password" v-slot="{ errors, valid }">
            <v-text-field
              required
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
// import VSelectWithValidation from '@/components/forms/inputs/VSelectWithValidation'
import VTextFieldWithValidation from '@/components/forms/inputs/VTextFieldWithValidation'
export default {
  components: { ToolbarHeader, VTextFieldWithValidation, ValidationProvider, ValidationObserver },

  props: ["currentUsername"],

  data() {
    return {
      username: this.currentUsername || "",
      password: "",
      confirm: "",
      show1: false,
      show2: false,
      instructionText: 'Please enter a new password below.',
    };
  },
  methods: {
    // VEE-VALIDATE IN MAIN..JS REQUIRED FOR THIS FORM....
    // ...mapActions({ login: "auth/AUTH_CHANGE_PASS" }),
    ...mapActions({ 
      changePassword: "auth/changePassword",
      snack: 'auth/snackBar',
      finalizeForgotPassword: 'auth/finalizeForgotPassword',
    }),

    onSubmit() {
        this.changePassword({ username: this.username, 
                              password: this.password });
    },

    
  },


};
</script>
