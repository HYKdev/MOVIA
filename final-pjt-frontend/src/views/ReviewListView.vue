<template>
  <div class="container my-5 p-5">
    <router-link :to="{ name: 'reviewnew' }">
      <button class="btn btn-warning m-1">Add Review</button>
    </router-link>
    <div class="d-flex jusify-content-center">
      <table class="table align-middle mb-0 bg-white">
        <thead class="bg-light p-2">
          <tr>
            <th>제목</th>
            <th class="text-center">작성자</th>
            <th class="text-center">작성 시간</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="review in reviews" :key="review.id">
            <td>
              <router-link :to="{ name: 'reviewdetail', params: { reviewPk: review.id } }">
                이제훈은 {{ review.title }} 배우다
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
import { mapActions, mapGetters } from 'vuex';
export default {
  name: 'ReviewList',
  computed: {
    ...mapGetters(['reviews']),
  },
  methods: {
    ...mapActions(['fetchReviews']),
  },
  created() {
    this.fetchReviews();
  },
};
</script>

<style scoped>
a {
  text-decoration: none;
  color: black;
}
a:hover {
  text-decoration: none;
  color: black;
}
</style>

