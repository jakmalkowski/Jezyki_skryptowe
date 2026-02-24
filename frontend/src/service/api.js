import axios from 'axios'

const API = import.meta.env.VITE_API_URL || 'http://127.0.0.1:5000'

export function getRedirectUrl(code) {
  return `${API}/api/url/${code}`
}

export async function shortenUrl(url) {
  const res = await axios.post(`${API}/api/url/shorten`, { url })
  return res.data.short_url
}

export async function fetchAllUrls() {
  const res = await axios.get(`${API}/api/url/`)
  return res.data.urls
}

export async function deleteUrl(code) {
  await axios.delete(`${API}/api/url/${code}`)
}

