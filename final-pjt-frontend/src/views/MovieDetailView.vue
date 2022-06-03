<template>
  <div class="moviedetail" v-if="movie && movie.image">
    <div
      class="moviedetail_image"
      :style="{
        backgroundImage: `url('${movie.image}')`,
      }"
    ></div>
    <div class="container">
      <div class="moviecontent">
        <div class="movieImage">
          <img :src="movie.image" alt="movie_poster" class="poster" />
          <button @click="likeMovie(moviePk)" class="like btn btn-warning text-white m-2">보고싶어요</button>
          <p>{{ likeCount }}명이 보고싶어요!</p>
        </div>

        <div class="mx-4">
          <div class="movieTitle">
            <h2>{{ movie.title }}</h2>
          </div>

          <div class="movieInfo">
            {{ movie.pubdate }}
            <span v-for="genre in movie.genres" :key="genre.id"> · {{ genre.name }} </span>

            <p class="overview">
              {{ movie.overview }}
            </p>
          </div>
          <iframe class="trailer" width="620" height="350" :src="movie.trailer" frameborder="0" allowfullscreen>
          </iframe>
        </div>
      </div>
      <div class="cast">
        <div>
          <h3>감독</h3>
          <span class="director p-2 m-2" v-for="director in movie.directors" :key="director.id">
            <div><img :src="director.main_image" class="photo" alt="directorPhoto" /></div>
            <div class="text-center my-2">
              {{ director.name }}
            </div>
          </span>
        </div>
        <div>
          <h3>출연</h3>
          <span class="actor p-2 m-2" v-for="actor in movie.actors" :key="actor.id">
            <router-link :to="{ name: 'actordetail', params: { actorPk: actor.id } }">
              <div><img :src="actor.main_image" class="photo" alt="actorPhoto" /></div>
            </router-link>
            <router-link :to="{ name: 'actordetail', params: { actorPk: actor.id } }">
              <div class="actorName text-center my-2">{{ actor.name }}</div>
            </router-link>
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'MovieDetail',
  data() {
    return {
      moviePk: this.$route.params.moviePk,
    };
  },
  computed: {
    ...mapGetters(['movie']),
    likeCount() {
      return this.movie.like_users?.length;
    },
  },
  methods: {
    ...mapActions(['fetchMovie', 'likeMovie']),
  },
  created() {
    this.fetchMovie(this.moviePk);
  },
};
</script>

<style scoped>
.moviedetail {
  height: 100vh;
  margin: 0;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}
/* .moviedetail_image {
  background-size: cover;
  z-index: 999;
} */
.container {
  /* border: 5px solid rgb(23, 23, 23);
  border-radius: 40px; */
  padding-bottom: 50px;
  padding-top: 20px;
}
.container h1 {
  color: white;
  z-index: 1;
}
.moviecontent {
  color: white;
}
.movieImage img {
  height: 600px;
  display: block;
  border-radius: 30px;
}
.container .moviecontent .movieTitle h2 {
  font-weight: bold;
  font-size: 40px;
}
.container .moviecontent .movieInfo {
  font-size: 16px;
  margin-top: 15px;
}

.cast h3 {
  font-weight: bold;
  color: white;
  margin: 20px 10px;
}
.cast span {
  font-size: 20px;
  color: white;
}
.cast div span.director {
  display: inline-block;
  padding: 5px;
}
.cast div span.actor {
  display: inline-block;
  padding: 5px;
}

.cast div span .photo {
  width: 140px;
  height: 140px;
  border-radius: 50%;
  object-fit: cover;
}

a {
  text-decoration: none;
  color: white;
}

a:hover {
  text-decoration: none;
  color: white;
}
.moviedetail {
  position: relative;
}

.moviedetail_image {
  position: fixed;
  background-position: center;
  background-size: cover;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: -1;
}

.moviedetail_image::after {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  min-height: 100vh;
  background-color: rgb(50, 50, 50);
  opacity: 0.8;
  content: '';
  display: block;
  content: '';
  display: block;
}

.moviecontent {
  display: flex;
}

@media screen and (max-width: 991px) {
  .moviecontent {
    display: block;
  }
}
</style>
