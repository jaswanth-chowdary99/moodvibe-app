import { useState, useEffect } from 'react';
import { getAffirmations } from '../api';

function MoodAffirmations({ mood, moods }) {
  const [affirmations, setAffirmations] = useState([]);
  const [current, setCurrent] = useState(0);

  useEffect(() => {
    if (!mood) return;
    getAffirmations(mood).then(res => {
      setAffirmations(res.data.affirmations);
      setCurrent(0);
    }).catch(console.error);
  }, [mood]);

  if (!mood || affirmations.length === 0) return null;
  const m = moods[mood];

  const next = () => setCurrent((current + 1) % affirmations.length);
  const prev = () => setCurrent((current - 1 + affirmations.length) % affirmations.length);

  return (
    <div className="affirmations-section fade-in-up">
      <div className="affirmations-header">
        <span className="affirmations-icon">✨</span>
        <span className="affirmations-title">Daily Affirmation</span>
      </div>
      <p className="affirmation-text">"{affirmations[current]}"</p>
      <div className="affirmations-nav">
        <button onClick={prev} className="affirmation-nav-btn">←</button>
        <span className="affirmation-counter">{current + 1}/{affirmations.length}</span>
        <button onClick={next} className="affirmation-nav-btn">→</button>
      </div>
    </div>
  );
}

export default MoodAffirmations;
