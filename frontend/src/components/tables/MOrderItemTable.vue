<template>
  <div>
        <v-data-table :headers="tableHeader" 
                      :items="tableData" 
                      class='elevation-1'>

          <template v-slot:top>
            <v-toolbar flat>
              <!-- TABLE TITLE -->
              <v-toolbar-title class='font-weight-bold'>{{ tableTitle }}</v-toolbar-title>
              <v-divider class="mx-4" inset vertical>
              </v-divider>

              <v-spacer></v-spacer>

              <v-dialog v-model="dialog" max-width="500px">

                <v-card>
                  <!-- DIALOG TITLE -->
                  <v-card-title>
                    <span class="headline mx-auto">{{ formTitle }}</span>
                  </v-card-title>

                  <v-card-text>
                    <v-container>
                      <v-col cols='12' class='mx-auto'>
                        
                        <v-col v-if='getUserType' cols="12" xs='12' sm="12" md="12" lg='12' xl='12'>
                          <v-text-field dense
                                        prepend-icon='mdi-counter'
                                        v-model.number="editedItem.quantity_fulfilled_count" 
                                        label="Qty In Production"
                                        solo
                                        type='number'
                                        persistent-hint
                                        hint='Qty in production'
                                        clearable>
                          </v-text-field>
                        </v-col>

                        <v-col cols="12" xs='12' sm="12" md="12" lg='12' xl='12'>
                          <v-select v-model="editedItem.status" 
                                    :items="status_changes" 
                                    label="Change Status" 
                                    persistent-hint 
                                    return-object 
                                    solo
                                    single-line 
                                    hint='Change Status'
                                    prepend-icon='mdi-truck'
                                    min-width='70' 
                                    max-width="70">
                          </v-select>
                        </v-col>

                      </v-col>
                    </v-container>
                  </v-card-text>

                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <!-- CANCEL BTN -->
                    <v-btn text color="red darken-1" @click="close">
                      Cancel
                    </v-btn>
                    <!-- SAVE BTN -->
                    <v-btn text color="green accent-3" @click="save">
                      Update
                    </v-btn>
                  </v-card-actions>

                </v-card>
              </v-dialog>
            </v-toolbar>
          </template>

          <template v-slot:item.date_submitted.$date="{ item }">
            {{ item.date_submitted.$date | format_date }}

          </template>

          <template v-slot:item.fulfillment_date.$date="{ item }">
            {{ item.fulfillment_date.$date | format_date }}
          </template>


            <!-- PENCIL ICON -->
            <template v-slot:item.actions="{ item }">
              <v-icon small color='green' class="mr-2" @click="editItem(item)">
                mdi-pencil
              </v-icon>
            </template>

    </v-data-table>

    <!-- {{ formatDates }} -->
  </div>
</template>
<script>
  import { mapGetters, mapActions } from 'vuex';
  export default {
    props: {
      sku: {
        type: String,
        required: false
      },

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

      dropdownArray: {
        type: Array,
        required: false
      },

    },
    data() {
      return {
        status_changes: this.dropdownArray,
        select: { _id: '', status: '' },
        editedIndex: -1,
        editedItem: [],
        dialog: false,
        formTitle: this.sku,
      }
    },

    computed: {
      ...mapGetters(['getUserType']),

      // formatDates() {
      //   console.log('format Dates')
      //   // console.log(this.tableData)
      //   const d = this.tableData.forEach(function(val, idx, arr) {
      //     // arr[idx].date_submitted.$date = new Date(val).toISOString().substr(0, 10);
      //     arr[idx].date_submitted.$date = new Date(arr[idx].date_submitted.$date).toISOString().substr(0, 10);
      //     arr[idx].fulfillment_date.$date = new Date(arr[idx].fulfillment_date.$date).toISOString().substr(0, 10);
      //   })
      // }
    },

    watch: {
      dialog(val) {
        val || this.close()
      },
    },

    methods: {
      editItem(item) {
        console.log('editItem: ', item)
        this.editedIndex = this.tableData.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
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
          // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign
          Object.assign(this.tableData[this.editedIndex], this.editedItem)
          //update DB
          // this.post_Update_QueItem_Api(this.editedItem);
          this.$store.dispatch('postUpdateFromJSON', {event: this.editedItem, 
                                                      collection: 'order'})

        } else {
          this.tableData.push(this.editedItem)
        }
        this.close()
      },

      ...mapActions(['post_Update_QueItem_Api']),
    },


    filters: {
      format_date(value) {
        return new Date(value).toISOString().substr(0, 10);
      }
    },



}
</script>
