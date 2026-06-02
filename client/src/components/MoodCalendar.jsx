import { useState, useEffect } from 'react';
import { getCalendar } from '../api';

function MoodCalendar({ moods }) {
  const [calendar, setCalendar] = useState({});
  const [hoveredDate, setHoveredDate] = useState(null);

  useEffect(() => {
    getCalendar(90).then(res => setCalendar(res.data.calendar)).catch(console.error);
  }, []);

  const getWeeks = () => {
    const today = new Date();
    const weeks = [];
    const startDate = new Date(today);
    startDate.setDate(startDate.getDate() - 89);

    // Align to start of week (Monday)
    const day = startDate.getDay();
    startDate.setDate(startDate.getDate() - (day === 0 ? 6 : day - 1));

    let current = new Date(startDate);
    while (current <= today) {
      const week = [];
      for (let i = 0; i < 7; i++) {
        const dateStr = current.toISOString().split('T')[0];
        const isFuture = current > today;
        week.push({
          date: dateStr,
          data: calendar[dateStr] || null,
          isFuture,
        });
        current.setDate(current.getDate() + 1);
      }
      weeks.push(week);
    }
    return weeks;
  };

  const getColor = (data) => {
    if (!data) return 'var(--surface-2)';
    const m = moods[data.dominant];
    return m ? m.color + '44' : 'var(--accent)';
  };

  const getOpacity = (data) => {
    if (!data) return 0.15;
    return Math.min(0.3 + data.count * 0.2, 1);
  };

  const weeks = getWeeks();
  const dayLabels = ['M', 'T', 'W', 'T', 'F', 'S', 'S'];

  return (
    <div className="calendar-page">
      <div className="section-header">
        <h2>Mood Calendar</h2>
        <span className="calendar-subtitle">Last 90 days</span>
      </div>

      <div className="calendar-grid-wrapper">
        <div className="calendar-day-labels">
          {dayLabels.map((d, i) => (
            <span key={i} className="calendar-day-label">{d}</span>
          ))}
        </div>
        <div className="calendar-grid">
          {weeks.map((week, wi) => (
            <div key={wi} className="calendar-week">
              {week.map((day, di) => (
                <div
                  key={di}
                  className={`calendar-cell ${day.isFuture ? 'future' : ''} ${day.data ? 'has-data' : ''}`}
                  style={{
                    background: day.data ? getColor(day.data) : 'var(--surface-2)',
                    opacity: day.isFuture ? 0.1 : (day.data ? getOpacity(day.data) : 0.15),
                  }}
                  onMouseEnter={() => setHoveredDate(day)}
                  onMouseLeave={() => setHoveredDate(null)}
                />
              ))}
            </div>
          ))}
        </div>
      </div>

      {hoveredDate && hoveredDate.data && (
        <div className="calendar-tooltip fade-in-up">
          <span className="calendar-tooltip-emoji">
            {moods[hoveredDate.data.dominant]?.emoji || '?'}
          </span>
          <div>
            <div className="calendar-tooltip-date">{hoveredDate.date}</div>
            <div className="calendar-tooltip-mood">
              {moods[hoveredDate.data.dominant]?.label || hoveredDate.data.dominant} — {hoveredDate.data.count} check-in{hoveredDate.data.count > 1 ? 's' : ''}
            </div>
          </div>
        </div>
      )}

      <div className="calendar-legend">
        <span className="calendar-legend-label">Less</span>
        {[0.15, 0.3, 0.5, 0.7, 1].map((op, i) => (
          <div key={i} className="calendar-legend-cell" style={{ background: 'var(--accent)', opacity: op }} />
        ))}
        <span className="calendar-legend-label">More</span>
      </div>
    </div>
  );
}

export default MoodCalendar;
