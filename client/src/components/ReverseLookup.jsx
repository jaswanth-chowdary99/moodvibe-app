import { useState } from 'react';
import { reverseLookup } from '../api';

function ReverseLookup({ moods }) {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    if (!query.trim()) return;
    setLoading(true);
    try {
      const res = await reverseLookup(query.trim());
      setResults(res.data.results);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') handleSearch();
  };

  const platformIcons = {
    'Spotify': '🟢', 'Apple Music': '🍎', 'JioSaavn': '🎵',
    'Netflix': '🔴', 'Prime Video': '🔵', 'Disney+': '✨',
    'Crunchyroll': '🍊', 'Amazon': '📦', 'YouTube': '▶️',
  };

  return (
    <div className="reverse-page">
      <div className="section-header">
        <h2>Reverse Lookup</h2>
        <span className="reverse-subtitle">Find what mood a title fits</span>
      </div>

      <div className="reverse-search">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Type a movie, song, or anime title..."
        />
        <button className="btn-analyze" onClick={handleSearch} disabled={loading || !query.trim()}>
          {loading ? 'Searching...' : 'Find Mood'}
        </button>
      </div>

      {results && results.length === 0 && (
        <div className="empty-state">
          <h3>No matches found</h3>
          <p>Try a different title or genre.</p>
        </div>
      )}

      {results && results.length > 0 && (
        <div className="reverse-results">
          {results.map((item, i) => {
            const m = moods[item.mood];
            return (
              <div key={item._id || i} className="reverse-result-card fade-in-up" style={{ animationDelay: `${i * 0.05}s` }}>
                <div className="reverse-mood-badge" style={{ background: m?.color || 'var(--accent)' }}>
                  <span className="reverse-mood-emoji">{m?.emoji || '?'}</span>
                  <span className="reverse-mood-label">{m?.label || item.mood}</span>
                </div>
                <div className="reverse-result-info">
                  <div className="reverse-result-title">{item.title}</div>
                  <div className="reverse-result-meta">
                    {item.artist && <span>{item.artist} · </span>}
                    {item.genre && <span>{item.genre}</span>}
                    {item.year && <span> · {item.year}</span>}
                    {item.episodes && <span> · {item.episodes} eps</span>}
                  </div>
                </div>
                <span className="reverse-result-platform">
                  {platformIcons[item.platform] || '🔗'} {item.platform}
                </span>
                {item.url && (
                  <a href={item.url} target="_blank" rel="noopener noreferrer" className="reverse-result-link">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><line x1="7" y1="17" x2="17" y2="7"/><polyline points="7,7 17,7 17,17"/></svg>
                  </a>
                )}
              </div>
            );
          })}
        </div>
      )}

      {!results && (
        <div className="empty-state">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
            <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
          </svg>
          <h3>Search any title</h3>
          <p>Find out what mood a movie, song, or anime matches.</p>
        </div>
      )}
    </div>
  );
}

export default ReverseLookup;
