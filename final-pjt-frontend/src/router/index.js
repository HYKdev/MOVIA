import Vue from 'vue';
import VueRouter from 'vue-router';
import store from '../store';

import HomeView from '@/views/HomeView.vue';
import MovieListView from '@/views/MovieListView.vue';
import MovieDetailView from '@/views/MovieDetailView.vue';

import ActorListView from '@/views/ActorListView.vue';
import ActorDetailView from '@/views/ActorDetailView.vue';

import ReviewListView from '@/views/ReviewListView.vue';
import ReviewDetailView from '@/views/ReviewDetailView.vue';
import ReviewNewView from '@/views/ReviewNewView.vue';
import ReviewEditView from '@/views/ReviewEditView.vue';

import LoginView from '@/views/LoginView.vue';
import LogoutView from '@/views/LogoutView.vue';
import SignupView from '@/views/SignupView.vue';
import ProfileView from '@/views/ProfileView.vue';
import NotFound404 from '../views/NotFound404.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/login',
    name: 'login',
    component: LoginView,
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView,
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView,
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView,
  },
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/movies/movielist',
    name: 'movielist',
    component: MovieListView,
  },
  {
    path: '/movies/moviedetail/:moviePk',
    name: 'moviedetail',
    component: MovieDetailView,
  },
  {
    path: '/movies/actorlist',
    name: 'actorlist',
    component: ActorListView,
  },
  {
    path: '/movies/actordetail/:actorPk',
    name: 'actordetail',
    component: ActorDetailView,
  },
  {
    path: '/reviews',
    name: 'reviewlist',
    component: ReviewListView,
  },
  {
    path: '/reviews/new',
    name: 'reviewnew',
    component: ReviewNewView,
  },
  {
    path: '/reviews/:reviewPk',
    name: 'reviewdetail',
    component: ReviewDetailView,
  },
  {
    path: '/reviews/:reviewPk/edit',
    name: 'reviewedit',
    component: ReviewEditView,
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404,
  },
  {
    path: '*',
    redirect: '/404',
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  // 이전 페이지에서 발생한 에러메시지 삭제
  store.commit('SET_AUTH_ERROR', null);

  const { isLoggedIn } = store.getters;

  const noAuthPages = ['home', 'login', 'signup'];

  const isAuthRequired = !noAuthPages.includes(to.name);

  if (isAuthRequired && !isLoggedIn) {
    alert('로그인이 필요해요!');
    next({ name: 'login' });
  } else {
    next();
  }

  if (!isAuthRequired && isLoggedIn) {
    next({ name: 'home' });
  }
});

export default router;
