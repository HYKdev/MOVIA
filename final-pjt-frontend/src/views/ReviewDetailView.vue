<template>
  <div>
    <h1>Review Detail</h1>
    <h2>{{ review.title }}</h2>
    <p>{{ review.content }}</p>
    <div v-if="isAuthor">
      <router-link :to="{ name: 'reviewedit', params: { reviewPk } }">
        <button>Edit</button>
      </router-link>
      <button @click="deleteReview(reviewPk)">Delete</button>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewDetail',
  data() {
    return {
      reviewPk: this.$route.params.reviewPk
    }
  },
  computed: {
    ...mapGetters(['isAuthor', 'review'])
  },
  methods: {
    ...mapActions(['fetchReview', 'deleteReview'])
  },
  created () {
    this.fetchReview(this.reviewPk)
  }
}
</script>

<style>

</style>