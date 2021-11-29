<template>
  <div>
    <ValidationObserver ref="obs1" v-slot="{ invalid, validated }">
      <v-container class="fill-height" fluid>
        <v-row>
          <div class="d-flex align-center">
            <!-- <img alt="login logo" src="../assets/4chan-pics/chanfash.png" height=100 width=110/> -->
          </div>
        </v-row>

        <v-row justify="center" class="mt-12">
          <v-col cols="12" sm="8" md="4">
            <v-card class="elevation-12 pb-8">
              <ToolbarHeader
                title="Login"
                class="font-weight-bold"
                color="dark"
              />

              <v-card-text>
                <v-form @keyup.native.enter="onSubmit()">
                  <ValidationProvider
                    rules="required|email"
                    name="username"
                    v-slot="{ errors, valid }"
                  >
                    <v-text-field
                      required
                      label="Email"
                      v-model="username"
                      :error-messages="errors"
                      :success="valid"
                      prepend-icon="mdi-email-multiple-outline"
                    />
                  </ValidationProvider>

                  <ValidationProvider
                    rules="required"
                    name="password"
                    v-slot="{ errors, valid }"
                  >
                    <v-text-field
                      required
                      label="Password"
                      v-model="password"
                      :error-messages="errors"
                      :success="valid"
                      :type="show ? 'text' : 'password'"
                      :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                      clearable
                      @click:append="show = !show"
                      prepend-icon="mdi-lock"
                    />
                  </ValidationProvider>
                  <v-btn
                    small
                    class="float-right font-weight-medium"
                    @click="onSubmit()"
                    color="primary"
                    style="color: #d92231"
                    :disabled="invalid || !validated"
                  >
                    Submit
                  </v-btn>
                </v-form>

                <router-link :to="{ name: 'SignUp' }" style="cursor: pointer">
                  <span>Sign Up!</span>
                </router-link>
                <v-spacer></v-spacer>
                <v-spacer></v-spacer>
                <router-link :to="{ name: 'ForgotPassword' }" style="cursor: pointer">
                  <span>I Forgot My Password...</span>
                </router-link>

              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </ValidationObserver>

    <LoadingOverlay />
  </div>
</template>
  <script>
import { ValidationObserver, ValidationProvider } from "vee-validate";
import { mapActions } from "vuex";
import ToolbarHeader from "@/components/fragments/ToolbarHeader";
import LoadingOverlay from "@/components/fragments/LoadingOverlay";
export default {
  components: {
    ValidationProvider,
    ValidationObserver,
    ToolbarHeader,
    LoadingOverlay,
  },

  data() {
    return {
      username: "",
      password: "",
      show: false,
      overlay: false,
    };
  },

  methods: {
    ...mapActions({ login: "auth/LOGIN_ACTION" }),

    onSubmit() {
      const creds = { username: this.username, password: this.password };
      this.login(creds);
      // this.$store.dispatch('LOGIN_ACTION', creds)
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
    