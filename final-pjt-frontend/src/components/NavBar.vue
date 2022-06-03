<template>
  <nav class="navbar navbar-expand-lg p-2">
    <div class="d-flex justify-content-between align-item-center collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav">
        <router-link :to="{ name: 'home' }" class="nav-item nav-link font-weight-bold mt-2"
          ><img src="@/assets/movia_onlyText.png" alt="moviaLogo"
        /></router-link>
        <router-link :to="{ name: 'movielist' }" class="nav-item nav-link font-weight-bold mt-2">Movie</router-link>
        <router-link :to="{ name: 'actorlist' }" class="nav-item nav-link font-weight-bold mt-2">Actor</router-link>
        <router-link :to="{ name: 'reviewlist' }" class="nav-item nav-link font-weight-bold mt-2">Review</router-link>
      </div>
      <div>
        <span>
          <span v-if="isLoggedIn" class="user p-1">
            <router-link :to="{ name: 'profile', params: { username } }">{{ currentUser.username }}</router-link
            >님</span
          >
        </span>
        <span v-if="!isLoggedIn"
          ><router-link :to="{ name: 'login' }" class="account font-weight-bold m-3 p-2">Login</router-link></span
        >
        <span v-if="isLoggedIn">
          <router-link :to="{ name: 'logout' }" class="account font-weight-bold m-3 p-2">Logout</router-link>
        </span>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'NavBar',
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser']),
    username() {
      return this.currentUser.username ? this.currentUser.username : 'guest';
    },
  },
};
</script>

<style scoped>
.navbar {
  background-color: rgb(0, 0, 0);
}
img {
  width: 155px;
}
.nav-item {
  text-decoration: none;
  color: white;
  font-size: 23px;
}
.nav-item:hover {
  text-decoration: none;
  color: white;
}
.user {
  color: white;
  font-size: 20px;
}
.account {
  text-decoration: none;
  color: white;
  font-size: 23px;
}
.account:hover {
  text-decoration: none;
  color: white;
}
a {
  text-decoration: none;
  color: white;
}
a:hover {
  text-decoration: none;
  color: white;
}
</style>
