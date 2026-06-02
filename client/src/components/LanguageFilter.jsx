function LanguageFilter({ languages, currentLang, onChange }) {
  if (!languages || languages.length <= 1) return null;

  const langLabels = {
    'all': 'All Languages',
    'Telugu': 'Telugu',
    'Hindi': 'Hindi',
    'English': 'English',
    'Tamil': 'Tamil',
    'Korean': 'Korean',
    'Japanese': 'Japanese',
  };

  const langFlags = {
    'all': '🌍',
    'Telugu': '🇮🇳',
    'Hindi': '🇮🇳',
    'English': '🇬🇧',
    'Tamil': '🇮🇳',
    'Korean': '🇰🇷',
    'Japanese': '🇯🇵',
  };

  return (
    <div className="lang-section">
      <div className="lang-tabs">
        {languages.map(l => (
          <button
            key={l}
            className={`lang-tab ${currentLang === l ? 'active' : ''}`}
            onClick={() => onChange(l)}
          >
            <span className="lang-flag">{langFlags[l] || '🌐'}</span>
            {langLabels[l] || l}
          </button>
        ))}
      </div>
    </div>
  );
}

export default LanguageFilter;
