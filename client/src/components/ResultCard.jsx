function ResultCard({ item, category, delay, isFavorited, onToggleFavorite }) {
  const cardClass = category === 'music' ? 'result-card' : category === 'movies' ? 'movie-card' : 'anime-card';

  const platformIcons = {
    'Spotify': '🟢',
    'Apple Music': '🍎',
    'JioSaavn': '🎵',
    'Netflix': '🔴',
    'Prime Video': '🔵',
    'Disney+': '✨',
    'Crunchyroll': '🍊',
    'Amazon': '📦',
    'YouTube': '▶️',
  };

  const handleFavorite = (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (onToggleFavorite) {
      onToggleFavorite({
        itemId: item._id,
        title: item.title,
        artist: item.artist,
        genre: item.genre,
        platform: item.platform,
        url: item.url,
        category,
        lang: item.lang,
        rating: item.rating,
        episodes: item.episodes,
        dub: item.dub,
      });
    }
  };

  return (
    <a
      href={item.url || '#'}
      target="_blank"
      rel="noopener noreferrer"
      className={`${cardClass} fade-in-up clickable-card`}
      style={{ animationDelay: `${delay}s`, textDecoration: 'none', color: 'inherit' }}
    >
      <button
        className={`favorite-btn ${isFavorited ? 'favorited' : ''}`}
        onClick={handleFavorite}
        title={isFavorited ? 'Remove from favorites' : 'Add to favorites'}
      >
        <svg width="16" height="16" viewBox="0 0 24 24" fill={isFavorited ? 'currentColor' : 'none'} stroke="currentColor" strokeWidth="2">
          <path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/>
        </svg>
      </button>

      {category === 'music' && (
        <>
          <div className="result-card-icon">
            {item.lang === 'Telugu' ? '🎵' : '🎶'}
          </div>
          <div className="result-card-info">
            <div className="result-card-title">{item.title}</div>
            <div className="result-card-meta">{item.artist} · {item.genre}</div>
          </div>
          <span className="result-card-tag">
            {platformIcons[item.platform] || '🎵'} {item.platform}
          </span>
          <svg className="card-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><line x1="7" y1="17" x2="17" y2="7"/><polyline points="7,7 17,7 17,17"/></svg>
        </>
      )}

      {category === 'movies' && (
        <>
          <div className="movie-card-icon">
            {item.lang === 'Telugu' ? '🎬' : '🎥'}
          </div>
          <div className="movie-card-info">
            <div className="movie-card-title">{item.title}</div>
            <div className="movie-card-meta">
              {item.year} · {item.genre}
            </div>
            <div className="movie-card-rating">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="#f59e0b" stroke="none"><polygon points="12,2 15.09,8.26 22,9.27 17,14.14 18.18,21.02 12,17.77 5.82,21.02 7,14.14 2,9.27 8.91,8.26"/></svg>
              {item.rating}
            </div>
          </div>
          <span className="result-card-platform">
            {platformIcons[item.platform] || '🎬'} {item.platform}
          </span>
          <svg className="card-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><line x1="7" y1="17" x2="17" y2="7"/><polyline points="7,7 17,7 17,17"/></svg>
        </>
      )}

      {category === 'anime' && (
        <>
          <div className="anime-card-icon">
            {item.lang === 'Telugu' ? '⛩️' : '🌸'}
          </div>
          <div className="anime-card-info">
            <div className="anime-card-title">{item.title}</div>
            <div className="anime-card-meta">
              {item.episodes ? `${item.episodes} eps` : 'Movie'} · {item.genre}
            </div>
            <div className="anime-card-rating">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="#f59e0b" stroke="none"><polygon points="12,2 15.09,8.26 22,9.27 17,14.14 18.18,21.02 12,17.77 5.82,21.02 7,14.14 2,9.27 8.91,8.26"/></svg>
              {item.rating}
            </div>
          </div>
          <span className="anime-card-dub">
            {item.dub || 'Both'}
          </span>
          <svg className="card-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><line x1="7" y1="17" x2="17" y2="7"/><polyline points="7,7 17,7 17,17"/></svg>
        </>
      )}
    </a>
  );
}

export default ResultCard;
