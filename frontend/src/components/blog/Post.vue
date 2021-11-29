<template>
  <div>
    <v-container fluid>

      <v-row>
        <v-col>
          <v-flex xs12 sm8 md8 lg7 xl7 class='mx-auto pt-3'>
            <v-card class='mx-auto'>
              <v-img contain class="white--text align-end pt-2" height="200px" :src="`data:${post.post_image_content_type};base64,${post.post_image_bytes}`" >
              </v-img>

              <v-card-title>{{ post.title }}</v-card-title>
              <v-card-subtitle>{{ post.headline }}</v-card-subtitle>
              <!-- <v-card-text >{{ i.headline }}</v-card-text> -->
              <v-card-text v-html='post.content'></v-card-text>
              <!-- </v-img> -->
            </v-card>
            </v-flex>
        </v-col>
      </v-row>

      <br />

      <v-row>
        <v-col>
          <v-flex xs10 sm10 md4 lg4 xl4 class='mx-auto pt-3'>
            <v-card class='p-3 m-3'>
              <ValidationObserver ref="postComment" v-slot="{ invalid, validated, handleSubmit, validate }">
                <v-card-text>
                <v-form class='p-2 m-3'>

                    <VTextFieldWithValidation label="Comment" hint='Comment' v-model="postComment" />

                    <v-card-actions>
                      <v-spacer></v-spacer>

                      <v-btn small color="primaryopposite" class='font-weight-bold' @click="handleSubmit(onSubmit)">Submit</v-btn>
                    </v-card-actions>

                </v-form>
                </v-card-text>
              </ValidationObserver>

            </v-card>
          </v-flex>
        </v-col>
      </v-row>

    </v-container>
  </div>
</template>
<script>
  import { ValidationObserver, ValidationProvider } from "vee-validate"
  import VTextFieldWithValidation from '@/components/forms/inputs/VTextFieldWithValidation'
  export default {
    components: { ValidationObserver, VTextFieldWithValidation },

    props: {
      postId: {
        type: String,
        // type: Object,
        required: false
      },
    },

    data() {
      return {
        post: {},
        postComment: '',
      }
    },

    methods: {
      onSubmit() {
        console.log('post comment: ', this.postComment)
      }
    },

    async mounted() {
      let d = await this.$store.dispatch('blog/readPost', this.postId);
      this.post = Object.assign({}, d.data)
      // console.log('single post: ', d)
    }

    
  }
</script>
<style >
  .v-card--reveal {
    align-items: center;
    bottom: 0;
    justify-content: center;
    opacity: .5;
    position: absolute;
    width: 100%;
  }

  p {
    text-align: center;
  }

  p img {
    width: 90%;
    height: 500px;
  }
</style>