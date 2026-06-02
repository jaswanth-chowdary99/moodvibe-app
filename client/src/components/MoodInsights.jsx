import { useState, useEffect } from 'react';
import { getInsights } from '../api';

function MoodInsights({ moods }) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getInsights().then(res => {
      setData(res.data);
      setLoading(false);
    }).catch(() => setLoading(false));
  }, []);

  if (loading) return <div className="empty-state"><h3>Analyzing...</h3></div>;

  if (!data || data.total === 0) {
    return (
      <div className="section">
        <div className="empty-state">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
            <path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/>
          </svg>
          <h3>No insights yet</h3>
          <p>Check in with your mood a few times to see patterns.</p>
        </div>
      </div>
    );
  }

  const { insights, patterns } = data;

  return (
    <div className="insights-page">
      <div className="section-header">
        <h2>Mood Insights</h2>
        <span className="insights-total">{data.total} check-ins analyzed</span>
      </div>

      <div className="insights-cards">
        {insights.map((insight, i) => (
          <div key={i} className="insight-card fade-in-up" style={{ animationDelay: `${i * 0.1}s` }}>
            <div className="insight-icon">💡</div>
            <p className="insight-text">{insight}</p>
          </div>
        ))}
      </div>

      {patterns.dayCounts && Object.keys(patterns.dayCounts).length > 0 && (
        <div className="insights-pattern">
          <h3>Check-in by Day</h3>
          <div className="pattern-bars">
            {['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'].map(day => {
              const count = patterns.dayCounts[day] || 0;
              const max = Math.max(...Object.values(patterns.dayCounts));
              const pct = max > 0 ? (count / max) * 100 : 0;
              return (
                <div key={day} className="pattern-row">
                  <span className="pattern-label">{day.slice(0, 3)}</span>
                  <div className="pattern-track">
                    <div className="pattern-fill" style={{ width: `${pct}%` }} />
                  </div>
                  <span className="pattern-count">{count}</span>
                </div>
              );
            })}
          </div>
        </div>
      )}

      {patterns.timeCounts && Object.keys(patterns.timeCounts).length > 0 && (
        <div className="insights-pattern">
          <h3>Check-in by Time</h3>
          <div className="pattern-bars">
            {['Morning', 'Afternoon', 'Evening', 'Night'].map(time => {
              const count = patterns.timeCounts[time] || 0;
              const max = Math.max(...Object.values(patterns.timeCounts));
              const pct = max > 0 ? (count / max) * 100 : 0;
              return (
                <div key={time} className="pattern-row">
                  <span className="pattern-label">{time}</span>
                  <div className="pattern-track">
                    <div className="pattern-fill" style={{ width: `${pct}%`, background: 'var(--accent-2)' }} />
                  </div>
                  <span className="pattern-count">{count}</span>
                </div>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
}

export default MoodInsights;
