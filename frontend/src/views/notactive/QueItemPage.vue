<template>
    <div>
      <!-- <p>{{ tableData }}</p> -->
      <v-container fluid class="mt-3 my-12">
        
        <v-layout row wrap>
          <v-flex xs12 sm6 md7 lg8 xl8 class='mx-auto pt-3'>
            <!-- <MOrderItemTable :sku='sku' 
                              tableTitle='Que Table' 
                              :tableHeader='tableHeader' 
                              :tableData='tableData'
                              :dropdownArray='getStatusChanges'/> -->
          </v-flex>
        </v-layout>
    </v-container>

  </div>
</template>
<script>
import { mapGetters, mapActions } from 'vuex';
import MOrderItemTable from '@/components/tables/MOrderItemTable';
export default {
  // name: "QueItemPage",
  props: ['sku'],
  components: {
    MOrderItemTable,
  },
  data() {
      return {
        pageTitle: this.sku,
        tableData: [],
      }
    },
    methods: {
      // ...mapActions(['postDashboardQueItemApi']),
    },
    computed: {
      ...mapGetters('auth', ['getUserType']),

    tableHeader() {
    // Que table on both admin/user tables but different statuses
    // Different item list not necessary atm but will leave incase needed in future?
      let items = [
        { text: "Date Submitted", value: 'date_submitted.$date', sortable: false },
        { text: "Shipping Date", value: 'fulfillment_date.$date', sortable: false },
        { text: "Status", value: 'status' },
        { text: "Qty Ordered", value: 'quantity' },
        { text: "Qty In Production", value: 'quantity_fulfilled_count' },
        { text: 'Update Status', value: 'actions', sortable: false },
      ];
      if (this.getUserType) {
        // User Que table with update button
        items = [
          { text: "Date Submitted", value: 'date_submitted.$date' },
          { text: "Shipping Date", value: 'fulfillment_date.$date' },
          { text: "Status", value: 'status' },
          { text: "Qty Ordered", value: 'quantity' },
          { text: "Qty In Production", value: 'quantity_fulfilled_count' },
          { text: 'Update Status/Qty', value: 'actions', sortable: false },
        ];
      }
      return items;
    },

  },

  async created() {
    this.tableData = await this.postDashboardQueItemApi({event: this.sku});
  }
    
};
</script>
