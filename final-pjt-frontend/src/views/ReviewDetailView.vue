<template>
  <div>
    <h1>Review Detail</h1>
    {{ review }}
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
    ...mapActions(['fetchReview'])
  },
  created () {
    this.fetchReview(this.reviewPk)
  }
}
</script>

<style>

</style>