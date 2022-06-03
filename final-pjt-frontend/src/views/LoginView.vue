<template>
  <div class="background">
    <br />
    <br />
    <br />
    <div class="container d-flex justify-content-center">
      <div class="loginform">
        <h1>Login</h1>

        <account-error-list v-if="authError"></account-error-list>

        <form @submit.prevent="login(credentials)">
          <div class="form-outline mb-4">
            <label for="username"></label>
            <input v-model="credentials.username" type="text" id="username" placeholder="Username" required />
          </div>

          <div class="form-outline mb-4">
            <label for="password"></label>
            <input v-model="credentials.password" type="password" id="password" placeholder="Password" required />
          </div>

          <!-- Submit button -->
          <button type="submit" class="loginBtn btn btn-primary btn-block mb-4">Login</button>
        </form>
        <hr />

        <!-- Register buttons -->
        <div class="text-center">
          <a href="#!">Forgot password?</a>
          <p>Don't havea an account? <router-link :to="{ name: 'signup' }"> Sign up </router-link></p>
          <p>or Signup/Login with:</p>
          <a href="">
            <img class="naverBtn" src="../assets/btnG_short.png" alt="" />
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import AccountErrorList from '@/components/AccountErrorList.vue';

export default {
  name: 'LoginView',
  components: {
    AccountErrorList,
  },
  data() {
    return {
      credentials: {
        username: '',
        password: '',
      },
    };
  },
  computed: {
    ...mapGetters(['authError']),
  },
  methods: {
    ...mapActions(['login']),
  },
};
</script>

<style scoped>
.container {
  width: 550px;
  padding: 50px;
  border: 1px solid black;
  border-radius: 5%;
}

.loginform {
  position: relative;
  width: 100%;
  height: 100%;
}

h1 {
  color: black;
  font-size: 35px;
  font-weight: 500px;
  margin-bottom: 40px;
  text-align: center;
}

.form-outline input {
  width: 100%;
  height: 40px;
  padding: 20px;
  border-radius: 15px;
  border: none;
  border: 1px solid rgba(74, 74, 74, 0.5);
}

.loginBtn {
  border-radius: 15px;
}

.naverBtn {
  width: 100px;
}

hr {
  height: 2px;
  color: black;
}
/* .background {
  background-color: white;
  height: 100vh;
} */
</style>
