<template>
  <div>
    <div class="container text-center">
      <div v-for="actor in actors" :key="actor.id" class="actorbox">
        <img :src="actor.main_image" alt="" class="actorimg" />
        <div class="actorinfo d-flex">
          <router-link :to="{ name: 'actordetail', params: { actorPk: actor.id } }">
            <span class="name text-center">{{ actor.name }}</span>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
export default {
  name: 'ActorList',
  computed: {
    ...mapGetters(['actors']),
  },
  methods: {
    ...mapActions(['fetchActors']),
  },
  created() {
    this.fetchActors();
  },
};
</script>

<style scoped>
.actorbox {
  position: relative;
  display: inline-block;
  overflow: hidden;
  margin: 20px;
  /* box-sizing: content-box; */
  box-shadow: 0 25px 45px rgba(0, 0, 0, 0.1);
}
.actorimg {
  width: inherit;
  height: inherit;
  /* border-radius: 15px; */
}

.actorinfo {
  position: absolute;
  /* height: 100%; */
  background-color: black;
  opacity: 0.7;
  bottom: 20px;
  height: 60px;
  width: 120px;
  z-index: 1;
  color: white;
  bottom: -60px;
  text-align: center;
}

.actorbox:hover > .actorinfo {
  transition: all 0.35s;
  bottom: 0;
}

.actorbox:hover > .actorimg {
  transition: all 0.35s;
  opacity: 0.8;
}

a {
  text-decoration: none;
  color: white;
  margin: auto;
}

a:hover {
  text-decoration: none;
  color: white;
}
</style>
