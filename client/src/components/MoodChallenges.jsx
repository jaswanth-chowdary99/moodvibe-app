import { useState, useEffect } from 'react';
import { getChallenges } from '../api';

function MoodChallenges({ mood, moods }) {
  const [challenges, setChallenges] = useState([]);
  const [completed, setCompleted] = useState(new Set());

  useEffect(() => {
    if (!mood) return;
    getChallenges(mood).then(res => {
      setChallenges(res.data.challenges);
      setCompleted(new Set());
    }).catch(console.error);
  }, [mood]);

  if (!mood || challenges.length === 0) return null;

  const toggle = (i) => {
    setCompleted(prev => {
      const next = new Set(prev);
      if (next.has(i)) next.delete(i);
      else next.add(i);
      return next;
    });
  };

  return (
    <div className="challenges-section fade-in-up">
      <div className="challenges-header">
        <span className="challenges-icon">🏆</span>
        <span className="challenges-title">Daily Challenges</span>
        <span className="challenges-count">{completed.size}/{challenges.length}</span>
      </div>
      <div className="challenges-list">
        {challenges.map((challenge, i) => (
          <button
            key={i}
            className={`challenge-item ${completed.has(i) ? 'done' : ''}`}
            onClick={() => toggle(i)}
          >
            <span className="challenge-check">{completed.has(i) ? '✅' : '⬜'}</span>
            <span className="challenge-text">{challenge}</span>
          </button>
        ))}
      </div>
    </div>
  );
}

export default MoodChallenges;
