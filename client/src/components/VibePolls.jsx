import { useState, useEffect } from 'react';
import { getPolls, votePoll, seedPolls } from '../api';

function VibePolls({ moods }) {
  const [polls, setPolls] = useState([]);
  const [votedPolls, setVotedPolls] = useState(new Set());
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadPolls();
  }, []);

  const loadPolls = async () => {
    setLoading(true);
    try {
      const res = await getPolls();
      if (res.data.length === 0) {
        // Seed polls if none exist
        await seedPolls();
        const res2 = await getPolls();
        setPolls(res2.data);
      } else {
        setPolls(res.data);
      }
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleVote = async (pollId, optionId) => {
    if (votedPolls.has(pollId)) return;
    try {
      const res = await votePoll(pollId, optionId);
      setPolls(prev => prev.map(p => p._id === pollId ? res.data : p));
      setVotedPolls(prev => new Set(prev).add(pollId));
    } catch (err) {
      console.error(err);
    }
  };

  if (loading) {
    return (
      <div className="section">
        <div className="empty-state"><h3>Loading polls...</h3></div>
      </div>
    );
  }

  if (polls.length === 0) {
    return (
      <div className="section">
        <div className="empty-state">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
            <path d="M12 20V10"/><path d="M18 20V4"/><path d="M6 20v-4"/>
          </svg>
          <h3>No active polls</h3>
          <p>Check back later for new vibe polls.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="polls-page">
      <div className="section-header">
        <h2>Vibe Polls</h2>
        <span className="polls-subtitle">Vote for your favorites</span>
      </div>

      {polls.map(poll => {
        const m = moods[poll.mood];
        const hasVoted = votedPolls.has(poll._id);
        const totalVotes = poll.totalVotes || 1;

        return (
          <div key={poll._id} className="poll-card fade-in-up">
            <div className="poll-header">
              <span className="poll-mood-emoji">{m?.emoji || '?'}</span>
              <div>
                <div className="poll-question">{poll.question}</div>
                <div className="poll-meta">{poll.totalVotes} votes</div>
              </div>
            </div>

            <div className="poll-options">
              {poll.options.map(opt => {
                const pct = Math.round((opt.votes / totalVotes) * 100);
                return (
                  <button
                    key={opt.id}
                    className={`poll-option ${hasVoted ? 'voted' : ''}`}
                    onClick={() => handleVote(poll._id, opt.id)}
                    disabled={hasVoted}
                  >
                    <div className="poll-option-fill" style={{ width: hasVoted ? `${pct}%` : '0%' }} />
                    <div className="poll-option-content">
                      <span className="poll-option-title">{opt.title}</span>
                      <span className="poll-option-cat">{opt.category}</span>
                      {hasVoted && <span className="poll-option-pct">{pct}%</span>}
                    </div>
                  </button>
                );
              })}
            </div>
          </div>
        );
      })}
    </div>
  );
}

export default VibePolls;
