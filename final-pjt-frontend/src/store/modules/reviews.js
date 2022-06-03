import axios from 'axios';
import drf from '@/api/drf';
import router from '@/router';

import _ from 'lodash';
export default {
  state: {
    reviews: [],
    review: [],
  },

  getters: {
    reviews: (state) => state.reviews,
    review: (state) => state.review,
    isAuthor: (state, getters) => {
      return state.review.user?.username === getters.currentUser.username;
    },
    isReview: (state) => !_.isEmpty(state.review),
  },

  mutations: {
    SET_REVIEWS: (state, reviews) => (state.reviews = reviews),
    SET_REVIEW: (state, review) => (state.review = review),
    SET_REVIEW_COMMENTS: (state, comments) => (state.review.comments = comments),
  },

  actions: {
    fetchReviews({ commit, getters }) {
      /* 리뷰 목록 받아오기
      GET: reviews URL (token)
      성공 -> 응답으로 받은 기뷰들 state.reviews에 저장
      실패 -> 에러 메세지 표시
      */
      axios({
        url: drf.community.reviews(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then((res) => commit('SET_REVIEWS', res.data))
        .catch((err) => console.error(err.response));
    },

    fetchReview({ commit, getters }, reviewPk) {
      /* 단일 리뷰 받아오기
      GET: review URL (token)
      성공 -> 응답으로 받은 리뷰 state.review에 저장
      실패 -> 단순 에러일 때는 에러 메시지 표시,
              404 에러일 때는 NotFound404 로 이동
      */
      axios({
        url: drf.community.review(reviewPk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then((res) => commit('SET_REVIEW', res.data))
        .catch((err) => {
          console.error(err.response);
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' });
          }
        });
    },

    createReview({ commit, getters }, review) {
      /* 리뷰 생성
      POST: reviews URL(리뷰 입력정보, token)
      성공 -> 응답으로 받은 리뷰 state.review에 저장
              ReviewDetailView로 이동
      실패 -> 에러 메세지 표시
      */
      axios({
        url: drf.community.reviews(),
        method: 'post',
        data: review,
        headers: getters.authHeader,
      }).then((res) => {
        commit('SET_REVIEW', res.data);
        router.push({
          name: 'reviewdetail',
          params: { reviewPk: getters.review.id },
        });
      });
    },
    updateReview({ commit, getters }, { pk, title, content }) {
      /* 리뷰 수정
      POST: reviews URL(리뷰 입력정보, token)
      성공 -> 응답으로 받은 리뷰 state.review에 저장
              ReviewDetailView로 이동
      실패 -> 에러 메세지 표시
      */
      axios({
        url: drf.community.review(pk),
        method: 'put',
        data: { title, content },
        headers: getters.authHeader,
      }).then((res) => {
        commit('SET_REVIEW', res.data);
        router.push({
          name: 'reviewdetail',
          params: { reviewPk: getters.review.id },
        });
      });
    },

    deleteReview({ commit, getters }, reviewPk) {
      /* 리뷰 삭제
      사용자가 확인 받고
      DELETE: review URL(token)
      성공 -> 응답으로 받은 리뷰를 state.review에 저장
      ReviewDetailView 로 이동
      실패 -> 에러 메세지 표시
       */
      if (confirm('삭제하시겠습니까?')) {
        axios({
          url: drf.community.review(reviewPk),
          method: 'delete',
          headers: getters.authHeader,
        })
          .then(() => {
            commit('SET_REVIEW', {});
            router.push({ name: 'reviewlist' });
          })
          .catnc((err) => console.error(err.response));
      }
    },

    createComment({ commit, getters }, { reviewPk, content }) {
      /* 댓글 생성
      POST: comments URL(댓글 입력 정보, token)
      성공 -> 응답으로 state.review의 comments 갱신
      실패 -> 에러 메시지 표시 
      */
      const comment = { content };

      axios({
        url: drf.community.comments(reviewPk),
        method: 'post',
        data: comment,
        headers: getters.authHeader,
      })
        .then((res) => {
          commit('SET_REVIEW_COMMENTS', res.data);
        })
        .catch((err) => console.error(err.response));
    },

    updateComment({ commit, getters }, { reviewPk, commentPk, content }) {
      /* 댓글 수정
      POST: comments URL(댓글 입력 정보, token)
      성공 -> 응답으로 state.review의 comments 갱신
      실패 -> 에러 메시지 표시 
      */
      const comment = { content };

      axios({
        url: drf.community.comments(reviewPk, commentPk),
        method: 'put',
        data: comment,
        headers: getters.authHeader,
      })
        .then((res) => {
          commit('SET_REVIEW_COMMENTS', res.data);
        })
        .catch((err) => console.error(err.response));
    },

    deleteComment({ commit, getters }, { reviewPk, commentPk }) {
      /* 댓글 삭제
      사용자가 확인 받고
      DELETE: comment URL(token)
      성공 -> 응답으로 state.review의 comments 갱신
      실패 -> 에러 메세지 표시
       */
      if (confirm('삭제하시겠습니까?')) {
        axios({
          url: drf.community.comment(reviewPk, commentPk),
          method: 'delete',
          data: {},
          headers: getters.authHeader,
        })
          .then((res) => {
            commit('SET_REVIEW_COMMENTS', res.data);
          })
          .catch((err) => console.error(err.response));
      }
    },
  },
};
