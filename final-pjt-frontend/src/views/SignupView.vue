<template>
  <div class="container">
    <div class="card">
      <div class="logoBox">
        <img src="@/assets/movia_onlyText.png" alt="moviaLogo">
      </div>
      <div class="signupForm">
        <h1>Sign up</h1>
        <account-error-list v-if="authError"></account-error-list>
        <form @submit.prevent="signup(credentials)">
          <div class="username">
            <label for="username"></label>
            <input v-model="credentials.username" type="text" id="username" placeholder="Username" required />
          </div>

          <div class="password">
            <label for="password"></label>
            <input v-model="credentials.password1" type="password" id="password1" placeholder="Password" required />
          </div>

          <div class="password2">
            <label for="password2"></label>
            <input v-model="credentials.password2" type="password" id="password2" placeholder="Password Confirmation" required />
          </div>

          <!-- Submit button -->
          <button type="submit" class="registerBtn">Register</button>
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
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

.container .card {
  width: 450px;
  height: 600px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  border-radius: 20px;
  box-shadow: 0 25px 40px rgba(0, 0, 0, 0.2);
}

.container .card .logoBox {
  width: 450px;
  height: 250px;
  background: black;
  border-radius: 20px 20px 0 0;
}

.container .card .logoBox img {
  width: 400px;
  position: absolute;
  top: 70px;
  left: 25px;
}

.container .card .signupForm {
  padding: 20px;
}

.container .card .signupForm h1 {
  color: black;
  font-size: 35px;
  font-weight: 600;
  text-align: center;
  margin-bottom: 15px;
}

.container .card .signupForm form input {
  width: 350px;
  height: 35px;
  border: 1px solid #ced4da;
  border-radius: 7px;
  padding: 10px;
  margin: 12px;
}

.container .card .signupForm form .registerBtn {
  width: 350px;
  height: 35px;
  background-color: #f3d42a;
  border: none;
  border-radius: 7px;
  margin: 10px 10px 20px 10px;
  font-size: 16px;
  font-weight: 500;
  line-height: 1.5;
  cursor: pointer;
  transition: background-color .15s ease-in-out;
}

.container .card .signupForm form .registerBtn:hover {
    background-color: rgba(232, 201, 48, 1)
  }
</style>
