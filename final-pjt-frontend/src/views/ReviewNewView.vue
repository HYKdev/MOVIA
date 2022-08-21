<template>
  <div>
    <review-form :review="review" action="create"></review-form>
  </div>
</template>

<script>
import ReviewForm from '@/components/ReviewForm.vue'

export default {
  name: 'ReviewNewView',
  components: { ReviewForm },
  data() {
    return {
      review: {
        pk: null,
        title: '',
        content: '',
      }
    }
  }
}
</script>

<style>

</style>