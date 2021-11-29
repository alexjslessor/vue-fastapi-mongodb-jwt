<template>
    <div>
      <v-container fluid>
        <v-row>
          <CheckoutShipment/>
        </v-row>
      </v-container>
    </div>
  </template>
  
<script>
import CheckoutShipment from '@/components/CheckoutShipment';
export default {
  name: "ShipPage",
  components: {CheckoutShipment},
};  
</script>
    