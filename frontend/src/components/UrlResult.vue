<script setup>
defineProps({
  shortUrl: String
})
</script>

<template>
  <div v-if="shortUrl" class="result">
    <p>Shortened URL:</p>
    <a :href="shortUrl" target="_blank">{{ shortUrl }}</a>
  </div>
</template>

