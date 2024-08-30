import React, { useRef, useEffect } from 'react';
import Chart from 'chart.js/auto';

const BarGraph = ({ foodScore }) => {
  const chartRef = useRef(null);
  const chartInstanceRef = useRef(null);

  useEffect(() => {
    if (!chartRef.current) return;

    // Sort food scores by score in descending order
    const sortedScores = [...foodScore].sort((a, b) => b.score - a.score);

    // Extract labels and data
    const labels = sortedScores.map(food => food.food_name);
    const data = sortedScores.map(food => food.score);

    const ctx = chartRef.current.getContext('2d');

    // Clean up the previous chart instance if it exists
    if (chartInstanceRef.current) {
      chartInstanceRef.current.destroy();
    }

    // Create the new chart instance
    chartInstanceRef.current = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'Food Score',
          data: data,
          backgroundColor: data.map(value => `rgba(${255 - value * 50}, ${value * 50}, 0, 0.7)`),
          borderColor: 'rgba(0, 0, 0, 0.1)',
          borderWidth: 1,
          barThickness: 'flex', // Ensures the bars have consistent thickness
          
        }],
      },
      options: {
        indexAxis: 'y',
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: false,
          },
          tooltip: {
            callbacks: {
              label: (context) => `Score: ${context.raw.toFixed(2)}`,
            },
          },
        },
        scales: {
          x: {
            beginAtZero: true,
            grid: {
              display: false, // Remove grid lines for x-axis
            },
          },
          y: {
            grid: {
              display: false, // Remove grid lines for y-axis
            },
            ticks: {
              font: {
                weight: 'bold', // Make the food names bolder
              },
              padding: 10, // Add padding between the labels and the bars
            },
          },
        },
        layout: {
          padding: {
            left: 0,
            right: 0,
            top: 0,
            bottom: 0,
          },
        },
      },
    });

    // Cleanup function to destroy the chart instance
    return () => {
      if (chartInstanceRef.current) {
        chartInstanceRef.current.destroy();
      }
    };
  }, [foodScore]);

  return <canvas ref={chartRef} style={{ width: '100%', height: '100%' }} />;
};

export default BarGraph;
