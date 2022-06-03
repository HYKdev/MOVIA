<template>
  <div>
    <div class="container">
      <div class="wrap d-flex justify-content-center row row-cols-2 row-cols-sm-3 row-cols-md-4 row-cols-lg-6">
        <div v-for="(movie, idx) in movies" :key="idx" class="moviebox scale">
          <img :src="movie.image" alt="movie_poster" class="poster" />
          <div class="movieinfo">
            <br />
            <router-link :to="{ name: 'moviedetail', params: { moviePk: movie.id } }">
              <span class="title text-center">{{ movie.title }}</span>
            </router-link>
            <br />
            <span class="genre" v-for="genre in movie.genres" :key="genre.id"> {{ genre.name }} </span>
            <br />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import { mapActions, mapGetters } from 'vuex';
export default {
  name: 'MovieList',
  computed: {
    ...mapGetters(['movies']),
  },
  methods: {
    ...mapActions(['fetchMovies']),
  },
  created() {
    this.fetchMovies();
  },
};
</script>

<style scoped>
.moviebox {
  position: relative;
  width: 203px;
  max-width: 203px;
  height: 290px;
  padding: 20px;
  box-sizing: content-box;
}
.scale {
  transform: scale(1);
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  -o-transform: scale(1);
  transition: all 0.3s ease-in-out;
}
.scale:hover {
  transform: scale(1.2);
  -webkit-transform: scale(1.2);
  -moz-transform: scale(1.2);
  -ms-transform: scale(1.2);
  -o-transform: scale(1.2);
}
.poster {
  /* width:height 1:1.3 */
  /* width: 100%;
  height: auto; */
  width: inherit;
  height: inherit;
  border-radius: 15px;
  /* padding: 5px;
  margin: 5px; */
}

.movieinfo {
  position: absolute;
  width: inherit;
  height: inherit;
  /* height: 100%; */
  background-color: black;
  opacity: 0.7;
  bottom: 20px;
  height: 100px;
  z-index: 1;
  color: white;
  display: none;
  text-align: center;
}

.moviebox:hover > .movieinfo {
  display: block;
  border-radius: 0 0 15px 15px;
}

a {
  text-decoration: none;
  color: white;
}

a:hover {
  text-decoration: none;
  color: white;
}

.title {
  font-size: 1.2rem;
  font-weight: 800;
  margin: auto 0rem;
}

.genre {
  font-size: 1rem;
  margin: auto 0rem;
}
/* #wrap {
    margin:0 auto; 
    text-align: center; 
    width: 300px;
  }
  .MovieInfo {
    display: block; 
    font-size: 12px; 
    color: white;
    opacity: 0; 
    transition: 0.5s all
  }
  #wrap:hover .MovieInfo {
    opacity: 1;
  } */
.container .wrap {
  flex-wrap: wrap;
}
</style>
