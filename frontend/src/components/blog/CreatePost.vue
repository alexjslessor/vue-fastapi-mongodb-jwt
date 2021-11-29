<template>
  <div>
    <v-row justify="center">

      <div style='background-color: black;'>
        <!-- {{ postImg }} -->
        <!-- <v-img ref='imgPreview' src=`${base64String}` /> -->
        <!-- <v-img ref='imgPreview' src="postImage" /> -->
        <!-- <v-img :src="url"></v-img> -->

        <!-- <v-img class="white--text align-end" :src="`data:image/png;base64,${base64String}`" ></v-img> -->
      </div>

      <!-- <v-card> -->
      <!-- <v-card-title> -->
      <!-- <span class="headline">Create Post</span> -->
      <!-- </v-card-title> -->

      <v-card-text>
        <v-container>

          <v-row>

            <v-col>
              <!-- <VFile rules="required" label="Post Image" hint=" Post Images" v-model="postImage" /> -->
              <!-- <v-file-input label="Headline Image" prepend-icon="mdi-camera" v-model='postImage' @change='PreviewImage'> -->
              <v-file-input label="Headline Image" prepend-icon="mdi-camera" v-model='headlineImage'>
              </v-file-input>

            </v-col>
            <v-col>
              <v-img :src="url" height='100' width='200'></v-img>
            </v-col>

          </v-row>

          <VTextFieldWithValidation rules="required" v-model="title" label="Title" hint='Title' prepend-inner-icon='mdi-account' />
          <VTextFieldWithValidation rules="required" v-model="headline" label="Headline" hint='Headline' prepend-inner-icon='mdi-account' />


          <tiptap-vuetify v-model="content" :extensions="extensions" placeholder="Create a new post …" :card-props="{ flat: true, color: '#010101' }" :toolbar-attributes="{ color: 'black', dark: true, dense: true }" />
        </v-container>
      </v-card-text>

      <v-row justify="end">
        <v-card-actions>

          <v-btn small @click='onSubmit' color="blue darken-1">
            Save
          </v-btn>

        </v-card-actions>
      </v-row>

      <!-- </v-card> -->

    </v-row>
  </div>
</template>
<script>
  import { mapGetters, mapActions } from "vuex";
  import VTextFieldWithValidation from '@/components/forms/inputs/VTextFieldWithValidation'
  // import VFile from '@/components/forms/inputs/VFile'
  import {
    TiptapVuetify, Heading, Bold, Italic, Strike,
    Underline, Code, Paragraph, BulletList, OrderedList,
    ListItem, Link, Blockquote, HardBreak, HorizontalRule, History, Image
  } from 'tiptap-vuetify'

  export default {
    components: {
      TiptapVuetify,
      // VFile, 
      VTextFieldWithValidation
    },

    data: () => ({
      base64String: '',
      url: null,

      extensions: [
        Image,
        History,
        Blockquote,
        Link,
        Underline,
        Strike,
        Italic,
        ListItem,
        BulletList,
        OrderedList,
        [Heading, {
          options: {
            levels: [1, 2, 3]
          }
        }],
        Bold,
        Code,
        HorizontalRule,
        Paragraph,
        HardBreak
      ],
    }),

    methods: {
      onSubmit() {
        console.log('submit post')
        this.$store.dispatch('blog/createPost')
      },

      PreviewImage() {
        this.url = URL.createObjectURL(this.postImage)
        console.log('preview image', this.url)
      },

      // imageUploaded(file) {
      //     const reader = new FileReader();
      //     reader.onload = function () {
      //         // this.base64String = reader.result.replace("data:", "").replace(/^.+,/, "");
      //         // this.base64String = reader.result
      //         this.base64String = JSON.stringify(reader.result)
      //         // return reader.result
      //         console.log('base64string: ', this.base64String);
      //     }
      //     reader.readAsDataURL(file);
      // },

    },

    computed: {

      ...mapGetters({
        postTitle: 'blog/getPostTitle',
        postHeadline: 'blog/getPostHeadline',
        postImg: 'blog/getPostImg',
        post: 'blog/getPostContent'
      }),


      title: {
        get() {
          return this.postTitle
        },
        set(value) {
          this.$store.commit('blog/updateTitle', value)
        }
      },

      headline: {
        get() {
          return this.postHeadline
        },
        set(head) {
          this.$store.commit('blog/updateHeadline', head)
        }
      },

      headlineImage: {
        get() {
          return this.postImg
        },
        set(event) {
          // this.imageUploaded(event)
          // const img_file = this.imageUploaded(event)
          this.$store.commit('blog/updateImage', event)
          // this.$store.commit('blog/updateImage', this.base64String)
        }
      },

      content: {
        get() {
          return this.post
        },
        set(cont) {
          this.$store.commit('blog/updateContent', cont)
        }
      }



    }



  }
</script>