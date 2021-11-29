<template>
    <v-data-table :headers="headers" 
                  :items="desserts"
                  sort-by="name" 
                  class="elevation-1">

        <template v-slot:top>
            <v-toolbar flat>
                <v-toolbar-title class='font-weight-bold'>{{ tableTitle }}</v-toolbar-title>
                <v-divider class="mx-4" inset vertical></v-divider>
                <v-spacer></v-spacer>

                <v-dialog v-model="dialog" max-width="1024px" style='background-color: rgba(0, 0, 0, 0);'>
                    
                    <template v-slot:activator="{ on, attrs }">
                        <v-btn small 
                                color="secondary" 
                                class="mb-2 font-weight-bold" 
                                v-bind="attrs" v-on="on">
                            Add Customer
                        </v-btn>
                    </template>

                    <v-card>
                        <!-- <v-card-title><span class="headline">{{ formTitle }}</span></v-card-title> -->
                        <v-card-text>
                            <v-container>
                                <v-row>
                                    <ValidationObserver v-slot="{ handleSubmit }">

                                        <v-toolbar flat color="primary" style='color:#D92231;'>
                                          <v-toolbar-title>{{ formTitle }}</v-toolbar-title>
                                        </v-toolbar>

                                        <!-- <v-form @submit.prevent="handleSubmit(save)"> -->
                                        <v-form @submit.prevent="handleSubmit(onSubmit)">
                                          <v-container>

                                            <v-layout row wrap>  
                                              <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
                                                <ValidationProvider name="Contact Person" rules="required" v-slot="{ errors }">
                                                    <v-text-field solo dense clearable prepend-inner-icon='mdi-account' v-model="editedItem.name" label='Contact Person' type="text" :error-messages='errors'/>
                                                </ValidationProvider>
                                              </v-col>
                                    
                                              <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
                                                <ValidationProvider name="Company Name" rules="required" v-slot="{ errors }">
                                                    <v-text-field solo dense clearable prepend-inner-icon='mdi-domain' v-model="editedItem.company_name" label='Company Name' type="text" :error-messages='errors'/>
                                                </ValidationProvider>
                                              </v-col>
                                    
                                              <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
                                                <ValidationProvider name="Phone" rules="required" v-slot="{ errors }">
                                                    <v-text-field solo dense clearable prepend-inner-icon='mdi-cellphone-basic' v-model="editedItem.phone" label='Phone' type="text" :error-messages='errors'/>
                                                </ValidationProvider>
                                              </v-col>
                                    
                                              <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
                                                <ValidationProvider name="E-mail" rules="required|email" v-slot="{ errors }">
                                                  <v-text-field solo dense clearable prepend-inner-icon='mdi-at' v-model="editedItem.email" type="email" label='E-mail' :error-messages='errors'/>
                                                </ValidationProvider>
                                              </v-col>
                                          </v-layout>
                                    
                                            <!-- ROW 2 -->
                                            <v-layout row wrap>
                                    
                                              <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
                                                <ValidationProvider name="Tax I.D." rules="required" v-slot="{ errors }">
                                                    <v-text-field solo dense clearable prepend-inner-icon='mdi-identifier' v-model="editedItem.tax_shipping_code" label='Tax I.D.' type="text" :error-messages='errors'/>
                                                  </ValidationProvider>
                                              </v-col>
                                    
                                              <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
                                                <ValidationProvider name="Unit #" rules="required" v-slot="{ errors }">
                                                    <v-text-field solo dense clearable prepend-inner-icon='mdi-numeric' v-model="editedItem.unit_number"  label='Unit #' type="number" :error-messages='errors'/>
                                                  </ValidationProvider>
                                              </v-col>
                                    
                                              <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
                                                <ValidationProvider name="Street" rules="required" v-slot="{ errors }">
                                                    <v-text-field solo dense clearable prepend-inner-icon='mdi-road-variant' v-model="editedItem.street_name" label='Street' type="text" :error-messages='errors'/>
                                                  </ValidationProvider>
                                              </v-col>
                                    
                                              <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
                                                <ValidationProvider name="Street Type" rules="required" v-slot="{ errors }">
                                                    <v-text-field solo dense clearable prepend-inner-icon='mdi-road' v-model="editedItem.street_type" label='Street Type' type="text" :error-messages='errors'/>
                                                  </ValidationProvider>
                                              </v-col>
                                            </v-layout>
                                            
                                            <!-- ROW 3 -->
                                            <v-layout row wrap>
                                              <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
                                                <ValidationProvider name="City" rules="required" v-slot="{ errors }">
                                                    <v-text-field solo dense clearable prepend-inner-icon='mdi-city-variant-outline' v-model="editedItem.city_name" label='City' type="text" :error-messages='errors'/>
                                                  </ValidationProvider>
                                              </v-col>
                                    
                                              <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
                                                  <ValidationProvider name="State/Province" rules="required" v-slot="{ errors }">
                                                    <v-select solo
                                                              prepend-inner-icon="mdi-map"
                                                              :items="states_list" 
                                                              v-model="editedItem.state_province" 
                                                              item-text="state" 
                                                              item-value="abbr" 
                                                              label="State/Province" 
                                                              :error-messages="errors"                          
                                                              single-line></v-select>
                                                  </ValidationProvider>
                                              </v-col>
                                    
                                              <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
                                                <ValidationProvider name="Country" rules="required" v-slot="{ errors }">
                                                  <v-select solo 
                                                            prepend-inner-icon="mdi-google-maps" 
                                                            :items="country_list" 
                                                            v-model="editedItem.country" 
                                                            label="Country" 
                                                            :error-messages="errors"></v-select>
                                                </ValidationProvider>
                                            </v-col>
                                    
                                            <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
                                                <ValidationProvider name="Zip/Postal" rules="required" v-slot="{ errors }">
                                                  <v-text-field solo dense clearable prepend-inner-icon='mdi-postage-stamp' v-model="editedItem.zip_code" label='Zip/Postal' type="text" :error-messages='errors'/>
                                                </ValidationProvider>
                                            </v-col>
                                          </v-layout>

                                            <small>*indicates required field</small>
                                            <!-- <br/> -->
                                            <v-spacer></v-spacer>
                                              <!-- <v-btn type="submit" @click='save'>Submit</v-btn> -->
                                              <v-btn small color='green accent-4' type="submit">Submit</v-btn>
                                    
                                          </v-container>
                                        </v-form>
                                      </ValidationObserver>
 
                                </v-row>
                            </v-container>
                        </v-card-text>

                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn small 
                                    text
                                   color="secondary"
                                   class='font-weight-bold'
                                   @click="close">
                                Close
                            </v-btn>
                            <!-- <v-btn type='submit' 
                                   color="blue darken-1" 
                                   text 
                                   @click="save">
                                Save
                            </v-btn> -->
                        </v-card-actions>

                    </v-card>
                </v-dialog>
            </v-toolbar>
        </template>

        <template v-slot:item.actions="{ item }">
            <v-icon small class="mr-2" @click="editItem(item)" color='green'>
                mdi-pencil
            </v-icon>
            <v-icon small @click="deleteItem(item)" color='secondary'>
                mdi-delete
            </v-icon>
        </template>

        <template v-slot:no-data>
            <v-btn color="primary" 
                    class='font-weight-bold' @click="initialize">
                Reset
            </v-btn>
        </template>

    </v-data-table>
</template>
<script>
  import { ValidationObserver, ValidationProvider } from "vee-validate";
    export default {
        components: {ValidationProvider, ValidationObserver},
        data: () => ({
            tableTitle: 'Customer List',
            dialog: false,
            desserts: [],
            editedIndex: -1,

            headers: [
                { text: "Contact Name", value: 'name' },
                { text: "Company Name", value: 'company_name' },
                { text: "Country", value: 'country' },
                { text: "State/Province", value: 'state_province' },
                { text: "City", value: 'city_name' },
                { text: "Unit #", value: 'unit_number' },
                { text: "Street", value: 'street_name' },
                { text: "Street Type", value: 'street_type' },
                { text: "Phone #", value: 'phone' },
                { text: "Email", value: 'email' },
                { text: "Tax ID", value: 'tax_shipping_code' },
                { text: "Zip/Postal", value: 'zip_code' },
                { text: 'Actions', value: 'actions', sortable: false },
            ],
            editedItem: {
                name: '',
                company_name: '',
                country: '',
                state_province: '',
                city_name: '',

                unit_number: '',
                street_name: '',
                street_type: '',

                phone: '',
                email: '',
                tax_shipping_code: '',
                zip_code: ''
            },
            defaultItem: {
                name: '',
                company_name: '',
                country: '',
                state_province: '',
                city_name: '',
                
                unit_number: '',
                street_name: '',
                street_type: '',

                phone: '',
                email: '',
                tax_shipping_code: '',
                zip_code: ''
            },
            // defaultItem: {
            //     name: 'Tyler Durden',
            //     company_name: 'Pumpin',
            //     country: '',
            //     state_province: '',
            //     city_name: 'Gainz',
                
            //     unit_number: '44',
            //     street_name: 'This is the',
            //     street_type: 'Way',

            //     phone: '222-333-2233',
            //     email: 'btc@gmail.com',
            //     tax_shipping_code: 'AA33423DD',
            //     zip_code: 'M6A1X5'
            // },
            country_list: ['U.S.A.', 'CANADA'],
            states_list: [
                { abbr: 'AK', state: 'Alaska'},
                { abbr: 'AL', state: 'Alabama'},
                { abbr: 'AR', state: 'Arkansas'},
                { abbr: 'AS', state: 'American Samoa'},
                { abbr: 'AZ', state: 'Arizona'},
                { abbr: 'CA', state: 'California'},
                { abbr: 'CO', state: 'Colorado'},
                { abbr: 'CT', state: 'Connecticut'},
                { abbr: 'DC', state: 'District of Columbia'},
                { abbr: 'DE', state: 'Delaware'},
                { abbr: 'FL', state: 'Florida'},
                { abbr: 'GA', state: 'Georgia'},
                { abbr: 'GU', state: 'Guam'},
                { abbr: 'HI', state: 'Hawaii'},
                { abbr: 'IA', state: 'Iowa'},
                { abbr: 'ID', state: 'Idaho'},
                { abbr: 'IL', state: 'Illinois'},
                { abbr: 'IN', state: 'Indiana'},
                { abbr: 'KS', state: 'Kansas'},
                { abbr: 'KY', state: 'Kentucky'},
                { abbr: 'LA', state: 'Louisiana'},
                { abbr: 'MA', state: 'Massachusetts'},
                { abbr: 'MD', state: 'Maryland'},
                { abbr: 'ME', state: 'Maine'},
                { abbr: 'MI', state: 'Michigan'},
                { abbr: 'MN', state: 'Minnesota'},
                { abbr: 'MO', state: 'Missouri'},
                { abbr: 'MP', state: 'Northern Mariana Islands'},
                { abbr: 'MS', state: 'Mississippi'},
                { abbr: 'MT', state: 'Montana'},
                { abbr: 'NA', state: 'National'},
                { abbr: 'NC', state: 'North Carolina'},
                { abbr: 'ND', state: 'North Dakota'},
                { abbr: 'NE', state: 'Nebraska'},
                { abbr: 'NH', state: 'New Hampshire'},
                { abbr: 'NJ', state: 'New Jersey'},
                { abbr: 'NM', state: 'New Mexico'},
                { abbr: 'NV', state: 'Nevada'},
                { abbr: 'NY', state: 'New York'},
                { abbr: 'OH', state: 'Ohio'},
                { abbr: 'OK', state: 'Oklahoma'},
                { abbr: 'OR', state: 'Oregon'},
                { abbr: 'PA', state: 'Pennsylvania'},
                { abbr: 'PR', state: 'Puerto Rico'},
                { abbr: 'RI', state: 'Rhode Island'},
                { abbr: 'SC', state: 'South Carolina'},
                { abbr: 'SD', state: 'South Dakota'},
                { abbr: 'TN', state: 'Tennessee'},
                { abbr: 'TX', state: 'Texas'},
                { abbr: 'UT', state: 'Utah'},
                { abbr: 'VA', state: 'Virginia'},
                { abbr: 'VI', state: 'Virgin Islands'},
                { abbr: 'VT', state: 'Vermont'},
                { abbr: 'WA', state: 'Washington'},
                { abbr: 'WI', state: 'Wisconsin'},
                { abbr: 'WV', state: 'West Virginia',},
                { abbr: 'WY', state: 'Wyoming' },
                { abbr: 'ON', state: 'Ontario' },
                { abbr: 'AB', state: 'Alberta' },
                { abbr: 'BC', state: 'British Columbia'},
                { abbr: 'SK', state: 'Saskatchewan'},
                { abbr: 'MB', state: 'Manitoba' },
                { abbr: 'QC', state: 'Quebec' },
                { abbr: 'NL', state: 'Newfoundland Labrador' },
                { abbr: 'YT', state: 'Yukon' },
                { abbr: 'NU', state: 'Nunavut' },
                { abbr: 'NT', state: 'Northwest Territories'}
            ]
        }),
        computed: {
            formTitle() {
                return this.editedIndex === -1 ? 'New Address' : 'Edit Address'
            },
        },
        watch: {
            dialog(val) {
                val || this.close()
            },
        },
        created() {
            this.initialize()
        },
        methods: {
            async initialize() {
                this.desserts = await this.$store.dispatch('getShippingApi', {optional: 'all'})
            },

            editItem(item) {
                this.editedIndex = this.desserts.indexOf(item)
                this.editedItem = Object.assign({}, item)
                this.dialog = true
            },

            deleteItem(item) {
                const index = this.desserts.indexOf(item)
                confirm('Are you sure you want to delete this item?') && this.desserts.splice(index, 1)
            },
            close() {
                this.dialog = false
                this.$nextTick(() => {
                    this.editedItem = Object.assign({}, this.defaultItem)
                    this.editedIndex = -1
                })
            },

            // save() {
            //     if (this.editedIndex > -1) {
            //         Object.assign(this.desserts[this.editedIndex], this.editedItem)
            //     } else {
            //         this.desserts.push(this.editedItem)
            //         // this.onSubmit();
            //         this.$store.dispatch('post_ShipTo', this.editedItem)
            //     }
            //     // this.close()
            // },

            onSubmit() {
              // If item has index it is not new, and we update with update api endpoint.
              if (this.editedIndex > -1) {// check if entry has index 
                  Object.assign(this.desserts[this.editedIndex], this.editedItem)
                  try{// UPDATE ITEM
                  this.$store.dispatch('postUpdateFromJSON', {event: this.editedItem, 
                                                              collection: 'shipto'})
                  } catch(e) {
                    this.$store.dispatch('infoSnackBar', {statusText: 'Address Table Edit: Uh Oh, there was an error editing your address, please try again later', data: {info: `${e}` }});
                  }
              // If item does not have index it is new create new entry in endpoint.
              } else {
                this.desserts.push(this.editedItem)
                // CREATE NEW ITEM
                try {
                    this.$store.dispatch('postUpdateFromJSON', {event: this.editedItem, 
                                                                collection: 'new_shipto_from_crud_table'})
                } catch(e) {
                    this.$store.dispatch('infoSnackBar', {statusText: 'Address Table New: Uh Oh, there was an error saving your new address, please try again later', data: {info: `${e}` }});
                }
              }
              this.close()
            }

            // onSubmit() {
            //   if (this.editedIndex > -1) {
            //       Object.assign(this.desserts[this.editedIndex], this.editedItem)
            //   } else {
            //       this.desserts.push(this.editedItem)
            //       // this.onSubmit();
            //       if (this.updateItem) {
            //           this.$store.dispatch('updateCollectionDocument', this.editedItem, 'shipto')
            //           this.updateItem = false
            //       } else {
            //         this.$store.dispatch('post_ShipTo', this.editedItem)
            //       }
            //     }
            //   this.close()
            // }
            //   this.$store.dispatch('post_ShipTo', {
            //     name: this.name,
            //     company_name: this.company_name,
            //     email: this.email,
            //     phone: this.phone,
            //     tax_id: this.tax_id,
            //     unit_number: this.unit_number,
            //     street_name: this.street_name,
            //     street_type: this.street_type,
            //     city_name: this.city_name,
            //     state_province: this.state_province,
            //     country: this.country,
            //     zip_code: this.zip_code,
            //   })
        

        },
    }
</script>