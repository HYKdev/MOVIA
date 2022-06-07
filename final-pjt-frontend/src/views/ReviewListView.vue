<template>
  <div>
    <h1>ReviewList</h1>
    <router-link :to="{ name: 'reviewnew' }">
      <button>게시글 작성하기</button>
    </router-link>
    <ul>
      <li v-for="review in reviews" :key="review.pk">
        {{ review.user.username}}
        <router-link :to="{ name: 'reviewdetail', params: { reviewPk: review.id } }">
          {{ review.title }} 는
          {{ review.content }} 이다.
        </router-link>
      </li>
    </ul>
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