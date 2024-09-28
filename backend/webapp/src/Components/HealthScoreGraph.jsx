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
          new Date(score.created).toLocaleDateString('en-GB', {
            day: '2-digit',
            month: '2-digit',
            year: '2-digit',
          })
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
        layout: {
          padding: {
            left: 0,
            right: 0,
            top: 20,
            bottom: 20,
          },
        },
        scales: {
          x: {
            title: {
              display: false,
            },
            ticks: {
              color: '#F7FAFC', // Set x-axis tick font color
            },
            grid: {
              borderColor: '#F7FAFC', // Set grid line color
            },
            offset: true, // Offset the axis to ensure space
          },
          y: {
            title: {
              display: true,
              color: '#F7FAFC', // Set y-axis title color
              padding: { top: 20 },
            },
            beginAtZero: true,
            ticks: {
              color: '#F7FAFC', // Set y-axis tick font color
            },
            grid: {
              borderColor: '#F7FAFC', // Set grid line color
            },
            padding: {
              top: 20, // Add space between the top border and axis
              bottom: 20, // Add space between the bottom border and axis
            },
          },
        },
        plugins: {
          legend: {
            display: true,
            position: 'top', // Move legend to the top
            labels: {
              color: '#F7FAFC', // Set legend label color
            },
          },
        },
        color: '#F7FAFC', // Set general font color
      },
    });

    // Cleanup on component unmount
    return () => {
      if (chartInstance.current) {
        chartInstance.current.destroy();
      }
    };
  }, [healthScore]);

  return (
    <div style={{ backgroundColor: '#192232', width: '100%', height: '100%', position: 'relative' }}>
      <canvas ref={chartRef} style={{ width: '100%', height: '100%' }} />
    </div>
  );
};

export default HealthScoreGraph;
