import React, { useEffect, useRef } from "react";
import { Chart, registerables } from "chart.js";
import CenteredMessage from "./CenteredMessage";

Chart.register(...registerables);

const ProbabilityBars = ({ sortedProbabilities }) => {
  const chartRef = useRef(null);
  
  useEffect(() => {
    if (chartRef.current) {
      const ctx = chartRef.current.getContext("2d");
      const labels = Object.keys(sortedProbabilities);
      const dataValues = Object.values(sortedProbabilities);

      // Create the chart
      const chartInstance = new Chart(ctx, {
        type: "bar",
        data: {
          labels: labels,
          datasets: [
            {
              label: "Probability (%)",
              data: dataValues,
              backgroundColor: "rgba(75, 192, 192, 0.6)",
              borderColor: "rgba(75, 192, 192, 1)",
              borderWidth: 1,
            },
          ],
        },
        options: {
          indexAxis: "y", // Make bars horizontal
          responsive: true,
          maintainAspectRatio: false, // Allow the chart to fill the container
          plugins: {
            legend: {
              display: false,
            },
            tooltip: {
              callbacks: {
                label: (context) => {
                  return `${context.label}: ${context.raw.toFixed(2)}%`;
                },
              },
            },
          },
          scales: {
            x: {
              beginAtZero: true,
              max: Math.max(...dataValues) + 10, // Add some padding
              grid: {
                display: false, // Remove grid lines from x-axis
              },
            },
            y: {
              categoryPercentage: 0.5, // Controls the width of the bars
              barPercentage: 0.9, // Controls the thickness of the bars
              ticks: {
                font: {
                  size: 14, // Increase font size of y-axis labels
                  weight: 'bold', // Make y-axis labels bold
                },
              },
              grid: {
                display: false, // Remove grid lines from y-axis
              },
            },
          },
        },
      });

      // Cleanup on unmount
      return () => {
        chartInstance.destroy();
      };
    }
  }, [sortedProbabilities]);

  return (
    <div className="w-100 h-100 d-flex justify-content-center align-items-center">
      <canvas ref={chartRef} style={{ height: "100%", width: "100%" }} />
    </div>
  );
};

export default ProbabilityBars;
