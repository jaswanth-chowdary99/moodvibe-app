import { useState } from 'react';

function MoodPicker({ moods, currentMood, onSelect, onAnalyze, loading }) {
  const [text, setText] = useState('');

  const handleAnalyze = () => {
    if (text.trim()) onAnalyze(text.trim());
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleAnalyze();
    }
  };

  return (
    <>
      <div className="vibe-grid">
        {Object.entries(moods).map(([key, mood]) => (
          <div
            key={key}
            className={`vibe-card ${currentMood === key ? 'selected' : ''}`}
            style={{ '--card-color': mood.color }}
            onClick={() => onSelect(key, 'manual')}
          >
            <span className="vibe-card-emoji">{mood.emoji}</span>
            <div className="vibe-card-label">{mood.label}</div>
          </div>
        ))}
      </div>

      <div className="text-section">
        <p className="text-section-label">Or describe how you feel...</p>
        <div className="text-input-card">
          <div className="textarea-wrapper">
            <textarea
              value={text}
              onChange={(e) => setText(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder="Just aced my exam, feeling amazing!&#10;&#10;Or: feeling lonely, miss my school days..."
              rows="3"
            />
            <div className="textarea-footer">
              <span className="char-count">{text.length}</span>
              <button className="btn-analyze" onClick={handleAnalyze} disabled={loading || !text.trim()}>
                {loading ? (
                  'Detecting...'
                ) : (
                  <>
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22,4 12,14.01 9,11.01"/></svg>
                    Detect mood
                  </>
                )}
              </button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default MoodPicker;
