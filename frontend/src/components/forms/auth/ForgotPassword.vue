<template>
  <div>
    <ValidationObserver ref="forgotPassword" v-slot="{ handleSubmit, invalid }">

    <v-row justify="center" class="mt-12">
      <v-col cols="12" sm="8" md="4">

    <v-card class="elevation-12 pb-8">

      <ToolbarHeader title='Forgot Password' class='font-weight-bold' color='primary' />

      <v-card-text>
        {{ instructionText }}
          <v-form>

          <VTextFieldWithValidation 
            required
            immediate 
            rules="required|email" 
            label="Email" 
            hint='Email / User Name' 
            v-model="email" 
            prepend-icon='mdi-email-multiple-outline'
            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'" 
          />

          <!-- <v-btn small
            class="float-right font-weight-bold"
            @click="onSubmit()"
            color="primary"
            :disabled="invalid"
            style='color:#D92231;'>
            Submit
          </v-btn> -->

        </v-form>

        <!-- <v-btn small color="primary" class='float-right font-weight-bold' :disabled="invalid" @click.native.enter="handleSubmit(onSubmit)">Submit</v-btn> -->
        <v-btn small color="primary" class='float-right font-weight-bold' :disabled="invalid" @click="handleSubmit(onSubmit)">Submit</v-btn>


        <form-auth-links/>

      </v-card-text>

      
    </v-card>

    </v-col>
  </v-row>
  </ValidationObserver>
</div>
</template>
<script>
import { mapActions } from "vuex";
import ToolbarHeader from '@/components/fragments/ToolbarHeader';
import FormAuthLinks from '@/components/forms/auth/FormAuthLinks';
import { ValidationObserver, ValidationProvider } from "vee-validate";
import VTextFieldWithValidation from '@/components/forms/inputs/VTextFieldWithValidation';
export default {
  components: { 
    ToolbarHeader, 
    VTextFieldWithValidation, 
    ValidationProvider, 
    ValidationObserver,
    FormAuthLinks,
  },
  data() {
    return {
      email: '',
      show1: false,
      instructionText: 'If an account with this email exists, reset password instructions will be sent.',
    };
  },
  methods: {
    // VEE-VALIDATE IN MAIN..JS REQUIRED FOR THIS FORM....
    // ...mapActions({ login: "auth/AUTH_CHANGE_PASS" }),
    ...mapActions({ 
      forgotPassword: "auth/forgotPassword",
      snack: 'auth/snackBar' 
    }),

    onSubmit() {
      console.log('forgot password email: ', this.email);
      this.forgotPassword( { email: this.email } );
      this.snack({color: 'green', btnColor: 'yellow', statusText: `Thanks, please check your email!`, data: {info: ''}});
    },

  }
};
</script>
