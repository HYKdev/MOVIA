<template>
  <div>
    <h1>ReviewList</h1>
    <button><router-link :to="{ name: 'reviewnew' }">게시글 작성하기</router-link></button>
    {{ reviews }}
  </div>  
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'ReviewList',
  computed: {
    ...mapGetters(['reviews'])
  },
  methods: {
    ...mapActions(['fetchReviews'])
  },
  created() {
    this.fetchReviews()
  }
}
</script>

<style>

</style>