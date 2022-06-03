<template>
  <div class="background">
    <br />
    <br />
    <br />
    <div class="container d-flex justify-content-center">
      <div class="signupform">
        <h1>Signup</h1>

        <account-error-list v-if="authError"></account-error-list>

        <form @submit.prevent="signup(credentials)">
          <div class="form-outline mb-4">
            <label for="username"></label>
            <input v-model="credentials.username" type="text" id="username" placeholder="Username" required />
          </div>

          <div class="form-outline mb-4">
            <label for="password1"></label>
            <input v-model="credentials.password1" type="password" id="password1" placeholder="Password" required />
          </div>

          <div class="form-outline mb-4">
            <label for="password2"></label>
            <input
              v-model="credentials.password2"
              type="password"
              id="password2"
              placeholder="Password Confirmation"
              required
            />
          </div>

          <!-- Submit button -->
          <button type="submit" class="signupBtn btn btn-primary btn-block mb-4">Signup</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import AccountErrorList from '@/components/AccountErrorList.vue';

export default {
  name: 'SignupView',
  components: {
    AccountErrorList,
  },
  data() {
    return {
      credentials: {
        username: '',
        password1: '',
        password2: '',
      },
    };
  },
  computed: {
    ...mapGetters(['authError']),
  },
  methods: {
    ...mapActions(['signup']),
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

.signupform {
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

.signupBtn {
  border-radius: 15px;
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
