<template>
  <div class="container">
    <div class="row d-flex justify-content-start align-items-center py-5">
      <div class="col col-md-9 col-lg-7 col-xl-5">
        <div class="card p-3" style="border-radius: 15px">
          <h1>{{ profile.username }}님의 프로필</h1>
          <hr />
          <div class="review">
            <h2>작성한 글</h2>
            <!-- <span v-for="review in profile.reviews" :key="review.id">
              <router-link :to="{ name: 'review', params: { reviewPk: review.id } }">
                {{ review.title }} 은(는) {{ review.content }} 배우다
              </router-link>
            </span> -->
          </div>
          <hr />
          <div class="likeMovie">
            <h2>보고싶어요 한 영화</h2>
            <span v-for="movie in profile.like_movies" :key="movie.pk">
              <router-link :to="{ name: 'moviedetail', params: { moviePk: movie.id } }">
                <img class="movie_image m-2" :src="movie.image" alt="movie" />
              </router-link>
            </span>
          </div>
          <hr />
          <div>
            <h2>좋아요 한 배우</h2>
            <span v-for="actor in profile.like_actors" :key="actor.pk">
              <router-link :to="{ name: 'actordetail', params: { actorPk: actor.id } }">
                <img class="actor_image m-2" :src="actor.main_image" alt="배우사진">
              </router-link>
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'ProfileView',
  computed: {
    ...mapGetters(['profile']),
  },
  methods: {
    ...mapActions(['fetchProfile']),
  },
  created() {
    const payload = { username: this.$route.params.username };
    this.fetchProfile(payload);
  },
};
</script>

<style scoped>
.card {
  box-shadow: 0 25px 45px rgba(0, 0, 0, 0.1);
  width: 1000px;
}
h1 {
  font-size: 30px;
}
h2 {
  font-size: 25px;
}
ul {
  list-style: none;
}
li {
  float: left;
  margin: 10px;
}
a {
  text-decoration: none;
  color: black;
}
a:hover {
  text-decoration: none;
  color: black;
}
.movie_image {
  width: 100px;
  border-radius: 15px;
  box-shadow: 0 15px 25px rgba(0, 0, 0, 0.1);
}
.actor_image {
  width: 100px;
  border-radius: 50%;
  box-shadow: 0 15px 25px rgba(0, 0, 0, 0.1);
}

</style>
