function MoodPlaylist({ mood, moods, recommendations }) {
  if (!mood || !recommendations || Object.keys(recommendations).length === 0) return null;

  const allItems = [];
  Object.entries(recommendations).forEach(([cat, items]) => {
    items.forEach(item => allItems.push({ ...item, category: cat }));
  });

  if (allItems.length === 0) return null;

  const m = moods[mood];

  const handlePlayAll = () => {
    allItems.forEach((item, i) => {
      if (item.url) {
        setTimeout(() => window.open(item.url, '_blank'), i * 300);
      }
    });
  };

  return (
    <div className="playlist-section fade-in-up">
      <div className="playlist-header">
        <div className="playlist-info">
          <span className="playlist-emoji">{m?.emoji}</span>
          <div>
            <div className="playlist-title">{m?.label} Playlist</div>
            <div className="playlist-count">{allItems.length} picks</div>
          </div>
        </div>
        <button className="btn-play-all" onClick={handlePlayAll}>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
          Open All
        </button>
      </div>
      <div className="playlist-items">
        {allItems.map((item, i) => (
          <a
            key={item._id || i}
            href={item.url || '#'}
            target="_blank"
            rel="noopener noreferrer"
            className="playlist-item"
          >
            <span className="playlist-num">{i + 1}</span>
            <div className="playlist-item-info">
              <span className="playlist-item-title">{item.title}</span>
              <span className="playlist-item-meta">{item.artist || item.genre || item.category}</span>
            </div>
            <span className="playlist-item-platform">{item.platform}</span>
          </a>
        ))}
      </div>
    </div>
  );
}

export default MoodPlaylist;
