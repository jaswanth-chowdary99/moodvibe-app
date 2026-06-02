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

export const getQuote = (mood) => api.get(`/quote/${mood}`);

export const getFavorites = () => api.get('/favorites');
export const addFavorite = (item) => api.post('/favorites', item);
export const removeFavorite = (itemId) => api.delete(`/favorites/${itemId}`);

export const getStats = () => api.get('/stats');

export const getCalendar = (days = 90) => api.get(`/calendar?days=${days}`);
export const getCombos = (mood) => api.get(`/combos/${mood}`);
export const getPolls = () => api.get('/polls');
export const createPoll = (mood) => api.post('/polls', { mood });
export const votePoll = (pollId, optionId) => api.post(`/polls/${pollId}/vote`, { optionId });
export const reverseLookup = (query) => api.post('/reverse-lookup', { query });
export const seedPolls = () => api.post('/seed-polls');

export default api;
