import { useState, useEffect, useRef } from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import MoodPicker from './components/MoodPicker';
import CategoryTabs from './components/CategoryTabs';
import LanguageFilter from './components/LanguageFilter';
import ResultsGrid from './components/ResultsGrid';
import MoodHistory from './components/MoodHistory';
import { getMoods, getRecommendations, analyzeText, logMood, getHistory, getLanguages } from './api';

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

  const pickerRef = useRef(null);
  const resultsRef = useRef(null);

  useEffect(() => {
    getMoods().then(res => setMoods(res.data)).catch(console.error);
  }, []);

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
      fetchLanguages(moodKey);
      fetchRecommendations(moodKey, 'all', 'all');
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
      fetchLanguages(res.data.mood);
      fetchRecommendations(res.data.mood, 'all', 'all');
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
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

  const switchView = (v) => {
    setView(v);
    if (v === 'history') loadHistory();
  };

  return (
    <div className="app">
      <div className="bg-mesh"></div>
      <div className="grain"></div>

      <Navbar view={view} switchView={switchView} currentMood={currentMood} moods={moods} />

      <main>
        {view === 'home' && (
          <>
            <Hero scrollToPicker={scrollToPicker} />

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
                  </div>
                </div>
              </div>
            )}

            {currentMood && (
              <>
                <CategoryTabs
                  category={category}
                  onChange={handleCategoryChange}
                />
                <LanguageFilter
                  languages={languages}
                  currentLang={lang}
                  onChange={handleLanguageChange}
                />
              </>
            )}

            <div ref={resultsRef}>
              {Object.keys(recommendations).length > 0 && (
                <ResultsGrid
                  recommendations={recommendations}
                  moods={moods}
                  currentMood={currentMood}
                />
              )}
            </div>
          </>
        )}

        {view === 'history' && (
          <MoodHistory history={history} moods={moods} />
        )}
      </main>

      <nav className="bottom-nav">
        <button className={`bottom-nav-item ${view === 'home' ? 'active' : ''}`} onClick={() => switchView('home')}>
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9,22 9,12 15,12 15,22"/></svg>
          <span>Home</span>
        </button>
        <button className="bottom-nav-item" onClick={scrollToPicker}>
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg>
          <span>Mood</span>
        </button>
        <button className={`bottom-nav-item ${view === 'history' ? 'active' : ''}`} onClick={() => switchView('history')}>
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="12" cy="12" r="10"/><polyline points="12,6 12,12 16,14"/></svg>
          <span>History</span>
        </button>
      </nav>
    </div>
  );
}

export default App;
