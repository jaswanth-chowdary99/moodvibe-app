import { useState } from 'react';

function ShareCard({ mood, moods, recommendations }) {
  const [copied, setCopied] = useState(false);

  if (!mood || !moods[mood]) return null;

  const m = moods[mood];
  const firstRec = Object.values(recommendations).flat()[0];

  const shareText = `I'm feeling ${m.emoji} ${m.label} right now on MoodVibe!\n${firstRec ? `🎵 ${firstRec.title}` : ''}\nCheck it out: https://moodvibe-app.onrender.com`;

  const handleShare = async () => {
    if (navigator.share) {
      try {
        await navigator.share({ title: `MoodVibe — ${m.label}`, text: shareText, url: 'https://moodvibe-app.onrender.com' });
      } catch (e) {
        // user cancelled
      }
    } else {
      try {
        await navigator.clipboard.writeText(shareText);
        setCopied(true);
        setTimeout(() => setCopied(false), 2000);
      } catch (e) {
        console.error(e);
      }
    }
  };

  return (
    <div className="share-section">
      <button className="btn-share" onClick={handleShare}>
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/>
          <line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/>
        </svg>
        {copied ? 'Copied!' : 'Share your vibe'}
      </button>
    </div>
  );
}

export default ShareCard;
