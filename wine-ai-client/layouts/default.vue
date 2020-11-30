<template>
  <v-app>
    <v-app-bar app fixed color="#121212">
      <v-toolbar-title>そのワインが美味しい確率</v-toolbar-title>
    </v-app-bar>
    <v-main>
      <v-container fluid>
        <nuxt />
      </v-container>
    </v-main>
    <v-footer class="mt-10">
      <span>bubekiti</span>
    </v-footer>
  </v-app>
</template>
<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'

@Component
export default class extends Vue {}
</script>

<style scoped></style>
