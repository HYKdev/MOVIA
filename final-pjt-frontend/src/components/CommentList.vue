<template>
  <div class="comment-list">
    <h2>Recent Comments</h2>
    <ul>
      <comment-list-item v-for="comment in comments" :comment="comment" :key="comment.id"> </comment-list-item>
    </ul>

    <comment-list-form></comment-list-form>
  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem.vue';
import CommentListForm from '@/components/CommentListForm.vue';
// import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentList',
  components: { CommentListForm, CommentListItem },
  props: { comments: Array },
};
</script>

<style>
.comment-list {
  border: 1px solid blue;
  padding-left: 0px;
}
ul {
  padding: 0;
}
</style>
