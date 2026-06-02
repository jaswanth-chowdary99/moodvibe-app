import { useState, useEffect, useRef } from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import MoodPicker from './components/MoodPicker';
import CategoryTabs from './components/CategoryTabs';
import LanguageFilter from './components/LanguageFilter';
import ResultsGrid from './components/ResultsGrid';
import MoodHistory from './components/MoodHistory';
import Favorites from './components/Favorites';
import MoodStats from './components/MoodStats';
import SearchBar from './components/SearchBar';
import ShareCard from './components/ShareCard';
import MoodCalendar from './components/MoodCalendar';
import VibePolls from './components/VibePolls';
import MoodCombos from './components/MoodCombos';
import ReverseLookup from './components/ReverseLookup';
import MoodJournal from './components/MoodJournal';
import ThemeToggle from './components/ThemeToggle';
import MoodParticles from './components/MoodParticles';
import LoadingSkeleton from './components/LoadingSkeleton';
import MoodWheel from './components/MoodWheel';
import MoodGoals from './components/MoodGoals';
import MoodAffirmations from './components/MoodAffirmations';
import MoodChallenges from './components/MoodChallenges';
import MoodTimeline from './components/MoodTimeline';
import MoodPlaylist from './components/MoodPlaylist';
import MoodInsights from './components/MoodInsights';
import RecommendationRating from './components/RecommendationRating';
import { getMoods, getRecommendations, analyzeText, logMood, getHistory, getLanguages, getQuote, getFavorites, addFavorite, removeFavorite, getStats, clearHistory, exportHistory } from './api';

function App() {
  const [moods, setMoods] = useState({});
  const [currentMood, setCurrentMood] = useState(null);
  const [confidence, setConfidence] = useState(null);
  const [source, setSource] = useState(null);
  const [category, setCategory] = useState('all');
  const [lang, setLang] = useState('all');
  const [languages, setLanguages] = useState([]);
  const [recommendations, setRecommendations] = useState({});
  const [history, setHistory] = useState([]);
  const [view, setView] = useState('home');
  const [loading, setLoading] = useState(false);
  const [quote, setQuote] = useState(null);
  const [favorites, setFavorites] = useState([]);
  const [favoriteIds, setFavoriteIds] = useState(new Set());
  const [stats, setStats] = useState(null);
  const [searchQuery, setSearchQuery] = useState('');
  const [theme, setTheme] = useState(() => localStorage.getItem('mv-theme') || 'dark');

  const pickerRef = useRef(null);
  const resultsRef = useRef(null);

  useEffect(() => {
    getMoods().then(res => setMoods(res.data)).catch(console.error);
    loadFavorites();
    document.documentElement.setAttribute('data-theme', theme);
  }, []);

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('mv-theme', theme);
  }, [theme]);

  const scrollToPicker = () => {
    setView('home');
    setTimeout(() => pickerRef.current?.scrollIntoView({ behavior: 'smooth' }), 100);
  };

  const handleMoodSelect = async (moodKey, src = 'manual') => {
    try {
      await logMood(moodKey, 1.0, src);
      setCurrentMood(moodKey);
      setConfidence(1.0);
      setSource(src);
      setCategory('all');
      setLang('all');
      setSearchQuery('');
      fetchLanguages(moodKey);
      fetchRecommendations(moodKey, 'all', 'all');
      fetchQuote(moodKey);
    } catch (err) {
      console.error(err);
    }
  };

  const handleTextAnalyze = async (text) => {
    setLoading(true);
    try {
      const res = await analyzeText(text);
      setCurrentMood(res.data.mood);
      setConfidence(res.data.confidence);
      setSource('text');
      setCategory('all');
      setLang('all');
      setSearchQuery('');
      fetchLanguages(res.data.mood);
      fetchRecommendations(res.data.mood, 'all', 'all');
      fetchQuote(res.data.mood);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleSurpriseMe = () => {
    const moodKeys = Object.keys(moods);
    if (moodKeys.length === 0) return;
    const randomMood = moodKeys[Math.floor(Math.random() * moodKeys.length)];
    handleMoodSelect(randomMood, 'surprise');
    scrollToPicker();
  };

  const fetchLanguages = async (mood) => {
    try {
      const res = await getLanguages(mood);
      setLanguages(res.data.languages);
    } catch (err) {
      console.error(err);
    }
  };

  const fetchRecommendations = async (mood, cat, language) => {
    try {
      const res = await getRecommendations(mood, cat, language);
      setRecommendations(res.data.recommendations);
      setTimeout(() => resultsRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' }), 100);
    } catch (err) {
      console.error(err);
    }
  };

  const fetchQuote = async (mood) => {
    try {
      const res = await getQuote(mood);
      setQuote(res.data.quote);
    } catch (err) {
      console.error(err);
    }
  };

  const handleCategoryChange = (cat) => {
    setCategory(cat);
    if (currentMood) fetchRecommendations(currentMood, cat, lang);
  };

  const handleLanguageChange = (l) => {
    setLang(l);
    if (currentMood) fetchRecommendations(currentMood, category, l);
  };

  const loadHistory = async () => {
    try {
      const res = await getHistory();
      setHistory(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  const loadFavorites = async () => {
    try {
      const res = await getFavorites();
      setFavorites(res.data);
      setFavoriteIds(new Set(res.data.map(f => f.itemId)));
    } catch (err) {
      console.error(err);
    }
  };

  const loadStats = async () => {
    try {
      const res = await getStats();
      setStats(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  const handleToggleFavorite = async (item) => {
    const isFav = favoriteIds.has(item.itemId);
    try {
      if (isFav) {
        await removeFavorite(item.itemId);
        setFavoriteIds(prev => { const next = new Set(prev); next.delete(item.itemId); return next; });
        setFavorites(prev => prev.filter(f => f.itemId !== item.itemId));
      } else {
        await addFavorite({ ...item, mood: currentMood });
        setFavoriteIds(prev => new Set(prev).add(item.itemId));
        loadFavorites();
      }
    } catch (err) {
      console.error(err);
    }
  };

  const filterRecommendations = () => {
    if (!searchQuery.trim()) return recommendations;
    const q = searchQuery.toLowerCase();
    const filtered = {};
    Object.entries(recommendations).forEach(([cat, items]) => {
      const matched = items.filter(item =>
        (item.title && item.title.toLowerCase().includes(q)) ||
        (item.artist && item.artist.toLowerCase().includes(q)) ||
        (item.genre && item.genre.toLowerCase().includes(q))
      );
      if (matched.length > 0) filtered[cat] = matched;
    });
    return filtered;
  };

  const switchView = (v) => {
    setView(v);
    if (v === 'history') loadHistory();
    if (v === 'favorites') loadFavorites();
    if (v === 'stats') loadStats();
  };

  const handleClearHistory = async () => {
    if (!window.confirm('Clear all mood history?')) return;
    try {
      await clearHistory();
      setHistory([]);
    } catch (err) {
      console.error(err);
    }
  };

  const handleExportHistory = async () => {
    try {
      const res = await exportHistory();
      const blob = new Blob([res.data], { type: 'text/csv' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'moodvibe_history.csv';
      a.click();
      URL.revokeObjectURL(url);
    } catch (err) {
      console.error(err);
    }
  };

  const toggleTheme = () => {
    setTheme(prev => prev === 'dark' ? 'light' : 'dark');
  };

  const filteredRecommendations = filterRecommendations();

  return (
    <div className="app">
      <div className="bg-mesh"></div>
      <div className="grain"></div>
      {currentMood && <MoodParticles mood={currentMood} moods={moods} />}

      <Navbar view={view} switchView={switchView} currentMood={currentMood} moods={moods} />
      <ThemeToggle theme={theme} onToggle={toggleTheme} />

      <main>
        {view === 'home' && (
          <>
            <Hero scrollToPicker={scrollToPicker} onSurpriseMe={handleSurpriseMe} />

            <section className="section" ref={pickerRef}>
              <div className="section-header">
                <h2>How are you feeling right now?</h2>
              </div>
              <MoodPicker
                moods={moods}
                currentMood={currentMood}
                onSelect={handleMoodSelect}
                onAnalyze={handleTextAnalyze}
                loading={loading}
              />
            </section>

            {currentMood && moods[currentMood] && (
              <div className="vibe-display">
                <div className="vibe-pill">
                  <span className="vibe-pill-emoji">{moods[currentMood].emoji}</span>
                  <div>
                    <span className="vibe-pill-label">{moods[currentMood].label}</span>
                    {source === 'text' && confidence && (
                      <span className="vibe-pill-confidence">{Math.round(confidence * 100)}% match</span>
                    )}
                    {source === 'surprise' && (
                      <span className="vibe-pill-confidence">surprise pick</span>
                    )}
                  </div>
                </div>
                {quote && <p className="vibe-quote">{quote}</p>}
              </div>
            )}

            {currentMood && (
              <div className="mood-extras">
                <MoodAffirmations mood={currentMood} moods={moods} />
                <MoodChallenges mood={currentMood} moods={moods} />
              </div>
            )}

            {currentMood && (
              <>
                <ShareCard mood={currentMood} moods={moods} recommendations={recommendations} />
                <CategoryTabs
                  category={category}
                  onChange={handleCategoryChange}
                />
                <LanguageFilter
                  languages={languages}
                  currentLang={lang}
                  onChange={handleLanguageChange}
                />
                <div className="search-section">
                  <SearchBar value={searchQuery} onChange={setSearchQuery} />
                </div>
              </>
            )}

            <div ref={resultsRef}>
              {Object.keys(filteredRecommendations).length > 0 && (
                <>
                  <MoodPlaylist mood={currentMood} moods={moods} recommendations={filteredRecommendations} />
                  <ResultsGrid
                    recommendations={filteredRecommendations}
                    moods={moods}
                    currentMood={currentMood}
                    favorites={favoriteIds}
                    onToggleFavorite={handleToggleFavorite}
                    searchQuery={searchQuery}
                  />
                </>
              )}
              {currentMood && Object.keys(recommendations).length > 0 && Object.keys(filteredRecommendations).length === 0 && (
                <div className="empty-state">
                  <h3>No results found</h3>
                  <p>Try a different search term.</p>
                </div>
              )}
            </div>
          </>
        )}

        {view === 'history' && (
          <div>
            <div className="history-actions">
              <button className="btn-export" onClick={handleExportHistory}>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="7,10 12,15 17,10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
                Export CSV
              </button>
              <button className="btn-clear" onClick={handleClearHistory}>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><polyline points="3,6 5,6 21,6"/><path d="M19 6v14a2 2 0 01-2 2H7a2 2 0 01-2-2V6m3 0V4a2 2 0 012-2h4a2 2 0 012 2v2"/></svg>
                Clear
              </button>
            </div>
            <MoodHistory history={history} moods={moods} />
          </div>
        )}

        {view === 'journal' && (
          <MoodJournal moods={moods} currentMood={currentMood} />
        )}

        {view === 'favorites' && (
          <Favorites favorites={favorites} moods={moods} onRemove={async (itemId) => { await removeFavorite(itemId); setFavoriteIds(prev => { const next = new Set(prev); next.delete(itemId); return next; }); setFavorites(prev => prev.filter(f => f.itemId !== itemId)); }} />
        )}

        {view === 'stats' && (
          <MoodStats stats={stats} moods={moods} />
        )}

        {view === 'calendar' && (
          <MoodCalendar moods={moods} />
        )}

        {view === 'polls' && (
          <VibePolls moods={moods} />
        )}

        {view === 'combos' && (
          <MoodCombos moods={moods} />
        )}

        {view === 'reverse' && (
          <ReverseLookup moods={moods} />
        )}

        {view === 'wheel' && (
          <div className="wheel-page">
            <MoodWheel moods={moods} onSelect={handleMoodSelect} />
          </div>
        )}

        {view === 'goals' && (
          <MoodGoals moods={moods} />
        )}

        {view === 'insights' && (
          <MoodInsights moods={moods} />
        )}

        {view === 'timeline' && (
          <MoodTimeline history={history} moods={moods} />
        )}
      </main>

      <nav className="bottom-nav">
        <button className={`bottom-nav-item ${view === 'home' ? 'active' : ''}`} onClick={() => switchView('home')}>
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9,22 9,12 15,12 15,22"/></svg>
          <span>Home</span>
        </button>
        <button className={`bottom-nav-item ${view === 'wheel' ? 'active' : ''}`} onClick={() => switchView('wheel')}>
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="2" x2="12" y2="22"/><line x1="2" y1="12" x2="22" y2="12"/></svg>
          <span>Wheel</span>
        </button>
        <button className={`bottom-nav-item ${view === 'goals' ? 'active' : ''}`} onClick={() => switchView('goals')}>
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>
          <span>Goals</span>
        </button>
        <button className={`bottom-nav-item ${view === 'favorites' ? 'active' : ''}`} onClick={() => switchView('favorites')}>
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/></svg>
          <span>Favs</span>
        </button>
        <button className={`bottom-nav-item ${view === 'insights' ? 'active' : ''}`} onClick={() => switchView('insights')}>
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>
          <span>Insights</span>
        </button>
      </nav>
    </div>
  );
}

export default App;
