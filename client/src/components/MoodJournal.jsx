import { useState, useEffect } from 'react';
import { getJournal, addJournal, deleteJournal } from '../api';

function MoodJournal({ moods, currentMood }) {
  const [entries, setEntries] = useState([]);
  const [note, setNote] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadJournal();
  }, []);

  const loadJournal = async () => {
    try {
      const res = await getJournal();
      setEntries(res.data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleAdd = async () => {
    if (!note.trim()) return;
    try {
      const res = await addJournal({ mood: currentMood || 'calm', note: note.trim() });
      setEntries(prev => [res.data, ...prev]);
      setNote('');
    } catch (err) {
      console.error(err);
    }
  };

  const handleDelete = async (id) => {
    try {
      await deleteJournal(id);
      setEntries(prev => prev.filter(e => e._id !== id));
    } catch (err) {
      console.error(err);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleAdd();
    }
  };

  return (
    <div className="journal-page">
      <div className="section-header">
        <h2>Mood Journal</h2>
        <span className="journal-count">{entries.length} entries</span>
      </div>

      <div className="journal-input-card">
        {currentMood && moods[currentMood] && (
          <div className="journal-current-mood">
            <span className="journal-mood-emoji">{moods[currentMood].emoji}</span>
            <span className="journal-mood-label">{moods[currentMood].label}</span>
          </div>
        )}
        <textarea
          className="journal-textarea"
          value={note}
          onChange={(e) => setNote(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Write about how you're feeling..."
          rows="3"
        />
        <div className="journal-input-footer">
          <span className="journal-char-count">{note.length}</span>
          <button className="btn-analyze" onClick={handleAdd} disabled={!note.trim()}>
            Save entry
          </button>
        </div>
      </div>

      {loading && <div className="empty-state"><h3>Loading...</h3></div>}

      {!loading && entries.length === 0 && (
        <div className="empty-state">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
            <path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14,2 14,8 20,8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10,9 9,9 8,9"/>
          </svg>
          <h3>No journal entries yet</h3>
          <p>Write about how you're feeling to start your journal.</p>
        </div>
      )}

      <div className="journal-entries">
        {entries.map((entry, i) => {
          const m = moods[entry.mood];
          const time = new Date(entry.createdAt).toLocaleString();
          return (
            <div key={entry._id} className="journal-entry fade-in-up" style={{ animationDelay: `${i * 0.05}s` }}>
              <div className="journal-entry-header">
                <div className="journal-entry-mood">
                  <span className="journal-entry-emoji">{m?.emoji || '📝'}</span>
                  <span className="journal-entry-label">{m?.label || entry.mood}</span>
                </div>
                <div className="journal-entry-actions">
                  <span className="journal-entry-time">{time}</span>
                  <button className="journal-delete-btn" onClick={() => handleDelete(entry._id)} title="Delete">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                      <polyline points="3,6 5,6 21,6"/><path d="M19 6v14a2 2 0 01-2 2H7a2 2 0 01-2-2V6m3 0V4a2 2 0 012-2h4a2 2 0 012 2v2"/>
                    </svg>
                  </button>
                </div>
              </div>
              <p className="journal-entry-note">{entry.note}</p>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default MoodJournal;
