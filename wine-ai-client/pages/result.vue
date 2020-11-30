<template>
  <v-layout column>
    <h3 class="my-5 ml-3">診断結果</h3>
    <result-chart />
    <result-list />
    <v-btn color="#BB86FC" class="mt-3">もう一度診断する</v-btn>
  </v-layout>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'

@Component({
  components: {
    ResultChart: () => import('~/components/Result/ResultChart.vue'),
    ResultList: () => import('~/components/Result/ResultList.vue'),
  },
})
export default class extends Vue {}
</script>

<style scoped></style>
