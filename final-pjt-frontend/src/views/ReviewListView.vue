<template>
  <div>
    <div class="container my-5 p-5">
      <router-link :to="{ name: 'reviewnew' }">
        <button class="addReview m-2">Add Review</button>
      </router-link>
      <table class="table align-middle mb-0 bg-white">
        <thead class="bg-light p-2">
          <tr>
            <th>제목</th>
            <th class="text-center">작성자</th>
            <th class="text-center">작성 시간</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="review in reviews" :key="review.pk">
            <td>
              <router-link :to="{ name: 'reviewdetail', params: { reviewPk: review.id } }">
                {{ review.title }} 은(는) {{ review.content }} 이다.
              </router-link>
            </td>
            <td class="text-center">{{ review.user.username }}</td>
            <td class="text-center">{{ $moment(review.created_at).format('YYYY-MM-DD') }}</td>
          </tr>
        </tbody>
      </table>
    </div>
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

<style scoped>
  .addReview {
    background-color: #f3d42a;
    color: white;
    padding: 12px;
    border: none;
    border-radius: 4px;
  }
</style>