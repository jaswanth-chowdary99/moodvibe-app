function Hero({ scrollToPicker }) {
  return (
    <div className="hero">
      <div className="hero-content">
        <h1 className="hero-title">
          Entertainment that<br />
          <span className="gradient-text">feels right.</span>
        </h1>
        <p className="hero-subtitle">
          Music, movies & anime matched to your mood. Not algorithms — just good taste.
        </p>
        <div className="hero-actions">
          <button className="btn-hero-cta" onClick={scrollToPicker}>
            Pick your mood
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5"><line x1="12" y1="5" x2="12" y2="19"/><polyline points="19,12 12,19 5,12"/></svg>
          </button>
        </div>
      </div>
    </div>
  );
}

export default Hero;
