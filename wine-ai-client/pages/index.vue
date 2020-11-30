<template>
  <v-layout column>
    <h3 class="my-5 ml-3">ワインの情報を教えてください。</h3>
    <form-card v-for="i in 11" :key="i" />
    <v-btn color="#BB86FC" @click="submit">POST</v-btn>
    <v-btn color="#BB86FC" @click="get">GET</v-btn>
    <v-btn color="#BB86FC" @click="analize">診断</v-btn>
  </v-layout>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import axios from 'axios'

@Component({
  components: {
    FormCard: () => import('~/components/Form/FormCard.vue'),
  },
})
export default class extends Vue {
  attribute = {
    // id: 1,
    japanese_title: 'クエン酸',
    english_title: 'acid',
    max_value: 0.2,
    min_value: 0.2,
    step: 0.1,
  }
  input = [
    {
      id: 1,
      value: 0.2
    },
    {
      id: 2,
      value: 0.8
    },
    {
      id: 3,
      value: 0.2
    },
    {
      id: 4,
      value: 0.8
    },
    {
      id: 5,
      value: 0.2
    },
    {
      id: 6,
      value: 0.8
    },
    {
      id: 7,
      value: 0.2
    },
    {
      id: 8,
      value: 0.8
    },
    {
      id: 9,
      value: 0.2
    },
    {
      id: 10,
      value: 0.8
    },
    {
      id: 11,
      value: 0.8
    },
    // {
    //   id: 12,
    //   value: 0.2
    // },
  ]
  async get() {
    await axios
      .get('http://127.0.0.1:8000/api/wine-attributes')
      .then((res) => console.log(res))
      .catch((e) => console.error(e))
  }
  async submit() {
    await axios
      .post('http://127.0.0.1:8000/api/wine-attributes', this.attribute)
      .then((res) => console.log(res))
      .catch((e) => console.error(e))
  }
  async analize() {
    await axios
      .post('http://127.0.0.1:8000/api/prediction', this.input)
      .then((res) => console.log(res))
      .catch((e) => console.error(e))
  }
}
</script>

<style scoped></style>
