const HOST = 'http://127.0.0.1:8000/api/v1/';

const ACCOUNTS = 'accounts/';
const MOVIES = 'movies/';
const COMMUNITY = 'community/';

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: (username) => HOST + ACCOUNTS + 'profile/' + username,
  },
  movies: {
    homes: () => HOST + MOVIES,
    // /movies/movielist
    movies: () => HOST + MOVIES + 'movielist/',
    // /movies/moviedetial/movie_name
    movie: (moviePk) => HOST + MOVIES + 'moviedetail/' + `${moviePk}/`,
    likeMovie: (moviePk) => HOST + MOVIES + `${moviePk}/` + 'movielike/',
    actors: () => HOST + MOVIES + 'actorlist/',
    actor: (actorPk) => HOST + MOVIES + 'actordetail/' + `${actorPk}/`,
    actorWordCloud: (actorPk) => HOST + MOVIES + 'actordetail/' + `${actorPk}/` + 'wordcloud/',
    likeActor: (actorPk) => HOST + MOVIES + `${actorPk}/` + 'actorlike/',
  },
  community: {
    reviews: () => HOST + COMMUNITY,
    review: (reviewPk) => HOST + COMMUNITY + `${reviewPk}/`,
    comments: (reviewPk) => HOST + COMMUNITY + `${reviewPk}/` + 'comments/',
    comment: (reviewPk, commentPk) => HOST + COMMUNITY + `${reviewPk}/` + 'comments/' + `${commentPk}/`,
  },
};
