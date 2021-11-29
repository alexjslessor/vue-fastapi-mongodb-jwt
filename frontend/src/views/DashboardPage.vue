<template>
  <div>
    <UserSettingsNav>
      <DialogWrapper slot='one' activatorBtnText='Create Post' btnText='Close'>
        <CreatePost />
      </DialogWrapper>

      <!-- <DialogWrapper slot='one' activatorBtnText='Shipping' btnText='My Shipping Info'> -->
      <!-- <CRUDTable></CRUDTable> -->
      <!-- </DialogWrapper> -->

      <!-- <DialogWrapper slot='two' activatorBtnText='Products' btnText='Close'> -->
        <!-- <CRUDTableProducts></CRUDTableProducts> -->
      <!-- </DialogWrapper> -->

    </UserSettingsNav>

    <v-container fluid class='my-12'>
      <v-row>
        <v-col cols='12'>
          <v-card class="mx-auto elevation-12 pb-12 pl-4 pr-4 m-4">

            <CRUDTableProducts></CRUDTableProducts>

            <!-- <DataTable :headers='headers' :items='getProductState'>
              <ToolbarHeader slot='top' title='Master Table'>
                <v-spacer></v-spacer>
                <v-text-field v-model="search" prepend-inner-icon="mdi-magnify" label="Search Products" single-line hide-details solo-inverted dense></v-text-field>
                <v-spacer></v-spacer>
                <DialogWrapper activatorBtnText='Products' btnText='Close'>
                  New Product Form
                </DialogWrapper>
              </ToolbarHeader>
            </DataTable> -->

          </v-card>
        </v-col>
      </v-row>
    </v-container>

  </div>
</template>
<script>
  import { mapGetters, mapActions } from 'vuex';
  import UserSettingsNav from '@/components/navBars/UserSettingsNav';
  import DialogWrapper from '@/components/fragments/dialogs/DialogWrapper';
  import CRUDTable from '@/components/tables/CRUDTable';
  import CRUDTableProducts from '@/components/tables/CRUDTableProducts';
  import DataTable from '@/components/tables/DataTable';
  import CreatePost from '@/components/blog/CreatePost'
  import ToolbarHeader from '@/components/fragments/ToolbarHeader'

  import { ValidationObserver, ValidationProvider } from "vee-validate";
  import VTextFieldWithValidation from '@/components/forms/inputs/VTextFieldWithValidation'
  import VSelectWithValidation from '@/components/forms/inputs/VSelectWithValidation'
  import VFile from '@/components/forms/inputs/VFile'

  // import MarkdownIt from '@/components/old/markDown/MarkdownIt.vue'
  // import MarkdownEditor from '@/components/mkdown/MarkdownEditor'
  // import Vor from '@/components/old/markDown/Vor.vue'
  export default {
    name: "Dashboard",
    components: {
      ToolbarHeader,
      DialogWrapper,
      UserSettingsNav,
      CRUDTable,
      CRUDTableProducts,
      CreatePost,
      DataTable,
      // TiptapBasic,
      // TiptapMain,
      // Vor,
      // MarkdownEditor,
      // MarkdownIt,
      ValidationProvider, 
      ValidationObserver, 
      VTextFieldWithValidation, 
      VSelectWithValidation, 
      VFile
    },

    data() {
      return {
        search: '',
        editedItem: {},
        defaultItem: {},
        
        headers: [
          { text: "Name", align: 'start', value: 'product_name', width: '6%' },
          { text: "Description", value: 'product_description', align: 'start' },
          { text: "Price", value: 'price', align: 'end', width: '6%' },
          { text: "Image", value: 'product_img' },
          { text: 'Actions', value: 'actions', sortable: false }
        ],
      }
    },


  created() {
    this.initialize();
  },

  methods: {
    async initialize() {
      await this.$store.dispatch('stripe/query_products', {query: 'all_products', filter: 'all'});
    },
  },
    computed: {

      ...mapGetters({
        // getCart: 'stripe/getCart', 
        getProductState: 'stripe/getProductState'
      }),
    }



  };
</script>