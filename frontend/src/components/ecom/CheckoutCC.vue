<template>
    <div>
        <v-flex xs12 sm12 md12 lg12 xl10 class='mx-auto pt-3'>
            <v-card>
                <v-card-text>
                    <v-container>

                        <v-row justify='space-around' >

                            <v-col cols='12'>
                                <v-card>
                                    <ValidationObserver ref='productSuggestForm' v-slot="{ invalid, validated, handleSubmit }">
                                        <v-form>
                                            <div class='ml-4 mr-4 mt-4 mb-4'>

                                                <v-row justify='space-between'>

                                                    <v-col cols="8" xs='12' sm='12' md='6' lg='6' xl='6'>

                                                        <VTextFieldWithValidation dense rules="required" label="Name" hint='Name on package.' v-model="formData.name" />
                                                        <VTextFieldWithValidation dense rules="required" label="Address" hint='Delivery Address' v-model="formData.address" />

                                                        <VTextFieldWithValidation dense label="Postal/ZIP Code" hint='Postal/ZIP Code' v-model="formData.postal_zip" />
                                                        <VTextFieldWithValidation dense rules='required|email' label="Email"  v-model="formData.email" />
                                                    </v-col>

                                                    <!-- <v-col cols="8" xs='12' sm='12' md='6' lg='6' xl='4'>
                                                        <VTextFieldWithValidation dense label="Postal/ZIP Code" hint='Postal/ZIP Code' v-model="formData.postal_zip" />
                                                        <VTextFieldWithValidation dense rules='required|email' label="Email" hint='Email for delivery status updates.' v-model="formData.email" />
                                                    </v-col> -->

                                                    <v-col cols="8" xs='12' sm='12' md='6' lg='6' xl='6'>
                                                        <v-card>
                                                            <v-banner two-line>
                                                                <v-avatar slot="icon" color="deep-purple accent-4" size="40">
                                                                    <v-icon icon="mdi-cart" color="white"> mdi-cart</v-icon>
                                                                </v-avatar>
                                                                <div class='subtitle-1'>Thanks for your order!</div>
                                                                <div class='subtitle-2'>Total: {{ cartTotalPrice }}</div>
                                                            </v-banner>
                                                            <div id="card-element"></div>
                                                            <!-- <br/> -->
                                                            <v-btn class='checkout-btn mt-3' @click="submit">Checkout</v-btn>
                                                        </v-card>
                                                    </v-col>


                                                </v-row>
                                            </div>
                                        </v-form>
                                    </ValidationObserver>
                                </v-card>
                            </v-col>

                            <!-- <v-col cols='12'>
                                <v-card>
                                    <v-banner two-line>
                                        <v-avatar slot="icon" color="deep-purple accent-4" size="40">
                                            <v-icon icon="mdi-cart" color="white"> mdi-cart</v-icon>
                                        </v-avatar>
                                        <div class='subtitle-1'>Thanks for your order!</div>
                                        <div class='subtitle-2'>Total: {{ cartTotalPrice }}</div>
                                    </v-banner>
                                    <div id="card-element"></div>
                                    <v-btn class='checkout-btn' @click="submit">Checkout</v-btn>
                                </v-card>
                            </v-col> -->

                        </v-row>


                        <v-row>
                            <v-col cols='12'>
                                <v-card>

                                    <v-data-table hide-default-footer :headers="tableHeader" :items="tableData" class='elevation-10'>

                                        <template v-slot:top>
                                            <v-toolbar dense rounded>
                                                <!-- TABLE TITLE -->
                                                <v-toolbar-title class='font-weight-bold'>{{ tableTitle }}</v-toolbar-title>
                                                </v-divider>

                                                <v-spacer></v-spacer>

                                                <v-dialog v-model="dialog" max-width="500px">

                                                    <v-card>
                                                        <!-- DIALOG TITLE -->
                                                        <v-card-title>
                                                            <span class="headline mx-auto" v-text='editedItem.product'></span>
                                                        </v-card-title>

                                                        <v-card-text>
                                                            <v-container>

                                                                <v-col cols='12' class='mx-auto'>

                                                                    <v-col cols="12" xs='12' sm="12" md="12" lg='12' xl='12'>
                                                                        <v-text-field outlined clearable dense v-model.number="editedItem.quantity" hint='How many would you like to order' label="Qty." persistent-hint type='number' prepend-icon='mdi-counter'>
                                                                        </v-text-field>
                                                                    </v-col>
                                                                </v-col>

                                                            </v-container>
                                                        </v-card-text>

                                                        <v-card-actions>
                                                            <v-spacer></v-spacer>
                                                            <!-- CANCEL BTN -->
                                                            <v-btn text color="cancelBtn" @click="close">
                                                                Cancel
                                                            </v-btn>
                                                            <!-- SAVE BTN -->
                                                            <v-btn text color="saveBtn" @click="save">
                                                                Update
                                                            </v-btn>
                                                        </v-card-actions>

                                                    </v-card>
                                                </v-dialog>
                                            </v-toolbar>
                                        </template>

                                        <template v-slot:item.price="{ item }">
                                            ${{ item.price.toFixed(2) }}
                                        </template>

                                        <template v-slot:item.subtotal="{ item }">
                                            <v-btn small rounded elevation='2' color='primary' class='font-weight-bold' style='color: #D92231;'>
                                                ${{ item.subtotal.toFixed(2) }}
                                            </v-btn>
                                        </template>


                                        <!-- PENCIL ICON -->
                                        <template v-slot:item.actions="{ item }">
                                            <v-icon small class="mr-2" @click="editItem(item)" color='green'>mdi-pencil</v-icon>
                                            <v-icon small @click="deleteItem(item)" color='red'>mdi-delete</v-icon>
                                        </template>

                                    </v-data-table>

                                </v-card>
                            </v-col>
                        </v-row>

                    </v-container>
                </v-card-text>
            </v-card>
        </v-flex>

        <!-- <v-flex xs12 sm11 md12 lg12 xl2 class='mx-auto mt-4' > -->
        <!-- <v-layout row wrap>
            <v-flex xs12 sm12 md10 lg12 xl12 class='mx-auto pt-3 mt-3'>
                <v-container fluid>
                </v-container>
            </v-flex>
        </v-layout> -->
        <!-- </v-flex> -->

    </div>
</template>
<script>
    import { mapGetters, mapActions } from 'vuex';
    import axios from 'axios'
    import { ValidationObserver, ValidationProvider } from "vee-validate";
    import VTextFieldWithValidation from '@/components/forms/inputs/VTextFieldWithValidation'
    // import VTextAreaValidation from '@/components/forms/inputs/VTextAreaValidation'
    export default {
        components: {
            ValidationObserver, ValidationProvider, VTextFieldWithValidation
        },
        props: {
            tableTitle: {
                type: String,
                required: false
            },
            tableHeader: {
                type: Array,
                required: false
            },
            tableData: {
                type: Array,
                required: false
            },
        },

        data() {
            return {
                stripe: '',
                elements: '',
                card: '',
                date: new Date().toISOString().substr(0, 10),
                menu: false,
                dialog: false,
                formTitle: this.sku,
                editedIndex: -1,
                editedItem: {},
                defaultItem: {},
                formData: {},

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

            }
        },

        filters: {
            format_date(value) {
                return new Date(value).toISOString().substr(0, 10)
            },
        },

        computed: {
            ...mapGetters({
                getCartSize: 'stripe/getCartSize',
                getCart: 'stripe/getCart',
                getUsername: 'auth/GET_USERNAME',
                cartTotalPrice: 'stripe/cartTotalPrice',
            })
        },

        watch: {
            dialog(val) {
                val || this.close()
            },
        },

        methods: {

            payWithCard(stripe, card, clientSecret) {
                stripe.confirmCardPayment(clientSecret, {
                    payment_method: {
                        card: card
                    }
                })
                .then(function (result) {
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
            // submit() {
                // this.$store.dispatch('stripe/cartCheckout')
                const cart_items = { 
                    info: this.formData, 
                    cart: this.getCart 
                };

                await axios
                    .post(`/cart-checkout`, { cart_items })
                    .then(resp => {
                        console.log('checkout ', resp)
                        // this.payWithCard(this.stripe, this.card, resp.data.clientSecret);
                    })
            },

            editItem(item) {
                this.editedIndex = this.tableData.indexOf(item)
                this.editedItem = Object.assign({}, item)
                this.dialog = true
            },

            deleteItem(item) {
                let confirmDelete = confirm('Are you sure you want to delete this item?')
                if (confirmDelete) {
                    console.log('checkoutCC: ', item)
                    // this.$store.commit('stripe/RESET_PRODUCT_STATE', item);
                    // this.$store.dispatch('stripe/remove_product_from_cart', this.editedItem.productId);
                    this.$store.dispatch('stripe/remove_product_from_cart', item);
                }
            },


            close() {
                this.dialog = false
                this.$nextTick(() => {
                    this.editedItem = Object.assign({}, this.defaultItem)
                    this.editedIndex = -1
                })
            },


            save() {
                if (this.editedIndex > -1) {
                    try {
                        this.$store.commit('stripe/UPDATE_CART', this.editedItem);
                    } catch (e) {
                        this.$store.dispatch('auth/snackBar', {
                            color: 'red', btnColor: 'red',
                            statusText: 'Checkout Update Table: Uh Oh, please try again later',
                            data: { info: `${e}` }
                        });
                    }
                } else {
                    this.tableData.push(this.editedItem)
                }
                this.close()
            },

            configureStripe() {
                // document.title = 'Checkout | ShadowStats'
                if (this.getCart.length > 0) {
                    this.stripe = Stripe(this.$ECOM_AUTH);
                    // this.stripe = Stripe('pk_test_IO25CKyOll75V93WOyjViUyR00wcfxjKAf');
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

    }
</script>
<style scoped>
    /* * {
      box-sizing: border-box;
    } */
    /* body {
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
        font-size: 16px;
        -webkit-font-smoothing: antialiased;
        display: flex;
        justify-content: center;
        align-content: center;
        height: 100vh;
        width: 100vw;
    } */

    /* form {
        width: 30vw;
        min-width: 500px;
        align-self: center;
        box-shadow: 0px 0px 0px 0.5px rgba(50, 50, 93, 0.1),
            0px 2px 5px 0px rgba(50, 50, 93, 0.1), 0px 1px 1.5px 0px rgba(0, 0, 0, 0.07);
        border-radius: 7px;
        padding: 40px;
    } */

    /* input {
        border-radius: 6px;
        margin-bottom: 6px;
        padding: 12px;
        border: 1px solid rgba(50, 50, 93, 0.1);
        height: 44px;
        font-size: 16px;
        width: 100%;
        background: white;
    } */

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
    .checkout-btn {
        /* background: #5469d4; */
        color: #ffffff;
        font-family: Arial, sans-serif;
        /* border-radius: 0 0 4px 4px; */
        /* border: 0; */
        /* padding: 12px 16px; */
        /* font-size: 16px; */
        /* font-weight: 600; */
        cursor: pointer;
        /* display: block; */
        transition: all 0.2s ease;
        box-shadow: 0px 4px 5.5px 0px rgba(0, 0, 0, 0.07);
        width: 100%;
    }

    /* button:hover {
      filter: contrast(115%);
    } */

    /* button:disabled {
      opacity: 0.5;
      cursor: default;
    }
   */
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