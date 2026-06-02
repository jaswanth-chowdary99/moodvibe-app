import axios from 'axios';

const api = axios.create({
  baseURL: '/api',
});

export const getMoods = () => api.get('/moods');

export const getRecommendations = (mood, category = 'all', lang = 'all', count = 6) =>
  api.post('/recommend', { mood, category, lang, count });

export const analyzeText = (text) => api.post('/analyze', { text });

export const logMood = (mood, confidence = 1.0, source = 'manual') =>
  api.post('/history', { mood, confidence, source });

export const getHistory = () => api.get('/history');

export const getLanguages = (mood) => api.get(`/languages/${mood}`);

export default api;
