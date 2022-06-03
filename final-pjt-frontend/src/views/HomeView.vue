<template>
  <div class="container p-3">
    <h1>오늘의 추천 배우</h1>
    <div class="d-flex justify-content-center mb-5">
      <span class="actorRecommend text-center" v-for="home in homes" :key="home.id">
        <div><img :src="home.main_image" alt="actor" class="actorPhoto p-2" /></div>
        <div class="actorName text-center">{{ home.name }}</div>
      </span>
    </div>
    <h1>이 배우들이 출연한 작품 어때요?</h1>
    <div class="d-flex justify-content-center my-3">
      <span class="movieRecommend" v-for="home in homes" :key="home.id">
        <div>
          <router-link :to="{ name: 'moviedetail', params: { moviePk: home.movies[0].id } }">
            <img :src="home.movies[0].image" alt="poster" class="moviePhoto p-2" />
          </router-link>
        </div>
      </span>
    </div>

    <!-- <div v-for="home in homes" :key="home.id">
      <div>{{ home.name }}</div>
      <img :src="home.main_image" alt="" />
      <div>{{ home.movies[0].title }}</div>
      <img :src="home.movies[0].image" />
    </div> -->
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
export default {
  name: 'HomeView',
  computed: {
    ...mapGetters(['homes']),
  },
  methods: {
    ...mapActions(['fetchHomes']),
  },
  created() {
    this.fetchHomes();
  },
};
</script>

<style scoped>
.actorRecommend {
  display: inline-block;
}
.actorPhoto {
  width: 200px;
  border-radius: 100px;
  object-fit: cover;
  margin: 0 20px 0px 20px;
}
.movieRecommend {
  display: inline-block;
}
.moviePhoto {
  width: 250px;
  object-fit: cover;
  border-radius: 15px;
}
h1 {
  margin: 10px 10px;
  text-align: center;
  font-size: 38px;
  font-weight: 800;
}
.actorName {
  font-size: 30px;
  font-weight: 700;
}
</style>
