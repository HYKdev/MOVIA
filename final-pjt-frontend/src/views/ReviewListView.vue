<template>
  <div>
    <div class="container">
      <router-link :to="{ name: 'reviewnew' }">
        <button  class="addReview">리뷰 작성</button>
      </router-link>
      <table class="table bg-white">
        <thead class="bg-light">
          <tr>
            <th>제목</th>
            <th class="author">작성자</th>
            <th class="createdTime">작성 시간</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="review in reviews" :key="review.pk">
            <td>
              <router-link :to="{ name: 'reviewdetail', params: { reviewPk: review.id } }" class="title">
                {{ review.title }} 은(는) {{ review.content }} 이다.
              </router-link>
            </td>
            <td class="author">{{ review.user.username }}</td>
            <td class="createdTime">{{ $moment(review.created_at).format('YYYY-MM-DD') }}</td>
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
  .container {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  table {
    padding: 20px;
    margin: 80px;
    vertical-align: middle;
  }

  .author, .createdTime {
    text-align: center;
  }
  
  .addReview {
    background-color: #f3d42a;
    border: none;
    border-radius: 8px;
    padding: 6px 12px;
    margin: 10px;
    color: #212529;
    font-size: 16px;
    font-weight: 500;
    line-height: 1.5;
    cursor: pointer;
    transition: background-color .15s ease-in-out;
    float: right;
    position: absolute;
    top: 18px;
    right: 84px;
  }

  .addReview:hover {
    background-color: rgba(232, 201, 48, 1)
  }

  .title {
    text-decoration: none;
    color: black;
  }
</style>