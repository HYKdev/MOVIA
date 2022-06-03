import axios from 'axios';
import drf from '@/api/drf';
import router from '@/router';

export default {
  state: {
    actors: [],
    actor: [],
    homes: [],
  },

  getters: {
    actors: (state) => state.actors,
    actor: (state) => state.actor,
    homes: (state) => state.homes,
  },

  mutations: {
    SET_ACTORS: (state, actors) => (state.actors = actors),
    SET_ACTOR: (state, actor) => (state.actor = actor),
    SET_HOMES: (state, homes) => (state.homes = homes),
  },

  actions: {
    fetchHomes({ commit, getters }) {
      /* 영화 추천 리스트 받기
    GET: actors URL
    성공 -> 받은 배우,영화 리스트 state.에 저장
    실패 -> 에러 메세지 표시
    */
      axios({
        url: drf.movies.homes(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then((res) => commit('SET_HOMES', res.data))
        .catch((err) => console.error(err.response));
    },

    fetchActors({ commit, getters }) {
      /* 배우 리스트 받기
    GET: actors URL
    성공 -> 받은 배우 리스트 state.actors에 저장
    실패 -> 에러 메세지 표시
    */
      axios({
        url: drf.movies.actors(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then((res) => commit('SET_ACTORS', res.data))
        .catch((err) => console.error(err.response));
    },

    fetchActor({ commit, getters }, actorPk) {
      /* 단일 배우 받기
    GET:  movies URL? 
    성공 -> 받은 배우  state.actor에 저장
    실패 -> 단순 에러: 에러 메세지 표시
            404 에러: NotFound404로 이동
    */
      axios({
        url: drf.movies.actor(actorPk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then((res) => commit('SET_ACTOR', res.data))
        .catch((err) => {
          console.error(err.response);
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' });
          }
        });
    },

    likeActor({ commit, getters }, actorPk) {
      /* 좋아요!
    POST: likeActor URL(token)
    성공 -> state. actor 갱신
    실패 -> 에러 메세지 표시
      */
      axios({
        url: drf.movies.likeActor(actorPk),
        method: 'post',
        headers: getters.authHeader,
      })
        .then((res) => commit('SET_ACTOR', res.data))
        .catch((err) => console.error(err.response));
    },
  },
};
