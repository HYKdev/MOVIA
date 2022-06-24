<template>
  <div class="container">
    <div class="card">
      <div class="logoBox">
        <img src="@/assets/movia_onlyText.png" alt="moviaLogo">
      </div>
      <div class="loginForm">
        <account-error-list v-if="authError"></account-error-list>
        <form @submit.prevent="login(credentials)">
          <div class="username">
            <label for="username"></label>
            <input v-model="credentials.username" type="text" id="username" placeholder="Username" required />
          </div>

          <div class="password">
            <label for="password"></label>
            <input v-model="credentials.password" type="password" id="password" placeholder="Password" required />
          </div>

          <!-- Submit button -->
          <button type="submit" class="loginBtn">Login</button>
        </form>
        
        <!-- Register buttons -->
        <div class="register">
          <p class="signup">Don't have an account? <router-link :to="{ name: 'signup' }"> Sign up </router-link></p>
          <p class="otherLogin">or Signup/Login with:</p>
          <a href="">
            <div class="naverLogin">
              <img class="naverBtn" src="../assets/btnG_short.png" alt="" />
            </div>
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

.container .card .loginForm {
  padding: 20px;
}

.container .card .loginForm form input {
  width: 350px;
  height: 35px;
  border: 1px solid #ced4da;
  border-radius: 7px;
  padding: 10px;
  margin: 10px;
}

.container .card .loginForm form .loginBtn {
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

.container .card .loginForm form .loginBtn:hover {
    background-color: rgba(232, 201, 48, 1)
  }

.container .card .loginForm .register {
  margin: 15px 0 0 0;
  font-weight: 500;
}

.container .card .loginForm .register .signup {
  margin-bottom: 0px;
  text-align: center;
}

.container .card .loginForm .register .signup a {
  /* text-decoration: none; */
  color: black;
  font-weight: 500;
}

.container .card .loginForm .register .otherLogin {
  margin-bottom: 0px;
  text-align: center;
}

.container .card .loginForm .register a .naverLogin {
  text-align: center;
}

.container .card .loginForm .register a .naverLogin .naverBtn {
  width: 100px;
  margin: 10px;
}
</style>
