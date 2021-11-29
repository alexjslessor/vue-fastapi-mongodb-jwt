<template>
    <v-data-table 
    show-expand
    :headers="headers" 
    :items="getProductState" 
    :search='search' 
    :items-per-page='1000'
    item-key='product_id'
    :single-expand='singleExpand'>

        <template v-slot:top>
            <v-toolbar dense rounded elevation='4' color="secondary" class='white--text'>

                <v-toolbar-title class='font-weight-bold'>{{ tableTitle }}</v-toolbar-title>
                <v-divider class="mx-4" inset vertical></v-divider>
                <v-spacer></v-spacer>

                <v-text-field v-model="search" prepend-inner-icon="mdi-magnify" label="Search Products" single-line hide-details solo-inverted dense></v-text-field>

                <v-spacer></v-spacer>

                <v-dialog v-model="dialog" max-width="1968px" style='background-color: rgba(0, 0, 0, 0);'>

                    <template v-slot:activator="{ on, attrs }">
                        <v-btn small color="primary" class="font-weight-bold red--text" v-bind="attrs" v-on="on">
                            Add Product
                        </v-btn>
                    </template>

                    <ValidationObserver ref="obs" v-slot="{ invalid, validated, handleSubmit, validate }">
                        <v-card>
                            <v-toolbar dense rounded class='mb-2' color="primary">
                                <v-toolbar-title class='font-weight-bold'>{{ formTitle }}</v-toolbar-title>
                            </v-toolbar>

                            <v-card-text>
                                <v-row>

                                    <v-form>
                                        <v-container fluid>
                                            <v-layout row wrap>

                                                <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
                                                    <VTextFieldWithValidation rules="required" label="Title" hint='Product Name' v-model="editedItem.product_name" />
                                                </v-col>

                                                <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
                                                    <VTextFieldWithValidation rules="required" label="Description" hint='Product Description' v-model="editedItem.product_description" prepend-inner-icon='mdi-account' />
                                                </v-col>

                                                <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
                                                    <VTextFieldWithValidation rules="required" type='number' label="Price" hint='Price' v-model="editedItem.price" />
                                                </v-col>

                                                <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
                                                    <VTextFieldWithValidation rules="required" type='number' label="Shipping Cost" hint="Shipping Cost" v-model="editedItem.shipping_cost" />
                                                </v-col>

                                                <v-col cols="12" xs='7' sm='6' md='6' lg='4' xl='3'>
                                                    <VFile rules="required" label="Product Images" hint=" Product Images" v-model="editedItem.product_img_list" />

                                                <!-- <v-file-input
                                                    small-chips
                                                    multiple
                                                    label="File input w/ small chips">
                                                </v-file-input> -->
                                            </v-col>
                                            </v-layout>

                                        </v-container>
                                    </v-form>
                                </v-row>
                            </v-card-text>

                            <v-card-actions>
                                <small class='font-weight-italic red--text'>Sell with crypto.</small>
                                <v-spacer></v-spacer>
                                <v-btn small color="secondary" class='font-weight-bold' @click="close">Close</v-btn>
                                <v-btn small color="primaryopposite" class='font-weight-bold' @click="handleSubmit(onSubmit)">Submit</v-btn>
                                <!-- <v-btn small color="primaryopposite" class='font-weight-bold' @click="handleSubmit(onSubmit)" :disabled="invalid || !validated">Submit</v-btn> -->
                            </v-card-actions>

                        </v-card>
                    </ValidationObserver>
                </v-dialog>
            </v-toolbar>
        </template>


        <template v-slot:item.product_img='{ item }'>
            <v-avatar size="36px">
                <img :src="item.product_img">
            <!-- <img src="https://avatars0.githubusercontent.com/u/9064066?v=4&s=460"> -->
            <!-- <v-icon v-else :color="message.color" v-text="message.icon"></v-icon> -->
          </v-avatar>
        </template>

        <template v-slot:item.actions="{ item }">
            <v-icon small class="mr-2" @click="editItem(item)" color='green'>mdi-pencil</v-icon>
            <v-icon small @click="deleteItem(item)" color='red'>mdi-delete</v-icon>
        </template>

        <template v-slot:no-data>
            <v-btn small color="secondary" class='font-weight-bold' @click="initialize">
                Reset
            </v-btn>
        </template>

        <!-- <template v-slot:expanded-item="{ headers, item }">
            <td :colspan="headers.length">
    
              <v-layout col wrap>
                <v-data-table single-expand hide-default-footer 
                :headers="dropTableHeader" 
                :items="item.product_img" 
                :items-per-page="4000" class="elevation-15 mx-auto">
                <template v-slot:item.product_img='{ item }'>
                    <v-avatar size="36px">
                        <img :src="item">
                    </v-avatar>
                    <p>{{ item }}</p>
                </template>
                <template v-slot:item.actions="{ item }">
                    <v-icon small class="mr-2" @click="editItem(item)" color='green'>mdi-pencil</v-icon>
                    <v-icon small @click="deleteItem(item)" color='red'>mdi-delete</v-icon>
                </template>
                </v-data-table>
              </v-layout>
            </td>
          </template> -->

          <template v-slot:expanded-item="{ headers, item }">
            <td :colspan="headers.length">
              <v-layout col wrap>
                <ImageList :imageArr='item.product_img' />
                <!-- <template v-slot:item.actions="{ item }"> -->
                    <v-card class='mx-auto'>
                    <!-- <v-file-input label="Headline Image" prepend-icon="mdi-camera" v-model='headlineImage'></v-file-input> -->
                    <!-- <v-icon small class="mr-2" @click="editItem(item)" color='green'>mdi-pencil</v-icon> -->
                    <!-- <v-icon small @click="deleteItem(item)" color='red'>mdi-delete</v-icon> -->
                    </v-card>
                <!-- </template> -->
              </v-layout>
            </td>
          </template>

    </v-data-table>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';
import { ValidationObserver, ValidationProvider } from "vee-validate";
// import { setInteractionMode } from 'vee-validate'
import VTextFieldWithValidation from '@/components/forms/inputs/VTextFieldWithValidation'
import VSelectWithValidation from '@/components/forms/inputs/VSelectWithValidation'
import VFile from '@/components/forms/inputs/VFile'
import ImageList from '@/components/fragments/ImageList'
import fleek from '@fleekhq/fleek-storage-js';   
export default {
components: { 
    ValidationProvider, ValidationObserver, 
    VTextFieldWithValidation, VSelectWithValidation, VFile,
    ImageList },

        data: () => ({
            search: '',
            tableTitle: 'Product List',
            dialog: false,
            desserts: [],
            editedIndex: -1,
            singleExpand: true,

            headers: [
                // { text: "Name", align: 'start', value: 'product_name', width: '6%' },
                { text: "Name", align: 'start', value: 'product_name', width: '6%' },
                { text: "Description", value: 'product_description', align: 'start' },
                { text: "Price", value: 'price', align: 'end', width: '6%' },
                { text: "Image", value: 'product_img' },
                { text: 'Actions', value: 'actions', sortable: false }
            ],
            dropTableHeader: [
                { text: "Thumbnail", value: 'product_img' },
                // { text: "Image URL", value: 'product_img' },
                { text: 'Actions', value: 'actions', sortable: false }
            ],
            editedItem: {},
            defaultItem: {},
        }),

        computed: {
            formTitle() {
                return this.editedIndex === -1 ? 'New Product' : 'Edit Product'
            },

            ...mapGetters({
                // getCart: 'stripe/getCart', 
                getProductState: 'stripe/getProductState'
            }),

        },
        watch: {
            dialog(val) {
                val || this.close()
            },
        },

        methods: {
            ...mapActions({query: 'stripe/query_db'}),

            async fleekUpload(event) {
                const input = {
                  apiKey: 'RmOhy96hLwmuDBsOueAq5g==',
                  apiSecret: 'ryBoPW0b7RYn4qasQYtlCwMBgb0kSD7AU4ZSTj5Br7s=',
                  key: `my-folder/my-file-name`,
                  data: myFile,
                };
                const result = await fleek.upload(input);
            },

            editItem(item) {
                // console.log('edit item type: ', typeof item)
                //makes copy of array object & assigns to editedItem as temporary store
                // this.editedIndex = this.desserts.indexOf(item)
                // this.editedItem = Object.assign({}, item)
                this.dialog = true
                // console.log('editedItem product: ', this.editedItem)
            },

            close() {
                this.dialog = false
                this.$nextTick(() => {
                    // this.editedItem = Object.assign({}, this.defaultItem)
                    this.editedIndex = -1
                    // console.log('editedItem: ', this.editedItem)
                })
            },

            updateProduct() {
                console.log('update product: ', this.editedItem)
                // this.$store.dispatch('postForm', { event: this.editedItem })
                // this.$store.dispatch('postUpdateFromJSON', { event: this.editedItem, collection: 'edit_product' })
                // Object.assign(this.desserts[this.editedIndex], this.editedItem)
                // this.desserts.splice(this.editedIndex, 1, this.editedItem)
            },
            createProduct() {
                // console.log(this.editedItem)
                console.log('create product: ', this.editedItem)
                // this.$store.dispatch('postForm', { event: this.editedItem })
                this.$store.dispatch('postForm', this.editedItem )

                // this.$store.dispatch('postUpdateFromJSON', {event: this.editedItem, collection: 'new_product'})
                // this.desserts.push(this.editedItem)
            },

            onSubmit() {// If item has index it is not new, and we update with update api endpoint.
                if (this.editedIndex > -1) {//UPDATE PRODUCT - check if entry has index 
                    console.log('update product: ')
                    // this.$store.dispatch('postUpdateFromJSON', { event: this.editedItem, collection: 'edit_product' })
                    // this.desserts.splice(this.editedIndex, 1, this.editedItem)
                    // this.updateProduct()
                    this.close()

                } else {// NEW PRODUCT - If item does not have index it is new, create new entry in endpoint.

                    
                    // let check_duplicate_sku = this.desserts.find(p => {
                    //     if (p.sku == this.editedItem.sku) return true
                    //     return false
                    // });

                    // if (check_duplicate_sku) {// DUPLICATE
                    //     this.$store.dispatch('snackBar', { cardColor: 'red', statusText: 'DUPLICATE', data: { info: `This SKU already exists` } });

                    // } else {// NOT DUPLICATE
                        console.log('NOT-duplicate: ')
                    //     // // this.$store.dispatch('postUpdateFromJSON', {event: this.editedItem, collection: 'new_product'})
                    //     // this.desserts.push(this.editedItem)
                        // this.createProduct()
                        this.close()
                    // }
                }
            },

            deleteItem(item) {
                let confirmDelete = confirm(`Are you sure you want to delete ${item.sku}? This action is irreversible.`);
                if (confirmDelete) {

                    try {
                        const index = this.desserts.indexOf(item)
                        this.desserts.splice(index, 1)
                        this.$store.dispatch('delete_document_db', { collection: 'products', object_id: item._id.$oid, feedback: `SKU ${item.sku} Deleted Successfully!`} )
                    } catch(e){
                        this.$store.dispatch('snackBar', 
                        { cardColor: 'red', statusText: 'Product unable to be deleted.', data: { info: `` } });
                    }

                }
            },


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


        filters: {
            format_date(value) {
                return new Date(value).toISOString().substr(0, 10);
            }
        },

    //     beforeCreate() {
    //         this.initialize()
    //     //   await this.$store.dispatch('stripe/query_products', {query: 'all_products', filter: 'all'});
    //   }


    }
</script>
<!-- https://stackoverflow.com/questions/50985783/vuetify-css-not-working-taking-effect-inside-component/50985784#50985784 -->
<style scoped>
    /* table header style */
    >>>.v-data-table-header tr th span {
        color: gray !important;
        border-bottom: none !important;
        font-weight: bold !important;
        font-size: 17px !important;
    }

    /* table body styles */
    >>>.v-data-table__wrapper table tbody tr td {
        color: white !important;
        /* border-bottom: none !important; */
        font-weight: bold !important;
        font-size: 16px !important;
    }
</style>