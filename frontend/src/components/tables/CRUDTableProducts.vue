<template>
    <v-data-table 
    show-expand 
    :headers="headers" 
    :items="getProductState" 
    :search='search' 
    :items-per-page='1000' 
    item-key='product_id'
    :expanded.sync="expanded" 
    :single-expand='singleExpand'>

        <template v-slot:top>
            <v-toolbar dense rounded elevation='4' color="secondary" class='white--text'>
                <v-toolbar-title class='font-weight-bold'>{{ tableTitle }}</v-toolbar-title>
                <v-divider class="mx-4" inset vertical></v-divider>
                <v-spacer></v-spacer>
                <v-text-field v-model="search" prepend-inner-icon="mdi-magnify" label="Search Products" single-line hide-details solo-inverted dense></v-text-field>
                <v-spacer></v-spacer>

                <v-dialog persistent v-model="dialog" max-width="1968px" style='background-color: rgba(0, 0, 0, 0);'>
                    <template v-slot:activator="{ on, attrs }">
                        <v-btn small 
                                color="primary" 
                                class="font-weight-bold red--text" 
                                v-bind="attrs" v-on="on">
                            Add Product
                        </v-btn>
                    </template>
                    <ValidationObserver ref="obs" v-slot="{ handleSubmit }">
                        <!-- <v-container> -->
                        <v-card >
                            <v-card-text >
                                <v-row justify='space-around'>
                                    <v-form >
                                        <v-container fluid>

                                                <v-file-input chips multiple counter outlined
                                                    color="deep-purple accent-4"
                                                    label="New Image" 
                                                    prepend-icon="mdi-camera" 
                                                    :show-size="1000"
                                                    v-model='multiFileModel'>
                                                    <template v-slot:selection="{ index, text }">
                                                        <v-chip color="deep-purple accent-4" dark label small>
                                                          INDEX: {{ index }} - TEXT: {{ text }}
                                                        </v-chip>
                                                        <!-- <span 
                                                        class="text-overline grey--text text--darken-3 mx-2">
                                                          {{ multiFileModel.length }} File(s)
                                                        </span> -->
                                                    </template>
                                                </v-file-input>


                                            <!-- <v-row > -->
                                            <!-- <v-row v-if='getImgList.length > 0'> -->
                                                <!-- <v-col class='mx-auto'> -->
                                                  <!-- <p>  {{ getImgList }} </p> -->
                                                  <p>  {{ getImgPreviewList }} </p>
                                                  <!-- <ImageList :imageArr='getImgList' /> -->
                                                  <ImageList :imageArr='getImgPreviewList' />

                                                  <!-- <ImageList :imageArr='editedItem.product_img' /> -->
                                                    <!-- <v-img :src="url" height='100' width='200'></v-img> -->
                                                <!-- </v-col> -->
                                            <!-- </v-row> -->

                                        </v-container>
                                    </v-form>
                                </v-row>
                            </v-card-text>

                            <v-card-actions>
                                <small class='font-weight-italic red--text'>Add a new picture</small>
                                <v-spacer></v-spacer>
                                <v-btn small color="secondary" class='font-weight-bold' @click="close">Close</v-btn>
                                <v-btn small color="primaryopposite" class='font-weight-bold' @click="handleSubmit(onSubmit)">Submit</v-btn>
                            </v-card-actions>
                        </v-card>
                        <!-- </v-container> -->
                    </ValidationObserver>
                </v-dialog>
            </v-toolbar>
        </template>

        <template v-slot:item.product_img='{ item }'>
            <v-avatar size="36px">
                <img :src="item.product_img[0]">
            </v-avatar>
        </template>

        <template v-slot:item.actions="{ item }">
            <v-icon small class="mr-2" @click="editItem(item)" color='green'>mdi-pencil</v-icon>
            <v-icon small @click="deleteItem(item)" color='red'>mdi-delete</v-icon>
        </template>

        <template v-slot:expanded-item="{ headers, item }">
            <td :colspan="headers.length">
                <v-container>
                <v-flex>
                    <v-card>
                        <v-card-text>
                            <!-- <v-container pa-0> -->
                        <v-row justify='space-between'>
                            <v-col xl='11'>
                                <ImageList :imageArr='item.product_img' />
                            </v-col>

                            <v-col xl='1' class='my-auto'>
                                <v-icon small class="mr-2" @click="editItem(item)" color='green'>mdi-pencil</v-icon>
                            </v-col>
                        </v-row>
                        <!-- </v-container> -->
                        </v-card-text>
                    </v-card>
                </v-flex>
                </v-container>
            </td>
        </template>

    </v-data-table>
</template>
<script>
    import { mapActions, mapGetters } from 'vuex';
    import { ValidationObserver, ValidationProvider } from "vee-validate";
    import VTextFieldWithValidation from '@/components/forms/inputs/VTextFieldWithValidation'
    import VSelectWithValidation from '@/components/forms/inputs/VSelectWithValidation'
    import VFile from '@/components/forms/inputs/VFile'
    import ImageList from '@/components/fragments/ImageList'
    export default {
        components: {
            ValidationProvider, ValidationObserver, VFile, ImageList,
            VTextFieldWithValidation, VSelectWithValidation },
        data: () => ({
            search: '',
            tableTitle: 'Product List',
            dialog: false,
            editedIndex: -1,
            singleExpand: true,
            expanded: [],

            headers: [
                { text: "Image", value: 'product_img' },
                { text: "Name", align: 'start', value: 'product_name', align: 'start' },
                { text: "Description", value: 'product_description', align: 'start' },
                { text: "Price", value: 'price', align: 'end', width: '6%' },
                // { text: 'Actions', value: 'actions', sortable: false },
                { text: '', value: 'data-table-expand' },
            ],
            dropTableHeader: [
                { text: "Thumbnail", value: 'product_img' },
                { text: 'Actions', value: 'actions', sortable: false }
            ],
            editedItem: {},
            defaultItem: {},
        }),

        computed: {
            ...mapGetters({
                getProductState: 'stripe/getProductState',
                getImgStr: 'imgHandler/getImgStr',
                getImgList: 'imgHandler/getImgList',
                getImgPreviewList: 'imgHandler/getImgPreviewList',
                getProductStateIDX: 'stripe/getProductStateIDX',
            }),

            multiFileModel: {
                get() {
                    return this.getImgList
                },
                set(event) {
                    this.$store.dispatch('imgHandler/multiFileAction', event)
                }
            },
            // singleFileModel: {
            //     get() {
            //         return this.getImgStr
            //     },
            //     set(event) {
            //         // this.$store.commit('imgHandler/uploadImg', event)
            //         // this.$store.dispatch('imgHandler/fleekUpload', event)
            //         // this.$store.dispatch('imgHandler/imageUpload', event)
            //         this.$store.dispatch('imgHandler/singleFileAction', event)
            //     }
            // },

        },

        watch: {
          dialog (val) {
            val || this.close()
          },
        //   dialogDelete (val) {
            // val || this.closeDelete()
        //   },
        },

        methods: {
            ...mapActions({ fleekUpload: 'imgHandler/fleekUpload' }),

            editItem(item) {
                // this.editedIndex = this.desserts.indexOf(item)
                this.editedIndex = this.getProductStateIDX(item);
                this.editedItem = item;
                this.dialog = true;
                console.log('editedItem: ', this.editedItem);
            },

            close() {
                // clear all imgHandler state on close button
                this.$store.commit('imgHandler/CLEAR_IMAGE_STATE');
                this.dialog = false;
                this.$nextTick(() => {
                    this.editedItem = Object.assign({}, this.defaultItem);
                    this.editedIndex = -1;
                })
            },

            onSubmit() {// If item has index it is not new, and we update with update api endpoint. 
                console.log('Submit: ', this.editedItem);
                // post product id from editeditem
                this.$store.dispatch('imgHandler/fleekUploadMulti', this.editedItem);
                // this.$store.dispatch('imgHandler/fleekUploadFromState', this.editedItem)
                
            },


        },


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