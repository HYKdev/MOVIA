<template>
  <form @submit.prevent="onSubmit">
    <div>
      <label for="title">title: </label>
      <input v-model="newReview.title" type="text" id="title">
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
import { mapActions } from 'vuex'

export default {
  name: 'ReviewForm',
  props: {
    review: Object,
    action: String,
  },
  data() {
    return {
      newReview: {
        title: this.review.title,
        content: this.review.content,
      }
    }
  },

  methods: {
    ...mapActions(['createReview']),
    onSubmit() {
      if (this.action === 'create') {
        this.createReview(this.newReview)
      }
    }
  }
}
</script>

<style>

</style>