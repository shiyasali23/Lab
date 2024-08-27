import React, { useRef, useEffect } from 'react';
import Chart from 'chart.js/auto';

const HealthScoreGraph = ({ healthScore }) => {
  const chartRef = useRef(null);
  const chartInstance = useRef(null);

  useEffect(() => {
    if (!Array.isArray(healthScore) || healthScore.length === 0) {
      return; // Exit early if healthScore is not a valid array
    }

    const ctx = chartRef.current?.getContext('2d');
    if (!ctx) return; // Exit if canvas context is not available

    if (chartInstance.current) {
      chartInstance.current.destroy();
    }

    chartInstance.current = new Chart(ctx, {
      type: 'line',
      data: {
        labels: healthScore.map((score) =>
          new Date(score.created).toLocaleDateString('en-GB')
        ),
        datasets: [
          {
            label: 'Health Score',
            data: healthScore.map((score) => score.health_score),
            borderColor: 'rgba(75,192,192,1)',
            backgroundColor: 'rgba(75,192,192,0.2)',
            tension: 0.4,
            fill: true,
            pointBackgroundColor: 'rgba(75,192,192,1)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgba(75,192,192,1)',
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: {
            title: {
              display: false,
            },
            ticks: {
              callback: function (value, index, ticks) {
                return new Date(value).toLocaleDateString('en-GB');
              },
            },
          },
          y: {
            title: {
              display: true,
              text: 'Health Score',
            },
            beginAtZero: true,
            ticks: {
              display: false, // Remove health scores from y-axis
            },
          },
        },
        plugins: {
          legend: {
            display: false, // Remove health score label from top
          },
        },
      },
    });

    // Cleanup on component unmount
    return () => {
      if (chartInstance.current) {
        chartInstance.current.destroy();
      }
    };
  }, [healthScore]);

  return <canvas ref={chartRef} style={{ width: '100%', height: '300px' }} />;
};

export default HealthScoreGraph;
