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
          <a href="#" className={`nav-link ${view === 'favorites' ? 'active' : ''}`} onClick={(e) => { e.preventDefault(); switchView('favorites'); }}>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/></svg>
            <span>Favorites</span>
          </a>
          <a href="#" className={`nav-link ${view === 'stats' ? 'active' : ''}`} onClick={(e) => { e.preventDefault(); switchView('stats'); }}>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M18 20V10"/><path d="M12 20V4"/><path d="M6 20v-6"/></svg>
            <span>Stats</span>
          </a>
          <a href="#" className={`nav-link ${view === 'history' ? 'active' : ''}`} onClick={(e) => { e.preventDefault(); switchView('history'); }}>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="12" cy="12" r="10"/><polyline points="12,6 12,12 16,14"/></svg>
            <span>History</span>
          </a>
          <a href="#" className={`nav-link ${view === 'calendar' ? 'active' : ''}`} onClick={(e) => { e.preventDefault(); switchView('calendar'); }}>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
            <span>Calendar</span>
          </a>
          <a href="#" className={`nav-link ${view === 'polls' ? 'active' : ''}`} onClick={(e) => { e.preventDefault(); switchView('polls'); }}>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M12 20V10"/><path d="M18 20V4"/><path d="M6 20v-4"/></svg>
            <span>Polls</span>
          </a>
          <a href="#" className={`nav-link ${view === 'combos' ? 'active' : ''}`} onClick={(e) => { e.preventDefault(); switchView('combos'); }}>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><rect x="2" y="2" width="20" height="20" rx="2.18"/><line x1="7" y1="2" x2="7" y2="22"/><line x1="17" y1="2" x2="17" y2="22"/><line x1="2" y1="12" x2="22" y2="12"/></svg>
            <span>Combos</span>
          </a>
          <a href="#" className={`nav-link ${view === 'reverse' ? 'active' : ''}`} onClick={(e) => { e.preventDefault(); switchView('reverse'); }}>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
            <span>Lookup</span>
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
