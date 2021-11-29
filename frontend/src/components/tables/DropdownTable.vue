<template>
  <div>
    <v-data-table show-expand :headers="tableHeader" :items="tableData" item-key='_id.invoice_num' :single-expand="singleExpand" class="elevation-1">
      <template v-slot:top>
        <v-toolbar flat>
          <!-- TABLE TITLE -->
          <v-toolbar-title class='font-weight-bold'>{{ table_title }}</v-toolbar-title>
          <v-divider class="mx-4" inset vertical>
          </v-divider>

          <v-spacer></v-spacer>

          <v-dialog v-model="dialog" max-width="500px">
            <v-card>
              <!-- DIALOG TITLE -->
              <v-card-title>

              </v-card-title>
              <v-card-text>
                <v-container>

                  <v-col cols='12' class='mx-auto'>

                      <v-col cols="12" xs='12' sm="12" md="12" lg='12' xl='12'>
                      <v-select 
                                v-model="editedItem.document_list" 
                                :items="document_list" 
                                label="Select Document" 
                                hint='Select Document'
                                persistent-hint 
                                return-object 
                                solo 
                                single-line 
                                prepend-icon='mdi-file-download-outline'
                                min-width='70' max-width="70">
                      </v-select>
                    </v-col>

                    <v-col v-if="allowStatusChanges === 'yes'" cols="12" xs='12' sm="12" md="12" lg='12' xl='12'>
                      <v-select v-model="editedItem._id.status" 
                                :items="statusChanges" 
                                label="Change Status" 
                                hint='Change Status'
                                persistent-hint 
                                return-object 
                                solo 
                                single-line 
                                prepend-icon='mdi-truck'
                                min-width='70' max-width="70">
                      </v-select>
                    </v-col>

                  </v-col>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <!-- CANCEL BTN -->
                <v-btn text color="cancelBtn" @click="close">
                  Close
                </v-btn>
                <!-- SAVE BTN -->
                <v-btn text color="printBtn" @click="print">
                  Print
                </v-btn>

                <v-btn text color="saveBtn" @click="update">
                  Update
                </v-btn>
              </v-card-actions>

            </v-card>
          </v-dialog>

          <!-- DELETE DIALOG -->
          <!-- <v-dialog v-model="dialogDelete" max-width="500px">
              <v-card>
                <v-card-title class="headline">Are you sure you want to delete this item?</v-card-title>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
                  <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
                  <v-spacer></v-spacer>
                </v-card-actions>
              </v-card>
            </v-dialog> -->

        </v-toolbar>
      </template>

      <!-- ROUND TOTAL DOLLAR AMOUNT -->
      <template v-slot:item.totalAmount="{ item }">
        {{ item.totalAmount.toFixed(2) }}
      </template>

      <!-- EDIT PENCIL ICON -->
      <template v-slot:item.actions="{ item }">
        <v-icon v-if="item._id.status !== 'Cancelled'" 
                small 
                color='green' 
                class="mr-2" 
                @click="edit(item)">
          mdi-pencil
        </v-icon>
      </template>


      <template v-slot:expanded-item="{ headers, item }">
        <!-- CENTER TABLE -->
        <td :colspan="headers.length">

          <v-layout col wrap>
            <!-- <v-flex xs12 sm12 md12 lg12 xl12 class='mx-auto'> -->
            <v-data-table single-expand hide-default-footer :headers="dropTableHeader" :items="item.order" :items-per-page="4000" class="elevation-1 mx-auto">
              <!-- ROUND PRICE 2 DECIMAL PLACES -->
              <template v-slot:item.order_price="{ item }">
                {{ item.order_price.toFixed(2) }}
              </template>
            </v-data-table>
            <!-- </v-flex> -->
          </v-layout>
        </td>
      </template>
    </v-data-table>
  </div>
</template>
<script>
  import { mapActions, mapGetters } from 'vuex';
  export default {
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

      dropTableHeader: {
        type: Array,
        required: false
      },

      dropdownArray: {
        type: Array,
        required: false
      },


      allowStatusChanges: {
        type: String,
        required: false,
      },
      statusChanges: {
        type: Array,
        required: false,
      }
    },

    data() {
      return {
        document_list: this.dropdownArray,
        select: { _id: '', document_type: '' },

        table_title: this.tableTitle,
        singleExpand: true,

        editedIndex: -1,
        dialog: false,

        editedItem: {
          count: 0,
          order: [],
          totalAmount: 0,
          totalItems: 0,
          _id: {
            invoice_num: '',
            status: ''
          },
        },

        defaultItem: {
          count: 0,
          order: [],
          totalAmount: 0,
          totalItems: 0,
          _id: {
            invoice_num: '',
            status: ''
          },
        },

      }
    },

    watch: {
      dialog(val) {
        val || this.close()
      },
    },

    computed: {
      ...mapGetters(['getShippedOrders']),
    },

    methods: {
      ...mapActions(['getPdfDocument',
        'get_Closed_Orders',
        'post_Update_InvoiceNum']),

      edit(item) {
        this.editedIndex = this.tableData.indexOf(item)
        // changes row items from table into object
        this.editedItem = Object.assign({}, item)
        this.dialog = true
        // console.log('edit-editedIndex: ', this.editedIndex)
        console.log('edit-editedItem: ', this.editedItem)

      },

      close() {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          //   // Resets edited index to -1 after close
          this.editedIndex = -1
        })
      },

      print() {
        // console.log('print-edited item: ', this.editedItem)
        if (this.editedIndex > -1) {
          // Object.assign(this.tableData[this.editedIndex], this.editedItem)
          this.getPdfDocument({
            invoice_num: this.editedItem._id.invoice_num,
            document: this.editedItem.document_list
          })
        }
        this.close()
      },

      update() {
        // console.log('update-editedIndex: ', this.editedIndex)
        // console.log('update-edited Item: ', this.editedItem)

        if (this.editedIndex > -1) {
          // this.editedItem = Object.assign({}, this.editedItem)
          // Object.assign(this.tableData[this.editedIndex], this.editedItem)
          // this.tableData[this.editedIndex] = this.editedItem; 
          // console.log('update: ', this.editedItem)

          this.$store.dispatch('post_Update_InvoiceNum',
            {
              invoice_num: this.editedItem._id.invoice_num,
              status: this.editedItem._id.status
            });
        } else {
          this.tableData.push(this.editedItem)
          // console.log('update else: ', this.editedItem)
        }
        this.close()
      },


    },


  }
</script>