import { useState, useEffect } from 'react';
import { getCombos } from '../api';

function MoodCombos({ moods }) {
  const [selectedMood, setSelectedMood] = useState(null);
  const [combos, setCombos] = useState([]);
  const [loading, setLoading] = useState(false);

  const loadCombos = async (mood) => {
    setLoading(true);
    try {
      const res = await getCombos(mood);
      setCombos(res.data.combos);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleMoodSelect = (mood) => {
    setSelectedMood(mood);
    loadCombos(mood);
  };

  return (
    <div className="combos-page">
      <div className="section-header">
        <h2>Mood Combos</h2>
        <span className="combos-subtitle">Curated vibes for your mood</span>
      </div>

      <div className="combos-mood-grid">
        {Object.entries(moods).map(([key, mood]) => (
          <div
            key={key}
            className={`combo-mood-chip ${selectedMood === key ? 'selected' : ''}`}
            style={{ '--chip-color': mood.color }}
            onClick={() => handleMoodSelect(key)}
          >
            <span>{mood.emoji}</span>
            <span>{mood.label}</span>
          </div>
        ))}
      </div>

      {loading && (
        <div className="empty-state"><h3>Loading combos...</h3></div>
      )}

      {!loading && selectedMood && combos.length > 0 && (
        <div className="combos-grid">
          {combos.map((combo, i) => {
            const m = moods[selectedMood];
            return (
              <div key={i} className="combo-card fade-in-up" style={{ animationDelay: `${i * 0.1}s` }}>
                <div className="combo-vibe-tag" style={{ background: m?.color || 'var(--accent)' }}>
                  {combo.vibe}
                </div>
                <div className="combo-items">
                  <div className="combo-item">
                    <span className="combo-icon">🎬</span>
                    <div>
                      <div className="combo-label">Watch</div>
                      <div className="combo-value">{combo.movie}</div>
                    </div>
                  </div>
                  <div className="combo-item">
                    <span className="combo-icon">🎵</span>
                    <div>
                      <div className="combo-label">Listen</div>
                      <div className="combo-value">{combo.music}</div>
                    </div>
                  </div>
                  <div className="combo-item">
                    <span className="combo-icon">🍿</span>
                    <div>
                      <div className="combo-label">Snack</div>
                      <div className="combo-value">{combo.snack}</div>
                    </div>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}

      {!loading && selectedMood && combos.length === 0 && (
        <div className="empty-state">
          <h3>No combos yet</h3>
          <p>Try another mood.</p>
        </div>
      )}

      {!selectedMood && (
        <div className="empty-state">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
            <rect x="2" y="2" width="20" height="20" rx="2.18"/>
            <line x1="7" y1="2" x2="7" y2="22"/>
            <line x1="17" y1="2" x2="17" y2="22"/>
            <line x1="2" y1="12" x2="22" y2="12"/>
          </svg>
          <h3>Pick a mood above</h3>
          <p>Get a curated movie + music + snack combo.</p>
        </div>
      )}
    </div>
  );
}

export default MoodCombos;
