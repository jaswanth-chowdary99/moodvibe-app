import { useState, useEffect } from 'react';
import { getGoals, addGoal, completeGoal, deleteGoal } from '../api';

function MoodGoals({ moods }) {
  const [goals, setGoals] = useState([]);
  const [description, setDescription] = useState('');
  const [selectedMood, setSelectedMood] = useState('motivated');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadGoals();
  }, []);

  const loadGoals = async () => {
    try {
      const res = await getGoals();
      setGoals(res.data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleAdd = async () => {
    if (!description.trim()) return;
    try {
      const res = await addGoal({ mood: selectedMood, description: description.trim() });
      setGoals(prev => [res.data, ...prev]);
      setDescription('');
    } catch (err) {
      console.error(err);
    }
  };

  const handleComplete = async (id) => {
    try {
      await completeGoal(id);
      setGoals(prev => prev.map(g => g._id === id ? { ...g, completed: true } : g));
    } catch (err) {
      console.error(err);
    }
  };

  const handleDelete = async (id) => {
    try {
      await deleteGoal(id);
      setGoals(prev => prev.filter(g => g._id !== id));
    } catch (err) {
      console.error(err);
    }
  };

  const active = goals.filter(g => !g.completed);
  const completed = goals.filter(g => g.completed);

  return (
    <div className="goals-page">
      <div className="section-header">
        <h2>Mood Goals</h2>
        <span className="goals-count">{active.length} active</span>
      </div>

      <div className="goals-input-card">
        <div className="goals-mood-select">
          {Object.entries(moods).slice(0, 5).map(([key, m]) => (
            <button
              key={key}
              className={`goals-mood-chip ${selectedMood === key ? 'selected' : ''}`}
              onClick={() => setSelectedMood(key)}
            >
              {m.emoji}
            </button>
          ))}
        </div>
        <div className="goals-input-row">
          <input
            type="text"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleAdd()}
            placeholder="Set a mood goal..."
          />
          <button className="btn-analyze" onClick={handleAdd} disabled={!description.trim()}>Add</button>
        </div>
      </div>

      {loading && <div className="empty-state"><h3>Loading...</h3></div>}

      {!loading && goals.length === 0 && (
        <div className="empty-state">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
            <circle cx="12" cy="12" r="10"/><polyline points="12,6 12,12 16,14"/>
          </svg>
          <h3>No goals yet</h3>
          <p>Set a mood goal to track your progress.</p>
        </div>
      )}

      {active.length > 0 && (
        <div className="goals-section">
          <h3 className="goals-section-title">Active</h3>
          {active.map((goal, i) => {
            const m = moods[goal.mood];
            return (
              <div key={goal._id} className="goal-card fade-in-up" style={{ animationDelay: `${i * 0.05}s` }}>
                <span className="goal-emoji">{m?.emoji || '🎯'}</span>
                <span className="goal-desc">{goal.description}</span>
                <div className="goal-actions">
                  <button className="goal-complete-btn" onClick={() => handleComplete(goal._id)} title="Complete">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5"><polyline points="20,6 9,17 4,12"/></svg>
                  </button>
                  <button className="goal-delete-btn" onClick={() => handleDelete(goal._id)} title="Delete">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      )}

      {completed.length > 0 && (
        <div className="goals-section">
          <h3 className="goals-section-title">Completed</h3>
          {completed.map((goal) => {
            const m = moods[goal.mood];
            return (
              <div key={goal._id} className="goal-card completed">
                <span className="goal-emoji">{m?.emoji || '🎯'}</span>
                <span className="goal-desc">{goal.description}</span>
                <span className="goal-check">✓</span>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}

export default MoodGoals;
