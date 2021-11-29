<template>
  <div>
    <v-container fluid>
      <!-- <p>{{ postsArr }}</p> -->
      <br />
      <br />
      <v-row>
        <v-col>
          <PostsCard :cardData="postsArr" />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
  <script>
import PostsCard from "@/components/blog/PostsCard";
import { mapGetters, mapActions } from "vuex";

export default {
  components: {
    PostsCard,
  },

  data: () => ({
    postsArr: [],
  }),

  async created() {
    // Commit products to product store
    this.postsArr = await this.$store.dispatch("blog/query_db", {
      query: "all_posts",
      filter: "all",
    });
    console.log(this.postsArr);
  },
};
</script>
    