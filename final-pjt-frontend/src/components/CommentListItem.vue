<template>
  <li class="comment-list-item">
    {{ comment.user.username }}

    <span v-if="!isEditing" class="content">{{ payload.content }}</span>

    <span v-if="isEditing">
      <input type="text" v-model="payload.content" />
      <button @click="onUpdate" clss="">Update</button> |
      <button @click="switchIsEditing" class="">Cancel</button>
    </span>

    <span v-if="currentUser.username === comment.user.username && !isEditing">
      <button @click="switchIsEditing">Edit</button> |
      <button @click="deleteComment(payload)">Delete</button>
    </span>
  </li>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'CommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        reviewPk: this.comment.review,
        commentPk: this.comment.id,
        content: this.comment.content,
      },
    };
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing;
    },
    onUpdate() {
      this.updateComment(this.payload);
      this.isEditing = false;
    },
  },
};
</script>

<style scoped>
.comment-list-item {
  border: 1px solid green;
  list-style: none;
  padding: 20px 0px;
}
</style>
