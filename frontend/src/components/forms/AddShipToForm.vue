<template>

  <ValidationObserver v-slot="{ handleSubmit }">

    <v-toolbar flat color="primary" style='color:#D92231;'>
      <v-toolbar-title>{{ formTitle }}</v-toolbar-title>
    </v-toolbar>

    <v-form @submit.prevent="handleSubmit(onSubmit)">
      <v-container>

        <v-layout row wrap>
          <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
            <ValidationProvider name="Contact Person" rules="required|alpha" v-slot="{ errors }">
                <v-text-field v-model="name" label='Contact Person' type="text" :error-messages='errors'/>
            </ValidationProvider>
          </v-col>

          <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
            <ValidationProvider name="Company Name" rules="required|alpha" v-slot="{ errors }">
                <v-text-field v-model="company_name" label='Company Name' type="text" :error-messages='errors'/>
            </ValidationProvider>
          </v-col>

          <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
            <ValidationProvider name="Phone" rules="required" v-slot="{ errors }">
                <v-text-field v-model="phone" label='Phone' type="text" :error-messages='errors'/>
            </ValidationProvider>
          </v-col>

          <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
            <ValidationProvider name="E-mail" rules="required|email" v-slot="{ errors }">
              <v-text-field v-model="email" type="email" label='E-mail' :error-messages='errors'/>
            </ValidationProvider>
          </v-col>

      </v-layout >

        <!-- ROW 2 -->
        <v-layout row wrap>

          <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
            <ValidationProvider name="Tax I.D." rules="required" v-slot="{ errors }">
                <v-text-field v-model="tax_id" label='Tax I.D.' type="text" :error-messages='errors'/>
              </ValidationProvider>
          </v-col>

          <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
            <ValidationProvider name="Unit #" rules="required" v-slot="{ errors }">
                <v-text-field v-model="unit_number"  label='Unit #' type="number" :error-messages='errors'/>
              </ValidationProvider>
          </v-col>

          <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
            <ValidationProvider name="Street" rules="required|alpha" v-slot="{ errors }">
                <v-text-field v-model="street_name" label='Street' type="text" :error-messages='errors'/>
              </ValidationProvider>
          </v-col>

          <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
            <ValidationProvider name="Street Type" rules="required|alpha" v-slot="{ errors }">
                <v-text-field v-model="street_type" label='Street Type' type="text" :error-messages='errors'/>
              </ValidationProvider>
          </v-col>
        </v-layout>

        <v-layout row wrap>
          <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
            <ValidationProvider name="City" rules="required|alpha" v-slot="{ errors }">
                <v-text-field v-model="city_name" label='City' type="text" :error-messages='errors'/>
              </ValidationProvider>
          </v-col>

          <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
            <!-- <ValidationProvider name="State/Province" rules="required|alpha" v-slot="{ errors }"> -->
                <!-- <v-text-field v-model="state_province" label='State/Province' type="text" :error-messages='errors'/> -->
              <!-- </ValidationProvider> -->
              <ValidationProvider name="State/Province" rules="required" v-slot="{ errors }">
                <v-select solo
                          prepend-icon="mdi-map"
                          :items="states_list" 
                          v-model="state_province" 
                          item-text="state" 
                          item-value="abbr" 
                          :hint="`${state_province.state}, ${state_province.abbr}`" 
                          label="State/Province" 
                          :error-messages="errors"                          
                          single-line></v-select>
              </ValidationProvider>
          </v-col>

          <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
            <!-- <ValidationProvider name="country" rules="required|alpha" v-slot="{ errors }">
              <v-text-field v-model="country" type="text" label='Country' :error-messages='errors'/>
            </ValidationProvider> -->
            <ValidationProvider name="Country" rules="required" v-slot="{ errors }">
              <v-select solo 
                        prepend-icon="mdi-google-maps" 
                        :items="country_list" 
                        v-model="country" 
                        label="Country" 
                        :error-messages="errors"></v-select>
            </ValidationProvider>
        </v-col>

        <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
            <ValidationProvider name="Zip/Postal" rules="required|alpha" v-slot="{ errors }">
              <v-text-field v-model="zip_code" label='Zip/Postal' type="text" :error-messages='errors'/>
            </ValidationProvider>
        </v-col>
      </v-layout>

          <v-btn type="submit">Submit</v-btn>


      </v-container>
    </v-form>
  </ValidationObserver>

</template>

<script>
  import { ValidationObserver, ValidationProvider } from "vee-validate";
  export default {
    components: {ValidationProvider, ValidationObserver},
    data() {
      return {
        formTitle: 'Add Customer Shipping',
        name: '',
        company_name: '',
        email: '',
        phone: '',
        
        unit_number: '',
        street_name: '',
        street_type: '',
        city_name: '',

        state_province: {state: '', abbr: ''},
        country: '',
        zip_code: '',
        tax_id: '',

        country_list: ['U.S.A.', 'CANADA'],
        nameRules: 'required',
        emailRules: 'required',
        phoneRules: 'required',
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
      }
    },


    methods: {
      onSubmit() {
        this.$store.dispatch('post_ShipTo', {
          name: this.name,
          company_name: this.company_name,
          email: this.email,
          phone: this.phone,
          tax_id: this.tax_id,
          unit_number: this.unit_number,
          street_name: this.street_name,
          street_type: this.street_type,
          city_name: this.city_name,
          state_province: this.state_province,
          country: this.country,
          zip_code: this.zip_code,
        })
      }
    }

  }
</script>
