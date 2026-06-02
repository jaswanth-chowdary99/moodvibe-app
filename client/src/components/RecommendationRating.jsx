import { useState, useEffect } from 'react';
import { rateRecommendation, getRating } from '../api';

function RecommendationRating({ itemId, mood }) {
  const [rating, setRating] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (!itemId) return;
    getRating(itemId).then(res => {
      if (res.data.rating) setRating(res.data.rating);
    }).catch(() => {});
  }, [itemId]);

  const handleRate = async (value) => {
    if (loading) return;
    setLoading(true);
    try {
      await rateRecommendation({ itemId, rating: value, mood });
      setRating(value);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="rating-widget">
      <button
        className={`rating-btn ${rating === 'up' ? 'active up' : ''}`}
        onClick={(e) => { e.preventDefault(); e.stopPropagation(); handleRate('up'); }}
        title="Good recommendation"
      >
        <svg width="14" height="14" viewBox="0 0 24 24" fill={rating === 'up' ? 'currentColor' : 'none'} stroke="currentColor" strokeWidth="2">
          <path d="M14 9V5a3 3 0 00-3-3l-4 9v11h11.28a2 2 0 002-1.7l1.38-9a2 2 0 00-2-2.3H14z"/><path d="M7 22H4a2 2 0 01-2-2v-7a2 2 0 012-2h3"/>
        </svg>
      </button>
      <button
        className={`rating-btn ${rating === 'down' ? 'active down' : ''}`}
        onClick={(e) => { e.preventDefault(); e.stopPropagation(); handleRate('down'); }}
        title="Not for me"
      >
        <svg width="14" height="14" viewBox="0 0 24 24" fill={rating === 'down' ? 'currentColor' : 'none'} stroke="currentColor" strokeWidth="2">
          <path d="M10 15v4a3 3 0 003 3l4-9V2H5.72a2 2 0 00-2 1.7l-1.38 9a2 2 0 002 2.3H10z"/><path d="M17 2h2.67A2.31 2.31 0 0122 4v7a2.31 2.31 0 01-2.33 2H17"/>
        </svg>
      </button>
    </div>
  );
}

export default RecommendationRating;
