// StatsGraph.js
import React from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid } from 'recharts';
import './StatsGraph.css';
import CalenderIcon from '../assets/calender_icon.svg'
const data = [
  { name: 'M', links: 5 },
  { name: 'T', links: 6 },
  { name: 'W', links: 7 },
  { name: 'T', links: 10 },
  { name: 'F', links: 15 },
  { name: 'S', links: 10 },
  { name: 'S', links: 12 },
];

const StatsGraph = () => {
  return (
    <div className="stats-card">
      <div className="stats-header">
        <div className="stats-title">
          <img className="stats-icon" src={CalenderIcon}></img> {/* Replace with an actual icon if available */}
          <span>Stats</span>
        </div>
        <span className="stats-subtitle">This week</span>
      </div>
      <ResponsiveContainer width="100%" height={150}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="links" stroke="#6200ea" strokeWidth={2} dot={{ r: 6 }} activeDot={{ r: 8 }} />
        </LineChart>
      </ResponsiveContainer>
      <div className="stats-footer">
        Links posted
      </div>
    </div>
  );
};

export default StatsGraph;
