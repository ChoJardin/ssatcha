// api/drf.js
export default {
  URL: 'http://18.209.238.84/',
  ROUTES: {
    // accounts
    signup: 'rest-auth/signup/',
    login: 'rest-auth/login/',
    logout: 'rest-auth/logout/',
    user: 'rest-auth/user/',
    profile: 'profile/',

    // movies
    initial: 'initial_data/',
    genres: 'genres/',
    search: 'search/',

    // board
    review: 'review/',

  }
}