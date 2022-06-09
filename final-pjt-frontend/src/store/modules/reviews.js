import axios from 'axios'
import drf from '@/api/drf'
// import router from '@/router'

import _ from 'lodash'
import router from '@/router'

export default {
  state: {
    reviews: [],
    review: [],
  },
  
  getters: {
    reviews: state => state.reviews,
    review: state => state.review,
    isAuthor: (state, getters) => {
      return state.review.user?.username === getters.currentUser.username
    },
    isReview: state => !_.isEmpty(state.review),
  },

  mutations: {
    SET_REVIEWS: (state, reviews) => state.reviews = reviews,
    SET_REVIEW: (state, review) => state.review = review,
  },

  actions: {
    fetchReviews({ commit, getters }) {
      /* 리뷰 목록 받아오기
      GET: reviews URL(token)
      성공 -> 응답으로 받은 게시글 state.reviews에 저장
      실패 -> 에러 메세지 표시
      */
      axios({
        url: drf.community.reviews(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_REVIEWS', res.data))
        .catch(err => console.error(err.response))
    },

    fetchReview({ commit, getters }, reviewPk ) {
      /* 단일 리뷰 받아오기
      GET: review URL (token)
      성공 -> 응답으로 받은 게시글 state.review에 저장
      실패 -> 단순 에러일 때는 에러 메세지 표시
              404 에러일 때는 NotFound404로 이동 */
      axios({
        url: drf.community.review(reviewPk),
        method: 'get',
        headers: getters.authHeader,
       })
         .then(res => commit('SET_REVIEW', res.data))
         .catch(err => {
           console.error(err.response)
           if (err.response.status === 404) {
             router.push({ name: 'NotFound404' })
           }
         })
    },

    createReview({ commit, getters }, review) {
      /* 리뷰 생성 
      POST: reviews URL(리뷰 입력정보, token)
      성공 -> 응답으로 받은 게시글 state.review에 저장
              ReviewDetailView 로 이동
      실패 -> 에러 메시지 표시
      */
      axios({
        url: drf.community.reviews(),
        method: 'post',
        data: review,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_REVIEW', res.data)
          router.push({
            name: 'reviewdetail',
            params: { reviewPk: getters.review.id }
          })
        })
    },

    updateReview({ commit, getters }, { pk, title, content }) {
      /* 리뷰 수정
      PUT: review URL (리뷰 입력정보, token)
      성공 -> 응답으로 받은 게시글 state.review에 저장 
              ReviewDetailView 로 이동
      실패 -> 에러 메시지 표시
      */
      axios({
        url: drf.community.review(pk),
        method: 'put',
        data: { title, content },
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_REVIEW', res.data)
          router.push({
            name: 'reviewdetail',
            params: { reviewPk: getters.review.id }
          })
        })
    },

    deleteReview({ commit, getters }, reviewPk) {
      /* 리뷰 삭제 
      사용자가 확인을 받고 
      DELETE: review URL (token)
      성공 -> state.review 비우기
              ReviewListView로 이동
      실패 -> 에러 메시지 표시
      */
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.community.review(reviewPk),
          method: 'delete',
          headers: getters.authHeader,
        })
          .then(() => {
            commit('SET_REVIEW', {})
            router.push({ name: 'reviewlist'})
          })
          .catch(err => console.log(err.response))
      }
    }
    
  },
}