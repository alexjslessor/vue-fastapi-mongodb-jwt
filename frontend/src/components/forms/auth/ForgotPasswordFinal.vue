<template>
  <div>
  <ValidationObserver ref="obs1" v-slot="{ invalid, validated }">

    <v-row justify="center" class="mt-12">
      <v-col cols="12" sm="8" md="4">

    <v-card class="elevation-12 pb-8">

      <ToolbarHeader 
      title='Create New Password' 
      class='font-weight-bold' 
      color='primary' />

      <v-card-text>
        
        {{ instructionText }}

        <!-- <v-form> -->
        <!-- <v-form @keyup.native.enter="onSubmit()"> -->
        <v-form @submit.prevent="onSubmit">

          <!-- <VTextFieldWithValidation 
          required
          immediate
          name='password'
          rules="required" 
          :type="show1 ? 'text' : 'password'" 
          :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'" 
          @click:append="show1 = !show1"
          label="Password" 
          v-model="password" 
          prepend-inner-icon='mdi-lock'/> -->
          <ValidationProvider
          name="password"
          rules='required'
          v-slot="{ errors, valid }">
          <v-text-field
            required
            label="Password"
            v-model="password"
            :error-messages="errors"
            :success="valid"
            :type="show1 ? 'text' : 'password'"
            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
            clearable
            @click:append="show1 = !show1"
            prepend-inner-icon='mdi-lock' />
        </ValidationProvider>



          <!-- <VTextFieldWithValidation 
          required
          immediate
          name='confirm'
          rules="required|confirmed:password" 
          :type="show2 ? 'text' : 'password'" 
          :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'" 
          @click:append="show2 = !show2"
          label="Confirm Password" 
          v-model="confirm" 
          prepend-inner-icon='mdi-lock'/> -->
          <ValidationProvider
          name="confirm"
          rules="required|confirmed:password"
          v-slot="{ errors, valid }">
          <v-text-field
            required
            label="Confirm Password"
            v-model="confirm"
            :error-messages="errors"
            :success="valid"
            :type="show2 ? 'text' : 'password'"
            :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="show2 = !show2"
            prepend-inner-icon='mdi-lock' />
        </ValidationProvider>


          <!-- <v-btn
            small
            class="float-right font-weight-bold"
            @click="onSubmit()"
            color="primary"
            :disabled="invalid"
            style='color:#D92231;'>
            Submit
          </v-btn> -->
          <v-btn small 
          type='submit'
          color="primary" 
          class='red--text font-weight-bold float-right' 
          :disabled="invalid">
          Submit
        </v-btn>

        </v-form>

        <!-- <v-btn small 
        @click='onSubmit()'
        
        color="primary" 
        class='red--text font-weight-bold float-right' 
        :disabled="validated || !validated">
        Submit
      </v-btn> -->
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
import VTextFieldWithValidation from '@/components/forms/inputs/VTextFieldWithValidation'
export default {
  components: { 
    ToolbarHeader, VTextFieldWithValidation, 
    ValidationProvider, ValidationObserver },

  props: ["query"],

  data() {
    return {
      password: "",
      confirm: "",
      show1: false,
      show2: false,
      instructionText: 'Please enter a new password below.',
      tok: '',
    };
  },
  methods: {
    ...mapActions({ 
      login: "auth/changePassword",
      snack: 'auth/snackBar',
      // finalizeForgotPassword: 'auth/finalizeForgotPassword',
      resetPassword: 'auth/resetPassword'
    }),

    onSubmit() {
      if (this.password === "" || this.confirm === "") {
        this.snack({ color: 'yellow', btnColor: 'white', statusText: `Please complete all fields`, data: {info: ''}});

      } else if (this.password !== this.confirm){
        this.snack({ color: 'yellow', btnColor: 'white', statusText: `Please ensure passwords match`, data: {info: ''}});
      
      } else {
        console.log('tok: ', this.tok)
        this.resetPassword({ token: this.query, password: this.password })
        // this.resetPassword({ token: this.tok, password: this.password })
    }
    },

    
  },

  // created() {
    // if(!this.query) {
      // this.$router.push('/login')
    // }
        // methods: mapActions(['finalizeLogin']),
    // // "http://localhost:8080/callback?code=AB11613499141vBzraIsUQTWp8VJAtAbwBju3k6XpH0dI0Gzdq&state=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdXRoZW50aWNhdGlvbl9iYWNrZW5kIjoiand0IiwiYXVkIjoiZmFzdGFwaS11c2VyczpvYXV0aC1zdGF0ZSIsImV4cCI6MTYxMzUwMjMyNH0.ZDrz-S9jVqJBPN45FthnD8hqzjFO_taNTMekb6ROfJQ&realmId=null"
    // created() {
      // console.log('window location About: ', window.location)
    //   this.finalizeLogin(window.location.search);
    // }
    // console.log('query: ', this.query)
    // this.tok = this.query
    // this.tok = await this.finalizeForgotPassword(window.location.search)
  // }


};
</script>
