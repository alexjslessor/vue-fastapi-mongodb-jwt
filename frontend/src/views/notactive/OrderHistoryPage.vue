<template>

  <twoColumnWrapper>
    <DropdownTable :tableTitle='tableTitle' 
                   :tableHeader='shippedTableHeader'
                   :tableData='tableHistoryData'
                   :dropTableHeader='dropTableHeader'
                   :dropdownArray='getDocumentList'
                   allowStatusChanges='yes'
                   :statusChanges='status_changes'/>
  </twoColumnWrapper>

</template>
<script>
// import pageTitle from '@/components/fragments/pageTitle';
import DropdownTable from '@/components/tables/DropdownTable';
import twoColumnWrapper from '@/components/fragments/twoColumnWrapper';
import { mapGetters, mapActions } from 'vuex';
export default {
  components: {
    // pageTitle,
    DropdownTable,
    twoColumnWrapper,
  },

  data() {
    return {
      pageTitle: 'Completed Orders',
      tableTitle: 'Completed',
      tableHistoryData: [],
      status_changes: ['Shipped', 'Complete'],
    }
  },

  computed: {
    ...mapGetters(['getUserType', 'getDocumentList']),

    shippedTableHeader() {
      let items = [
        { text: '', value: 'data-table-expand', align:'end' },
        { text: 'Invoice', value: '_id.invoice_num', groupable: false },
        // { text: 'Status', value: 'status', groupable: false },
        { text: 'Status', value: '_id.status', groupable: false },
        { text: "# of SKU's", value: 'count', groupable: false },
        { text: "Total Qty.", value: 'totalItems', groupable: false },
        { text: "Total $(USD)", value: 'totalAmount', groupable: false },
        { text: 'Action', value: 'actions', sortable: false, groupable: false },
      ];
      return items;
    },

    dropTableHeader() {
      let items = [
        { text: 'SKU', value: 'order_sku' },
        { text: 'Price', value: 'order_price' },
        { text: 'Qty.', value: 'quantity' },
        { text: 'Description', value: 'order_description' },
      ];
      return items;
    },

  },

  methods: {
    ...mapActions(['get_Closed_Orders']),
  },

  async created() {
    this.tableHistoryData = await this.get_Closed_Orders('cancelled_complete');
  },

}
</script>