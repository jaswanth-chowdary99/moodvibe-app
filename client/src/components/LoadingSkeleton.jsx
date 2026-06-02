function LoadingSkeleton({ type = 'card', count = 3 }) {
  if (type === 'card') {
    return (
      <div className="skeleton-grid">
        {Array.from({ length: count }).map((_, i) => (
          <div key={i} className="skeleton-card">
            <div className="skeleton-icon skeleton-pulse" />
            <div className="skeleton-lines">
              <div className="skeleton-line skeleton-pulse" style={{ width: '80%' }} />
              <div className="skeleton-line skeleton-pulse" style={{ width: '60%' }} />
            </div>
          </div>
        ))}
      </div>
    );
  }

  if (type === 'mood') {
    return (
      <div className="skeleton-grid">
        {Array.from({ length: 10 }).map((_, i) => (
          <div key={i} className="skeleton-mood-card">
            <div className="skeleton-emoji skeleton-pulse" />
            <div className="skeleton-line skeleton-pulse" style={{ width: '60%', margin: '8px auto 0' }} />
          </div>
        ))}
      </div>
    );
  }

  return null;
}

export default LoadingSkeleton;
