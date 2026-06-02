function MoodHistory({ history, moods }) {
  if (!history || history.length === 0) {
    return (
      <div className="hero">
        <div className="hero-content">
          <h1 className="hero-title">
            Your <span className="gradient-text">mood log</span>
          </h1>
          <p className="hero-subtitle">
            See how your moods shift over time.
          </p>
        </div>
        <section className="section">
          <div className="empty-state">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5"><circle cx="12" cy="12" r="10"/><polyline points="12,6 12,12 16,14"/></svg>
            <h3>No mood history yet</h3>
            <p>Pick a mood to start tracking.</p>
          </div>
        </section>
      </div>
    );
  }

  return (
    <div className="hero">
      <div className="hero-content">
        <h1 className="hero-title">
          Your <span className="gradient-text">mood log</span>
        </h1>
        <p className="hero-subtitle">
          See how your moods shift over time.
        </p>
      </div>
      <section className="section">
        <div className="history-list">
          {history.map((entry) => {
            const mood = moods[entry.mood];
            const time = new Date(entry.createdAt).toLocaleString();
            return (
              <div key={entry._id} className="history-item">
                <span className="history-emoji">{mood ? mood.emoji : '⚡'}</span>
                <div className="history-info">
                  <div className="history-vibe">{mood ? mood.label : entry.mood}</div>
                  <div className="history-time">{time}</div>
                </div>
                <span className="history-source">{entry.source}</span>
              </div>
            );
          })}
        </div>
      </section>
    </div>
  );
}

export default MoodHistory;
