<script setup>
import { getRedirectUrl, deleteUrl } from '@/service/api'

const props = defineProps({
  urls: Object
})

const emit = defineEmits(['deleted'])

function copyLink(code) {
  navigator.clipboard.writeText(getRedirectUrl(code))
}

async function remove(code) {
  await deleteUrl(code)
  emit('deleted')
}
</script>

<template>
  <div v-if="Object.keys(urls).length" class="list">
    <h2>All URLs</h2>
    <table>
      <thead>
        <tr>
          <th>Short Code</th>
          <th>Original URL</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(original, code) in urls" :key="code">
          <td>
            <a :href="getRedirectUrl(code)" target="_blank">{{ code }}</a>
          </td>
          <td class="original-url">{{ original }}</td>
          <td class="actions">
            <button @click="copyLink(code)" class="btn-small">Copy</button>
            <button @click="remove(code)" class="btn-small btn-delete">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

