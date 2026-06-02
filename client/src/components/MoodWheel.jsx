import { useState, useRef } from 'react';

function MoodWheel({ moods, onSelect }) {
  const [spinning, setSpinning] = useState(false);
  const [result, setResult] = useState(null);
  const wheelRef = useRef(null);
  const rotationRef = useRef(0);

  const moodKeys = Object.keys(moods);
  const sliceAngle = 360 / moodKeys.length;

  const spin = () => {
    if (spinning) return;
    setSpinning(true);
    setResult(null);

    const extraRotation = 1440 + Math.random() * 720;
    rotationRef.current += extraRotation;

    if (wheelRef.current) {
      wheelRef.current.style.transition = 'transform 4s cubic-bezier(0.17, 0.67, 0.12, 0.99)';
      wheelRef.current.style.transform = `rotate(${rotationRef.current}deg)`;
    }

    setTimeout(() => {
      const normalizedAngle = rotationRef.current % 360;
      const index = Math.floor(((360 - normalizedAngle + sliceAngle / 2) % 360) / sliceAngle);
      const selectedMood = moodKeys[index % moodKeys.length];
      setResult(selectedMood);
      setSpinning(false);
      if (onSelect) onSelect(selectedMood, 'wheel');
    }, 4200);
  };

  const colors = moodKeys.map(k => moods[k]?.color || '#a78bfa');

  return (
    <div className="wheel-container">
      <div className="wheel-wrapper">
        <div className="wheel-pointer">▼</div>
        <div className="wheel" ref={wheelRef}>
          <svg viewBox="0 0 300 300" width="300" height="300">
            {moodKeys.map((key, i) => {
              const startAngle = i * sliceAngle - 90;
              const endAngle = startAngle + sliceAngle;
              const startRad = (startAngle * Math.PI) / 180;
              const endRad = (endAngle * Math.PI) / 180;
              const x1 = 150 + 140 * Math.cos(startRad);
              const y1 = 150 + 140 * Math.sin(startRad);
              const x2 = 150 + 140 * Math.cos(endRad);
              const y2 = 150 + 140 * Math.sin(endRad);
              const largeArc = sliceAngle > 180 ? 1 : 0;
              const midAngle = ((startAngle + endAngle) / 2 * Math.PI) / 180;
              const textX = 150 + 90 * Math.cos(midAngle);
              const textY = 150 + 90 * Math.sin(midAngle);

              return (
                <g key={key}>
                  <path
                    d={`M150,150 L${x1},${y1} A140,140 0 ${largeArc},1 ${x2},${y2} Z`}
                    fill={colors[i]}
                    stroke="#0a0a0f"
                    strokeWidth="2"
                    opacity="0.85"
                  />
                  <text x={textX} y={textY} textAnchor="middle" dominantBaseline="middle" fontSize="24" fill="white">
                    {moods[key]?.emoji}
                  </text>
                </g>
              );
            })}
            <circle cx="150" cy="150" r="30" fill="#0a0a0f" stroke="#2a2a3a" strokeWidth="2" />
            <text x="150" y="150" textAnchor="middle" dominantBaseline="middle" fontSize="12" fill="white" fontWeight="600">
              SPIN
            </text>
          </svg>
        </div>
      </div>

      <button className="btn-wheel-spin" onClick={spin} disabled={spinning}>
        {spinning ? 'Spinning...' : 'Spin the Wheel'}
      </button>

      {result && moods[result] && (
        <div className="wheel-result fade-in-up">
          <span className="wheel-result-emoji">{moods[result].emoji}</span>
          <span className="wheel-result-label">{moods[result].label}</span>
        </div>
      )}
    </div>
  );
}

export default MoodWheel;
