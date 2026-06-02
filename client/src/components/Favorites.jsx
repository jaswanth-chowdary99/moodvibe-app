import ResultCard from './ResultCard';

function Favorites({ favorites, moods, favoriteIds, onToggleFavorite }) {
  if (!favorites || favorites.length === 0) {
    return (
      <div className="empty-state">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
          <path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/>
        </svg>
        <h3>No favorites yet</h3>
        <p>Heart the recommendations you love to save them here.</p>
      </div>
    );
  }

  const grouped = { music: [], movies: [], anime: [] };
  favorites.forEach(fav => {
    const cat = fav.category || 'music';
    if (grouped[cat]) grouped[cat].push(fav);
  });

  const categoryLabels = { music: 'Music', movies: 'Movies', anime: 'Anime' };
  const categoryIcons = {
    music: <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>,
    movies: <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><rect x="2" y="2" width="20" height="20" rx="2.18"/><line x1="7" y1="2" x2="7" y2="22"/><line x1="17" y1="2" x2="17" y2="22"/><line x1="2" y1="12" x2="22" y2="12"/></svg>,
    anime: <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg>,
  };

  return (
    <div className="favorites-page">
      <div className="favorites-header">
        <h2>Your Favorites</h2>
        <span className="favorites-count">{favorites.length} saved</span>
      </div>
      {Object.entries(grouped).map(([cat, items]) => {
        if (items.length === 0) return null;
        return (
          <div key={cat} className="result-category fade-in-up">
            <div className="result-category-header">
              <div className="result-category-icon">{categoryIcons[cat]}</div>
              <span className="result-category-title">{categoryLabels[cat]}</span>
              <span className="result-category-count">{items.length}</span>
            </div>
            <div className="result-grid">
              {items.map((item, i) => (
                <ResultCard
                  key={item.itemId || i}
                  item={{ ...item, _id: item.itemId }}
                  category={cat}
                  delay={i * 0.05}
                  isFavorited={favoriteIds.has(item.itemId)}
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

export default Favorites;
