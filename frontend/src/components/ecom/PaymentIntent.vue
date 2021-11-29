<template>
  <!-- <div>
    <form id="payment-form">
      <div id="card-element"></div>
      <v-btn @click='submit()'>
        <div class="spinner hidden" id="spinner"></div>
        <span id="button-text">Pay now</span>
      </v-btn>
      <p id="card-error" role="alert"></p>
      <p class="result-message hidden">
        Payment succeeded, see the result in your
        <a href="" target="_blank">Stripe dashboard.</a> Refresh the page to pay again.
      </p>
    </form>
  </div> -->


  <div>
    <div id="card-element" class=""></div>
    <!-- <template v-if="getCart.length > 0"> -->
        <button class="button" @click="submit">Pay with Stripe</button>
    <!-- </template> -->
  </div>

</template>
<script>
  // https://stripe.com/docs/payments/integration-builder
  import { mapGetters, mapActions } from 'vuex';
  import axios from 'axios';

  export default {
    data() {
      return {
        testCard: '4242 4242 4242 4242',
        
        stripe: '',
        elements: '',
        card: '',

        cardStyle: {
          base: {
            color: "#32325d",
            fontFamily: 'Arial, sans-serif',
            fontSmoothing: "antialiased",
            fontSize: "16px",
            "::placeholder": {
              color: "#32325d"
            }
          },
          invalid: {
            fontFamily: 'Arial, sans-serif',
            color: "#fa755a",
            iconColor: "#fa755a"
          }
        },


      };
    },

    computed: {
      ...mapGetters( { 
                  getCart: 'stripe/getCart', 
                  getUsername: 'auth/GET_USERNAME'
                }),
    },

    methods: {

      payWithCard(stripe, card, clientSecret) {
        // loading(true);
        console.log('email receipt: ', this.getUsername)
        stripe.confirmCardPayment(clientSecret, {
          receipt_email: this.getUsername,
          payment_method: {
            card: card
          }
        }
        ).then(function(result) {
          if (result.error) {
            // Show error to your customer
            // showError(result.error.message);
            console.log('error', result.error.message);
          } else {
            // The payment succeeded!
            // orderComplete(result.paymentIntent.id);
            console.log('Payment Success: ', result.paymentIntent.id);
          }
        });
      },

      async submit() {
        const cart_items = { cart: this.getCart };
        await axios
          .post(`/cart-checkout`, { cart_items })
          .then(resp => {
            console.log('checkout ', resp)
            this.payWithCard(this.stripe, this.card, resp.data.clientSecret);
          })
    },

    // configureStripe() {
    //   // this.stripe = Stripe( this.stripeAPIToken );
    //   this.elements = stripe.elements();
    //   this.card = this.elements.create('card', { style: this.cardStyle } );
    //   this.card.mount('#card-element');
    // },
    configureStripe() {
        document.title = 'Checkout | ShadowStats'
        if (this.getCart.length > 0) {
            this.stripe = Stripe('pk_test_IO25CKyOll75V93WOyjViUyR00wcfxjKAf');
            // this.stripe = Stripe('pk_live_aeL64z4JQupPmUGuxf5Fr3i300qwPU0pca');

            this.elements = this.stripe.elements();
            this.card = this.elements.create('card', { hidePostalCode: true, style: this.cardStyle })
            this.card.mount('#card-element')
        }
    },
  },

  mounted() {
    this.configureStripe();
  }
};
</script>
<style scoped>
  * {
    box-sizing: border-box;
  }
  body {
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    font-size: 16px;
    -webkit-font-smoothing: antialiased;
    display: flex;
    justify-content: center;
    align-content: center;
    height: 100vh;
    width: 100vw;
  }
  form {
    width: 30vw;
    min-width: 500px;
    align-self: center;
    box-shadow: 0px 0px 0px 0.5px rgba(50, 50, 93, 0.1),
      0px 2px 5px 0px rgba(50, 50, 93, 0.1), 0px 1px 1.5px 0px rgba(0, 0, 0, 0.07);
    border-radius: 7px;
    padding: 40px;
  }
  input {
    border-radius: 6px;
    margin-bottom: 6px;
    padding: 12px;
    border: 1px solid rgba(50, 50, 93, 0.1);
    height: 44px;
    font-size: 16px;
    width: 100%;
    background: white;
  }
  .result-message {
    line-height: 22px;
    font-size: 16px;
  }
  .result-message a {
    color: rgb(89, 111, 214);
    font-weight: 600;
    text-decoration: none;
  }
  .hidden {
    display: none;
  }
  #card-error {
    color: rgb(105, 115, 134);
    text-align: left;
    font-size: 13px;
    line-height: 17px;
    margin-top: 12px;
  }
  #card-element {
    border-radius: 4px 4px 0 0;
    padding: 12px;
    border: 1px solid rgba(50, 50, 93, 0.1);
    height: 44px;
    width: 100%;
    background: white;
  }

  #payment-request-button {
    margin-bottom: 32px;
  }

  /* Buttons and links */
  button {
    background: #5469d4;
    color: #ffffff;
    font-family: Arial, sans-serif;
    border-radius: 0 0 4px 4px;
    border: 0;
    padding: 12px 16px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    display: block;
    transition: all 0.2s ease;
    box-shadow: 0px 4px 5.5px 0px rgba(0, 0, 0, 0.07);
    width: 100%;
  }

  button:hover {
    filter: contrast(115%);
  }

  button:disabled {
    opacity: 0.5;
    cursor: default;
  }

  /* v-btn__content:hover {
    filter: contrast(115%);
  }
  v-btn__content:disabled {
    opacity: 0.5;
    cursor: default;
  } */
  
  /* spinner/processing state, errors */
  .spinner,
  .spinner:before,
  .spinner:after {
    border-radius: 50%;
  }

  .spinner {
    color: #ffffff;
    font-size: 22px;
    text-indent: -99999px;
    margin: 0px auto;
    position: relative;
    width: 20px;
    height: 20px;
    box-shadow: inset 0 0 0 2px;
    -webkit-transform: translateZ(0);
    -ms-transform: translateZ(0);
    transform: translateZ(0);
  }

  .spinner:before,
  .spinner:after {
    position: absolute;
    content: "";
  }

  .spinner:before {
    width: 10.4px;
    height: 20.4px;
    background: #5469d4;
    border-radius: 20.4px 0 0 20.4px;
    top: -0.2px;
    left: -0.2px;
    -webkit-transform-origin: 10.4px 10.2px;
    transform-origin: 10.4px 10.2px;
    -webkit-animation: loading 2s infinite ease 1.5s;
    animation: loading 2s infinite ease 1.5s;
  }

  .spinner:after {
    width: 10.4px;
    height: 10.2px;
    background: #5469d4;
    border-radius: 0 10.2px 10.2px 0;
    top: -0.1px;
    left: 10.2px;
    -webkit-transform-origin: 0px 10.2px;
    transform-origin: 0px 10.2px;
    -webkit-animation: loading 2s infinite ease;
    animation: loading 2s infinite ease;
  }

  @-webkit-keyframes loading {
    0% {
      -webkit-transform: rotate(0deg);
      transform: rotate(0deg);
    }

    100% {
      -webkit-transform: rotate(360deg);
      transform: rotate(360deg);
    }
  }

  @keyframes loading {
    0% {
      -webkit-transform: rotate(0deg);
      transform: rotate(0deg);
    }

    100% {
      -webkit-transform: rotate(360deg);
      transform: rotate(360deg);
    }
  }

  @media only screen and (max-width: 600px) {
    form {
      width: 80vw;
    }
  }
</style>