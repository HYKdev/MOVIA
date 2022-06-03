<template>
  <div class="container my-5 p-5">
    <div>
      <div class="review p-3">
        <h1>이제훈은 {{ review.title }} 배우다</h1>

        <p>
          {{ review.content }}
        </p>
        <div v-if="isAuthor">
          <router-link :to="{ name: 'reviewedit', params: { reviewPk } }">
            <button class="btn btn-success m-1">Edit</button>
          </router-link>
          |
          <button @click="deleteReview(reviewPk)" class="btn btn-success">Delete</button>
        </div>
      </div>

      <hr />
      <div class="comment p-3">
        <comment-list :comments="review.comments"></comment-list>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import CommentList from '@/components/CommentList.vue';

export default {
  name: 'ReviewDetail',
  components: { CommentList },
  data() {
    return {
      reviewPk: this.$route.params.reviewPk,
    };
  },
  computed: {
    ...mapGetters(['isAuthor', 'review']),
  },
  methods: {
    ...mapActions(['fetchReview', 'deleteReview']),
  },
  created() {
    this.fetchReview(this.reviewPk);
  },
};
</script>

<style scoped>
.container {
  border-radius: 20px;
  border: 1px solid rgba(255, 255, 255, 0.5);
  box-shadow: 0 25px 45px rgba(0, 0, 0, 0.1);
  /* box-shadow: 2px 2px 5px 0; */
}
</style>
