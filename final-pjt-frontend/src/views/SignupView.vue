<template>
  <div class="container">
    <div class="card">
      <div class="logoBox">
        <img src="@/assets/movia_onlyText.png" alt="moviaLogo">
      </div>
      <div class="signupForm">
        <form @submit.prevent="signup(credentials)">
          <div class="username">
            <label for="username"></label>
            <input v-model="credentials.username" type="text" id="username" placeholder="Username" required />
            <div v-if="authError">
              <div v-if="authError.username">
                <span v-for="error in authError.username" :key="error.id">
                  <p class="error">{{ error }}</p>
                </span>
              </div>
            </div>
          </div>

          <div class="password">
            <label for="password"></label>
            <input v-model="credentials.password1" type="password" id="password1" placeholder="Password" required />
            <div v-if="authError">
              <div v-if="authError.password1">
                <p class="error">{{ authError.password1[0] }}</p>
              </div>
            </div>
          </div>

          <div class="password2">
            <label for="password2"></label>
            <input v-model="credentials.password2" type="password" id="password2" placeholder="Password Confirmation" required />
            <div v-if="authError">
              <div v-if="authError.non_field_errors">
                <p class="error">비밀번호가 일치하지 않습니다.</p>
              </div>
            </div>
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


export default {
  name: 'SignupView',
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
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

.container .card {
  width: 500px;
  height: 650px;
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

.container .card .signupForm {
  padding: 40px;
}

.container .card .signupForm h1 {
  color: black;
  font-size: 35px;
  font-weight: 600;
  text-align: center;
  margin-bottom: 15px;
}

 .accountError {
  font-size: 15px;
}

.container .card .signupForm form input {
  width: 400px;
  height: 40px;
  border: 1px solid #ced4da;
  border-radius: 7px;
  padding: 10px;
  margin: 12px;
}

.container .card .signupForm form .registerBtn {
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

.container .card .signupForm form .registerBtn:hover {
    background-color: rgba(232, 201, 48, 1)
  }

.error {
  color: red;
  font-size: 15px;
  margin: 0 0 10px 12px;
}

@media  screen and (max-width:480px) {
  .container .card {
    min-width: 435px;
  }
}
</style>
