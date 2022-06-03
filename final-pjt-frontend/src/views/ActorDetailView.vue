<template>
  <div class="container p-4">
    <p class="actorname">{{ actor.name }}</p>
    <div class="actorInfo">
      <button @click="likeActor(actorPk)" class="like btn btn-warning my-3">좋아요</button>
      <p class="actorlike">{{ likeCount }}명이 {{ actor.name }} 배우를 좋아하고 있어요!</p>
    </div>
    

    <div class="movieStills">
      <h2 class="text-center p-4">Movie stills</h2>
      <div class="slid-er">
        <div class="slides" id="slides" ref="target">
          <div class="slide" v-for="(image, idx) in actor.images" :key="idx">
            <div class="slide-content">
              <img :src="image.url" loading="lazy" />
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <div class="moviecastingtext">{{actor.name}} 출연작</div>
    <div class="container">
      <div class="wrap d-flex justify-content-center row row-cols-2 row-cols-sm-3 row-cols-md-4 row-cols-lg-6">
        <div v-for="(movie, idx) in actor.movies" :key="idx" class="moviebox scale">
          <img :src="movie.image" alt="movie_poster" class="poster" />
        </div>
      </div>
    </div>

  


  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'ActorDetail',
  data() {
    return {
      actorPk: this.$route.params.actorPk,
      xOffset: this.xOffset,
    };
  },
  computed: {
    ...mapGetters(['actor']),
    likeCount() {
      return this.actor.like_users?.length;
    },
  },
  methods: {
    ...mapActions(['fetchActor', 'likeActor']),
  },
  created() {
    this.fetchActor(this.actorPk);
  },
  mounted() {
    let xOffset = 0;
    const slides = this.$refs.target;
    // const totalWidth = 3000;

    const translate = () => {
      let offsetIncrementor = 0.2;
      if (xOffset >= 2050) xOffset = 0;
      else xOffset = xOffset + offsetIncrementor;
      // xOffset = (xOffset + 0.2) % totalWidth;
      slides.style.transform = 'translateX(-' + xOffset + 'px)';
    };
    setInterval(translate, 0);
  },
};
</script>

<style scoped>
.slide-content {
  margin: 8px;
  width: 300px;
  height: 190px;
  background-color: lightgray;
  border-radius: 12px;
  overflow: hidden;
  position: relative;
}
img {
  width: 100%;
}
.slid-er {
  height: 256px; /* slide-content height + 2*margin */
  margin: auto;
  overflow: hidden;
  width: 100%;
}
.slid-er .slides {
  display: flex;
}
.slid-er .slide {
  width: 366px; /* slide-content width + margin */
}
.actorname {
  font-size: 30px;
  font-weight: 700;
}
.actorlike {
  font-size: 20px;
  padding: 30px 0;
}
.poster {
  border-radius: 30px;
  margin: 15px;
  padding: 15px;
}
.moviecastingtext{
  font-size: 25px;
  font-weight: 800;
  text-align: center;
}
</style>
