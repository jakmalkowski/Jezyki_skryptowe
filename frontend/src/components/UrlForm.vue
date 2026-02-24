<script setup>
import { ref } from 'vue'
import { shortenUrl, getRedirectUrl } from '@/service/api'

const emit = defineEmits(['shortened'])

const url = ref('')
const error = ref('')

async function submit() {
  error.value = ''
  try {
    const code = await shortenUrl(url.value)
    url.value = ''
    emit('shortened', getRedirectUrl(code))
  } catch (e) {
    error.value = e.response?.data?.error || 'Something went wrong'
  }
}
</script>

<template>
  <form @submit.prevent="submit" class="form">
    <input
      v-model="url"
      type="text"
      placeholder="Paste a URL (e.g. https://google.com)"
      required
    />
    <button type="submit">Shorten</button>
  </form>
  <p v-if="error" class="error">{{ error }}</p>
</template>

