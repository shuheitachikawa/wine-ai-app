<template>
  <v-list two-line>
    <div v-for="j in 11" :key="j" >
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title>クエン酸</v-list-item-title>
          <v-list-item-subtitle>acid</v-list-item-subtitle>
        </v-list-item-content>
        <v-list-item-content>
          <v-list-item-action-text>0.1</v-list-item-action-text>
        </v-list-item-content>
      </v-list-item>
    </div>
  </v-list>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
@Component
export default class extends Vue {}
</script>

<style scoped></style>
