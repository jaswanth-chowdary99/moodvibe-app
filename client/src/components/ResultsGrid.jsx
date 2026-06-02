import ResultCard from './ResultCard';

function ResultsGrid({ recommendations, moods, currentMood, favoriteIds, onToggleFavorite }) {
  const categoryConfig = {
    music: {
      title: 'Music',
      icon: <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>,
    },
    movies: {
      title: 'Movies',
      icon: <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><rect x="2" y="2" width="20" height="20" rx="2.18"/><line x1="7" y1="2" x2="7" y2="22"/><line x1="17" y1="2" x2="17" y2="22"/><line x1="2" y1="12" x2="22" y2="12"/></svg>,
    },
    anime: {
      title: 'Anime',
      icon: <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg>,
    },
  };

  return (
    <div className="results-section">
      {Object.entries(recommendations).map(([cat, items], catIdx) => {
        const config = categoryConfig[cat];
        if (!config || !items || items.length === 0) return null;

        return (
          <div key={cat} className="result-category fade-in-up" style={{ animationDelay: `${catIdx * 0.1}s` }}>
            <div className="result-category-header">
              <div className="result-category-icon">{config.icon}</div>
              <span className="result-category-title">{config.title}</span>
              <span className="result-category-count">{items.length} picks</span>
            </div>
            <div className="result-grid">
              {items.map((item, i) => (
                <ResultCard
                  key={item._id || i}
                  item={item}
                  category={cat}
                  delay={catIdx * 0.1 + i * 0.05}
                  isFavorited={favoriteIds?.has(item._id)}
                  onToggleFavorite={onToggleFavorite}
                />
              ))}
            </div>
          </div>
        );
      })}
    </div>
  );
}

export default ResultsGrid;
