<template>
<!-- <div> -->
    <v-container fluid class="mt-3 my-12">
      <!-- <p>{{ tableData }}</p> -->

        <CheckoutCC 
        tableTitle='Cart Items' 
        :tableHeader='tableHeader' 
        :tableData='getCart' />
         <!-- <CheckoutStepper /> -->

    </v-container>
  <!-- </div> -->
</template>
<script>
  import { mapGetters, mapActions } from 'vuex';
  // import CheckoutTable from '@/components/tables/CheckoutTable';
  import CheckoutCC from '@/components/ecom/CheckoutCC';
  import PaymentIntent from '@/components/ecom/PaymentIntent';
  import CheckoutStepper from '@/components/ecom/CheckoutStepper';

  export default {
    components: {
      CheckoutCC,
      PaymentIntent,
      CheckoutStepper
    },

    data: () => ({
      pageTitle: 'Checkout',
      cardTitleLeft: 'Thank you for your purchase!',
      cardTitleRight: 'You will not be invoiced until items are shipped.',
      shippingAddr: [],
      tableData: [],
      select: { _id: '', company_name: '' },
    }),

    computed: {
      ...mapGetters({getCart: 'stripe/getCart', 
                    cartTotalPrice: 'stripe/cartTotalPrice', 
                    getUsername: 'auth/GET_USERNAME',
                  }),

      tableHeader() {
        let items = [
          { text: "Name", value: 'name' },
          { text: "Description", value: 'description' },
          { text: "Price", value: 'price' },
          { text: 'Sub-Total', value: 'subtotal' },
          { text: "Qty Ordered", value: 'quantity' },
          { text: 'Update', value: 'actions', sortable: false },
        ];
        return items;
      },



    },

    // methods: {
      // ...mapActions(['getShippingApi', 'postCheckoutApi']),
    // },

    mounted() {
      document.title = 'Checkout | shadowstats.net'
      // Get items in cart and pass to component array
      // this.tableData = this.getCart;
    },

    // async created() {
      // Get shipping addresses for user
      // this.shippingAddr = await this.getShippingApi({optional: 'only'});
    // }

  };  
// A reference to Stripe.js initialized with your real test publishable API key.
// var stripe = Stripe("pk_test_IO25CKyOll75V93WOyjViUyR00wcfxjKAf");
// // The items the customer wants to buy
// var purchase = {
//   items: [{ id: "xl-tshirt" }]
// };

// Disable the button until we have Stripe set up on the page
// document.querySelector("button").disabled = true;
// fetch("/create-payment-intent", {
//   method: "POST",
//   headers: {
//     "Content-Type": "application/json"
//   },
//   body: JSON.stringify(purchase)
// })
//   .then(function(result) {
//     return result.json();
//   })
//   .then(function(data) {
//     var elements = stripe.elements();

//     var style = {
//       base: {
//         color: "#32325d",
//         fontFamily: 'Arial, sans-serif',
//         fontSmoothing: "antialiased",
//         fontSize: "16px",
//         "::placeholder": {
//           color: "#32325d"
//         }
//       },
//       invalid: {
//         fontFamily: 'Arial, sans-serif',
//         color: "#fa755a",
//         iconColor: "#fa755a"
//       }
//     };

  //   var card = elements.create("card", { style: style });
  //   // Stripe injects an iframe into the DOM
  //   card.mount("#card-element");

  //   card.on("change", function (event) {
  //     // Disable the Pay button if there are no card details in the Element
  //     document.querySelector("button").disabled = event.empty;
  //     document.querySelector("#card-error").textContent = event.error ? event.error.message : "";
  //   });

  //   var form = document.getElementById("payment-form");
  //   form.addEventListener("submit", function(event) {
  //     event.preventDefault();
  //     // Complete payment when the submit button is clicked
  //     payWithCard(stripe, card, data.clientSecret);
  //   });
  // });

// Calls stripe.confirmCardPayment
// If the card requires authentication Stripe shows a pop-up modal to
// prompt the user to enter authentication details without leaving your page.
// var payWithCard = function(stripe, card, clientSecret) {
//   loading(true);
//   stripe
//     .confirmCardPayment(clientSecret, {
//       payment_method: {
//         card: card
//       }
//     })
//     .then(function(result) {
//       if (result.error) {
//         // Show error to your customer
//         showError(result.error.message);
//       } else {
//         // The payment succeeded!
//         orderComplete(result.paymentIntent.id);
//       }
//     });
// };


</script>