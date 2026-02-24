<script setup>
import { ref, onMounted } from 'vue'
import { fetchAllUrls } from '@/service/api'
import UrlForm from '@/components/UrlForm.vue'
import UrlResult from '@/components/UrlResult.vue'
import UrlList from '@/components/UrlList.vue'

const shortUrl = ref('')
const urls = ref({})

async function refresh() {
  urls.value = await fetchAllUrls()
}

function onShortened(link) {
  shortUrl.value = link
  refresh()
}

onMounted(refresh)
</script>

<template>
  <div class="container">
    <h1>URL Shortener</h1>
    <UrlForm @shortened="onShortened" />
    <UrlResult :shortUrl="shortUrl" />
    <UrlList :urls="urls" @deleted="refresh" />
  </div>
</template>
