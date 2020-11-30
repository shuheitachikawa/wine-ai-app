<template>
  <v-card color="#121212">
    <v-card-title>クエン酸</v-card-title>
    <v-card-subtitle>1/11</v-card-subtitle>
    <v-slider
      thumb-label="always"
      color="#BB86FC"
      class="px-5 pt-8 pb-3"
      :max=100
      :min=0
      :step=1
    ></v-slider>
  </v-card>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'

@Component
export default class extends Vue {}
</script>

<style scoped></style>
