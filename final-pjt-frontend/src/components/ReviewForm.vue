<template>
  <form @submit.prevent="onSubmit">
    <span class="title">
      <label for="title"></label>
      <input v-model="newReview.title" type="text" id="title"> 배우는
    </span>
    <span class="content">
      <label for="content"></label>
      <input v-model="newReview.content" type="text" id="content" cols="30" rows="1"> 이다.
    </span>
    <div>
      <button class="btn">{{ action }}</button>
    </div>
  </form>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'ReviewForm',
  props: {
    review: Object,
    action: String,
  },
  data() {
    return {
      newReview: {
        title: this.review.title,
        content: this.review.content,
      }
    }
  },

  methods: {
    ...mapActions(['createReview', 'updateReview']),
    onSubmit() {
      if (this.action === 'create') {
        this.createReview(this.newReview)
      } else if (this.action === 'update') {
        const payload = {
          pk: this.review.id,
          ...this.newReview,
        }
        this.updateReview(payload)
      }
    }
  }
}
</script>

<style scoped>
  form {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 30px;
  }

  form span {
    margin: 5px;
  }

  form input {
    border: 1px solid #ced4da;
    border-radius: 15px;
    padding: 5px;
  }

  form .title input {
    width: 150px;
    height: 36px;
  }

  form .content input {
    width: 400px;
    height: 36px;
  }

  .btn {
    background-color: #f3d42a;
    border: none;
    border-radius: 15px;
    padding: 6px 12px;
    margin: 0px 0px 0px 20px;
    color: #212529;
    font-size: 16px;
    font-weight: 500;
    line-height: 1.5;
    cursor: pointer;
    transition: background-color .15s ease-in-out;
  }

  .btn:hover {
    background-color: rgba(232, 201, 48, 1)
  }
  
</style>