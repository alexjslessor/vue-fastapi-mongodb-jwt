<template>
  <div>
    <v-container fluid>

      <v-row v-for='i in cardData' :key='i.id'>
        <v-col>

          <v-flex xs12 sm9 md5 lg4 xl3 class='mx-auto pt-3'>
            <v-card :to="{ name: 'Post', params: { postId: i._id }}">

              <v-img class="white--text align-end" height="200px" :src="`data:${i.post_image_content_type};base64,${i.post_image_bytes}`">
              <!-- <v-img class="white--text align-end" height="200px" :src="`data:${i.content_type};base64,${i.post_image}`"> -->

              <v-card-title>{{ i.title }}</v-card-title>
              <v-card-text >{{ i.headline }}</v-card-text>
            </v-img>

            </v-card>
          </v-flex>

        </v-col>
      </v-row>

    </v-container>
  </div>
</template>
<script>
  export default {
    props: {
      cardData: {
        type: Array,
        required: false
      },
    },

    data() {
      return { }
    },

    methods: {},

  }
</script>
<style>
  .v-card--reveal {
    align-items: center;
    bottom: 0;
    justify-content: center;
    opacity: .5;
    position: absolute;
    width: 100%;
  }
</style>