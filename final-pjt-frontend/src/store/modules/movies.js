import axios from 'axios';
import drf from '@/api/drf';
import router from '@/router';

export default {
  state: {
    movies: [],
    movie: [],
  },

  getters: {
    movies: (state) => state.movies,
    movie: (state) => state.movie,
  },

  mutations: {
    SET_MOVIES: (state, movies) => (state.movies = movies),
    SET_MOVIE: (state, movie) => (state.movie = movie),
  },

  actions: {
    fetchMovies({ commit, getters }) {
      /* 영화 리스트 받기
    GET:  movies URL? 
    성공 -> 받은 영화 리스트 state.movies에 저장
    실패 -> 에러 메세지 표시
    */
      axios({
        url: drf.movies.movies(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then((res) => commit('SET_MOVIES', res.data))
        .catch((err) => console.error(err.response));
    },

    fetchMovie({ commit, getters }, moviePk) {
      /* 단일 영화 받기
    GET:  movies URL? 
    성공 -> 받은 영화  state.movie에 저장
    실패 -> 단순 에러: 에러 메세지 표시
            404 에러: NotFound404로 이동
    */
      axios({
        url: drf.movies.movie(moviePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then((res) => commit('SET_MOVIE', res.data))
        .catch((err) => {
          console.error(err.response);
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' });
          }
        });
    },

    likeMovie({ commit, getters }, moviePk) {
      /* 보고싶어요(좋아요!)
    POST: likeMovie URL(token)
    성공 -> state.movie 갱신
    실패 -> 에러 메세지 표시
      */
      axios({
        url: drf.movies.likeMovie(moviePk),
        method: 'post',
        headers: getters.authHeader,
      })
        .then((res) => commit('SET_MOVIE', res.data))
        .catch((err) => console.error(err.response));
    },
  },
};
