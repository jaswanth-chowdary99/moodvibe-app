function MoodStats({ stats, moods }) {
  if (!stats || stats.total === 0) {
    return (
      <div className="section">
        <div className="empty-state">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
            <path d="M18 20V10"/><path d="M12 20V4"/><path d="M6 20v-6"/>
          </svg>
          <h3>No mood data yet</h3>
          <p>Select a mood to start building your vibe history.</p>
        </div>
      </div>
    );
  }

  const sortedMoods = Object.entries(stats.moodCounts)
    .sort((a, b) => b[1] - a[1]);

  const maxCount = sortedMoods.length > 0 ? sortedMoods[0][1] : 1;

  return (
    <div className="section stats-page">
      <div className="section-header">
        <h2>Mood Stats</h2>
        <span className="stats-total">{stats.total} check-ins</span>
      </div>

      <div className="stats-cards">
        <div className="stat-card">
          <div className="stat-card-emoji">
            {stats.mostFrequent && moods[stats.mostFrequent] ? moods[stats.mostFrequent].emoji : '📊'}
          </div>
          <div className="stat-card-label">Top Mood</div>
          <div className="stat-card-value">
            {stats.mostFrequent && moods[stats.mostFrequent] ? moods[stats.mostFrequent].label : '—'}
          </div>
        </div>
        <div className="stat-card">
          <div className="stat-card-emoji">🔥</div>
          <div className="stat-card-label">Current Streak</div>
          <div className="stat-card-value">{stats.currentStreak}</div>
        </div>
        <div className="stat-card">
          <div className="stat-card-emoji">📈</div>
          <div className="stat-card-label">Total Check-ins</div>
          <div className="stat-card-value">{stats.total}</div>
        </div>
      </div>

      <div className="mood-chart">
        <h3 className="chart-title">Mood Distribution</h3>
        {sortedMoods.map(([mood, count]) => {
          const m = moods[mood];
          const pct = Math.round((count / maxCount) * 100);
          return (
            <div key={mood} className="chart-row">
              <div className="chart-label">
                <span className="chart-emoji">{m?.emoji || '❓'}</span>
                <span>{m?.label || mood}</span>
              </div>
              <div className="chart-bar-track">
                <div
                  className="chart-bar-fill"
                  style={{ width: `${pct}%`, background: m?.color || 'var(--accent)' }}
                />
              </div>
              <span className="chart-count">{count}</span>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default MoodStats;
