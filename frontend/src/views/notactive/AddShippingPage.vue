<template>
<div>
  <v-row class='mx-auto' justify='center'>
    <v-col cols='12'>

      <v-card>
          <AddShipToForm/>
      </v-card>

  </v-col>
</v-row>

</div>
</template>
<script>
    import AddShipToForm from '@/components/forms/AddShipToForm';  
    export default {
      // name: "ShipToCustomerFormPage",
      components: {
        AddShipToForm
      },
    };
  
</script>