<template>
  <div class="container">
    <div class="card">
      <div class="logoBox">
        <img src="@/assets/movia_onlyText.png" alt="moviaLogo">
      </div>
      <div class="loginForm">
        <!-- <account-error-list v-if="authError"></account-error-list> -->
        <form @submit.prevent="login(credentials)">
          <div class="username">
            <label for="username"></label>
            <input v-model="credentials.username" type="text" id="username" placeholder="Username" required />
          </div>

          <div class="password">
            <label for="password"></label>
            <input v-model="credentials.password" type="password" id="password" placeholder="Password" required />
            <div v-if="authError">
              <div v-if="authError.non_field_errors">
                <span v-for="error in authError.non_field_errors" :key="error.id">
                  <p class="error">아이디 또는 비밀번호를 잘못 입력 하셨습니다. <br>입력하신 내용을 다시 확인해주세요.</p>
                </span>
              </div>
            </div>
          </div>

          <!-- Submit button -->
          <button type="submit" class="loginBtn">Login</button>
        </form>
        
        <!-- Register buttons -->
        <p class="signup">Don't have an account? <router-link :to="{ name: 'signup' }"> Sign up </router-link></p>        
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'LoginView',
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
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
  }

.container .card {
  width: 500px;
  height: 600px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  border-radius: 20px;
  box-shadow: 0 25px 40px rgba(0, 0, 0, 0.2);
}

.container .card .logoBox {
  width: 100%;
  height: 100%;
  background: black;
  border-radius: 20px 20px 0 0;
  text-align: center;
  line-height: 300px;
}

.container .card .logoBox img {
  width: 100%;
  vertical-align: middle;
}

.container .card .loginForm {
  padding: 40px;
}

.container .card .loginForm form input {
  width: 400px;
  height: 40px;
  border: 1px solid #ced4da;
  border-radius: 7px;
  padding: 10px;
  margin: 10px;
}

.container .card .loginForm form .loginBtn {
  width: 400px;
  height: 40px;
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

.error {
  color: red;
  font-size: 15px;
  margin: 0 0 10px 12px;
}
.container .card .loginForm .register {
  margin: 15px 0 0 0;
  font-weight: 500;
}

.container .card .loginForm .signup {
  margin-bottom: 0px;
  text-align: center;
}

.container .card .loginForm .signup a {
  color: black;
  font-weight: 500;
  font-size: 20px;
}

@media  screen and (max-width:480px) {
  .container .card {
    min-width: 435px;
  }
}
</style>
