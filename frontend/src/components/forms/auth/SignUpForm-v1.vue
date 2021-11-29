<template>
  <div>
    <ValidationObserver ref="SignUpForm" v-slot="{ invalid }">
      <!-- <ValidationObserver ref='SignUpForm' v-slot="{ invalid, validated, handleSubmit }"> -->

      <v-container class="fill-height" fluid>
        <v-row>
          <div class="d-flex align-center">
            <!-- <img alt="login logo" src="../assets/4chan-pics/chanfash.png" height=100 width=110/> -->
          </div>
        </v-row>

        <v-row justify="center" class="mt-12">
          <v-col cols="12" sm="8" md="4">
            <v-card class="elevation-12 pb-8">
              <v-toolbar dense rounded color="secondary">
                <v-toolbar-title class="font-weight-bold">
                  <!-- {{ formTitle }} -->
                  Sign Up
                </v-toolbar-title>
                <v-spacer></v-spacer>
              </v-toolbar>

              <v-card-text>
                <v-form @submit.prevent="onSubmit">
                  <!-- <v-form> -->

                  <ValidationProvider
                    name="username"
                    v-slot="{ errors, valid }"
                  >
                    <v-text-field
                      label="Email"
                      v-model="username"
                      :error-messages="errors"
                      :success="valid"
                      prepend-inner-icon="mdi-email"
                    />
                  </ValidationProvider>

                  <ValidationProvider
                    name="password"
                    v-slot="{ errors, valid }"
                  >
                    <v-text-field
                      label="Password"
                      v-model="password"
                      :error-messages="errors"
                      :success="valid"
                      :type="show ? 'text' : 'password'"
                      :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                      clearable
                      @click:append="show = !show"
                      prepend-inner-icon="mdi-lock"
                    />
                  </ValidationProvider>

                  <ValidationProvider
                    name="confirm"
                    rules="confirmed:password"
                    v-slot="{ errors, valid }"
                  >
                    <v-text-field
                      label="Confirm Password"
                      v-model="confirm"
                      :error-messages="errors"
                      :success="valid"
                      :type="show2 ? 'text' : 'password'"
                      :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                      @click:append="show2 = !show2"
                      prepend-inner-icon="mdi-lock"
                    />
                  </ValidationProvider>

                  <router-link to="/login" style="cursor: pointer">
                    <span>Login</span>
                  </router-link>

                  <!-- <v-btn
                small
                class="float-right font-weight-bold"
                @click="onSubmit()"
                color="secondary"
                :disabled="!validated">
                {{ btnText }}
              </v-btn> -->

                  <v-btn
                    small
                    color="primary"
                    class="red--text font-weight-bold float-right"
                    @click="onSubmit"
                    :disabled="invalid"
                  >
                    {{ btnText }}
                  </v-btn>

                  <!-- <v-btn
                    small
                    class="float-right font-weight-bold"
                    @click="onSubmit"
                    color="secondary"
                    :disabled="invalid || !validated">{{ btnText }}</v-btn> -->
                </v-form>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </ValidationObserver>
  </div>
</template>
<script>
import axios from "axios";
import { ValidationObserver, ValidationProvider } from "vee-validate";
import { mapActions } from "vuex";
export default {
  components: { ValidationProvider, ValidationObserver },
  data() {
    return {
      formTitle: "Sign Up",
      btnText: "Submit",
      username: "",
      password: "",
      confirm: "",
      show: false,
      show2: false,
    };
  },
  methods: {
    ...mapActions({
      infoSnackBar: "auth/snackBar",
      registerUser: "auth/registerUser",
    }),

    onSubmit() {
      const creds = { username: this.username, password: this.password };
      // this.registerUser(creds)
    },
  },
};
</script>
<style lang="css" scoped>
.form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: auto;
}
.form-signin .checkbox {
  font-weight: 400;
}
.form-signin .form-control {
  position: relative;
  box-sizing: border-box;
  height: auto;
  padding: 10px;
  font-size: 16px;
}
.form-signin .form-control:focus {
  z-index: 2;
}
.form-signin input[type="text"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
</style>
    