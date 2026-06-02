function MoodTimeline({ history, moods }) {
  if (!history || history.length === 0) {
    return (
      <div className="section">
        <div className="empty-state">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
            <circle cx="12" cy="12" r="10"/><polyline points="12,6 12,12 16,14"/>
          </svg>
          <h3>No timeline yet</h3>
          <p>Select some moods to build your timeline.</p>
        </div>
      </div>
    );
  }

  const grouped = {};
  history.forEach(entry => {
    const date = new Date(entry.createdAt).toLocaleDateString('en-US', { weekday: 'long', month: 'short', day: 'numeric' });
    if (!grouped[date]) grouped[date] = [];
    grouped[date].push(entry);
  });

  return (
    <div className="timeline-page">
      <div className="section-header">
        <h2>Mood Timeline</h2>
      </div>

      {Object.entries(grouped).map(([date, entries]) => (
        <div key={date} className="timeline-day">
          <div className="timeline-date">{date}</div>
          <div className="timeline-entries">
            {entries.map((entry, i) => {
              const m = moods[entry.mood];
              const time = new Date(entry.createdAt).toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });
              return (
                <div key={i} className="timeline-entry fade-in-up" style={{ animationDelay: `${i * 0.05}s` }}>
                  <div className="timeline-dot" style={{ background: m?.color || 'var(--accent)' }} />
                  <div className="timeline-line" />
                  <div className="timeline-content">
                    <div className="timeline-time">{time}</div>
                    <div className="timeline-mood">
                      <span className="timeline-emoji">{m?.emoji || '?'}</span>
                      <span className="timeline-label">{m?.label || entry.mood}</span>
                      {entry.source === 'text' && <span className="timeline-badge">text</span>}
                      {entry.source === 'surprise' && <span className="timeline-badge">surprise</span>}
                      {entry.source === 'wheel' && <span className="timeline-badge">wheel</span>}
                    </div>
                    {entry.confidence < 1 && (
                      <div className="timeline-confidence">{Math.round(entry.confidence * 100)}% match</div>
                    )}
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      ))}
    </div>
  );
}

export default MoodTimeline;
