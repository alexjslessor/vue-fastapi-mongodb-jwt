<template>
  <div>
        <v-data-table hide-default-footer :headers="tableHeader" :items="tableData" class='elevation-10'>

          <template v-slot:top>
            <v-toolbar flat dense>
              <!-- TABLE TITLE -->
              <v-toolbar-title class='font-weight-bold'>{{ tableTitle }}</v-toolbar-title>
              <!-- <v-divider class="mx-4" inset vertical> -->
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
                          <v-text-field outlined
                                        clearable
                                        dense
                                        v-model.number="editedItem.quantity" 
                                        hint='How many would you like to order'
                                        label="Qty."
                                        persistent-hint
                                        type='number'
                                        prepend-icon='mdi-counter'>
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
            <!-- <v-btn small rounded elevation='2' color='primary' class='font-weight-bold' style='color: #D92231;'> -->
              ${{ item.price.toFixed(2) }}
            <!-- </v-btn> -->
         </template>

          <template v-slot:item.subtotal="{ item }">
              <v-btn small rounded elevation='2' color='primary' class='font-weight-bold' style='color: #D92231;'>
                ${{ item.subtotal.toFixed(2) }}
              </v-btn>
           </template>


            <!-- PENCIL ICON -->
            <template v-slot:item.actions="{ item }">
              <v-icon small class="mr-2" @click="editItem(item)" color='green'>mdi-pencil</v-icon>
              <!-- <v-icon small @click="deleteItem(item)" color='secondary'>mdi-delete</v-icon> -->
            </template>

        </v-data-table>
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
    },

    data() {
      return {
        date: new Date().toISOString().substr(0, 10),
        menu: false,
        dialog: false,
        formTitle: this.sku,
        editedIndex: -1,
        editedItem: [],
      }
    },

    filters: {
      format_date(value) {
        return new Date(value).toISOString().substr(0, 10)},
    },

    computed: {...mapGetters(['getCartSize']) },

    watch: {
      dialog(val) {
        val || this.close()
      },
    },

    methods: {
      editItem(item) {
        // console.log('editItem - editItem before: ', this.editedItem)
        this.editedIndex = this.tableData.indexOf(item)
        // changes row items from table into object?
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem(item) {
        confirm('Are you sure you want to delete this item?')

        this.$store.dispatch('popCartItemAction', item.product);
        const index = this.tableData.indexOf(item)
        // confirm('Are you sure you want to delete this item?') && this.tableData.splice(index, 1)
        this.tableData.splice(index, 1)

        // If all items deleted from cart by user -> redirect to /shop
        if (this.getCartSize == 0) {this.$router.push('/shop')}
      },

      close() {
        this.dialog = false
        this.$nextTick(() => {
          // this.editedItem = Object.assign({}, this.defaultItem)
          // Resets edited index to -1 after close
          this.editedIndex = -1
        })
      },


      save(item) {
        if (this.editedIndex > -1) {
          try {
            // this.$store.dispatch('updateCart', this.editedItem);
            this.$store.commit('UPDATE_CART', this.editedItem);
          } catch(e) {
            this.$store.dispatch('infoSnackBar', {statusText: 'Checkout Update Table: Uh Oh, please try again later', data: {info: `${e}` }});
          }
        } else {
          this.tableData.push(this.editedItem)
          // console.log('save 2: ', this.editedItem)
        }
        this.close()
      },

  },




}
</script>
