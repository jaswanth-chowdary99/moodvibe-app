function Navbar({ view, switchView, currentMood, moods }) {
  const mood = currentMood && moods[currentMood];

  return (
    <nav className="navbar">
      <div className="nav-container">
        <a href="#" className="nav-logo" onClick={(e) => { e.preventDefault(); switchView('home'); }}>
          <svg viewBox="0 0 32 32" width="28" height="28">
            <defs>
              <linearGradient id="logoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style={{ stopColor: '#a78bfa' }} />
                <stop offset="100%" style={{ stopColor: '#7c3aed' }} />
              </linearGradient>
            </defs>
            <circle cx="16" cy="16" r="14" fill="url(#logoGrad)" />
            <path d="M12 10v12l10-6z" fill="white" opacity="0.95" />
          </svg>
          <span>MoodVibe</span>
        </a>

        <div className="nav-links">
          <a href="#" className={`nav-link ${view === 'home' ? 'active' : ''}`} onClick={(e) => { e.preventDefault(); switchView('home'); }}>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9,22 9,12 15,12 15,22"/></svg>
            <span>Home</span>
          </a>
          <a href="#" className={`nav-link ${view === 'history' ? 'active' : ''}`} onClick={(e) => { e.preventDefault(); switchView('history'); }}>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="12" cy="12" r="10"/><polyline points="12,6 12,12 16,14"/></svg>
            <span>History</span>
          </a>
        </div>

        {mood && (
          <div className="nav-vibe-indicator">
            <span className="nav-vibe-emoji">{mood.emoji}</span>
            <span className="nav-vibe-label">{mood.label}</span>
          </div>
        )}
      </div>
    </nav>
  );
}

export default Navbar;
