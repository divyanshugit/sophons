import React from 'react';
import { Doughnut } from 'react-chartjs-2';
import { Chart, ArcElement, Tooltip, Legend } from 'chart.js';
import './TopicInventoryChart.css'; // Import the CSS file for styling

Chart.register(ArcElement, Tooltip, Legend);

const TopicInventoryChart = () => {
  const data = {
    labels: ['AI', 'LLMs', 'Security', 'Agents'],
    datasets: [
      {
        data: [48, 15, 22, 15], // The percentages for each topic
        backgroundColor: ['#D6A3FF', '#B48DF9', '#9E77ED', '#7C57C1'], // The colors for each segment
        borderWidth: 0,
      },
    ],
  };

  const options = {
    cutout: '70%',
    plugins: {
      tooltip: {
        enabled: false,
      },
      legend: {
        display: false,
      },
    },
  };

  return (
    <div className="topic-inventory-chart">
      <h3>Topic Inventory</h3>
      <div className="doughnut-container">
        <Doughnut data={data} options={options} />
        <div className="chart-text">
          <span>48%</span>
          <br />
          of inventory holds AI
        </div>
      </div>
      <div className="chart-legend">
        <div className='chart-legent-indi'><span style={{ backgroundColor: '#D6A3FF' }} ></span> AI</div>
        <div className='chart-legent-indi'><span style={{ backgroundColor: '#B48DF9' }}></span> LLMs</div>
        <div className='chart-legent-indi'><span style={{ backgroundColor: '#9E77ED' }}></span> Security</div>
        <div className='chart-legent-indi'><span style={{ backgroundColor: '#7C57C1' }}></span> Agents</div>
      </div>
    </div>
  );
};

export default TopicInventoryChart;
