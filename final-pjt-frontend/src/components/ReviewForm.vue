<template>
  <form @submit.prevent="onSubmit">
    <div>
      <label for="title">title: 이제훈은</label>
      <input v-model="newReview.title" type="text" id="title" />
      <label for="title">배우다</label>
    </div>
    <div>
      <label for="content">content: </label>
      <textarea v-model="newReview.content" type="text" id="content"></textarea>
    </div>
    <div>
      <button>{{ action }}</button>
    </div>
  </form>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'ReviewForm',
  props: {
    review: Object,
    action: String,
  },
  data() {
    return {
      newReview: {
        // reviewPk: this.review.id,
        title: this.review.title,
        content: this.review.content,
      },
    };
  },

  methods: {
    ...mapActions(['createReview', 'updateReview']),
    onSubmit() {
      if (this.action === 'create') {
        this.createReview(this.newReview);
      } else if (this.action === 'update') {
        const payload = {
          pk: this.review.id,
          ...this.newReview,
        };
        this.updateReview(payload);
      }
    },
  },
};
</script>

<style scoped></style>
