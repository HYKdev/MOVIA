import Vue from 'vue'
import Vuex from 'vuex'

import movies from './modules/movies'
import actors from './modules/actors'
import reviews from './modules/reviews'
import accounts from './modules/accounts'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: { movies, actors, reviews, accounts}
})