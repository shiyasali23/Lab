import React, { useRef, useEffect } from "react";
import Chart from "chart.js/auto";

const NutrientsGraph = ({ data }) => {
  const chartRef = useRef(null); // Reference to the canvas element
  const chartInstanceRef = useRef(null); // Reference to the Chart.js instance

  useEffect(() => {
    if (!chartRef.current || !data || data.length === 0) return;

    // Extract the nutrients array from the data
    const nutrients = data[0]?.nutrients || [];

    // Sort nutrients by value in ascending order
    const sortedNutrients = [...nutrients].sort((a, b) => a.value - b.value);

    // Extract labels and transform data
    const labels = sortedNutrients.map((nutrient) => nutrient.name);
    const chartData = sortedNutrients.map((_, index) => index + 1); // Use index+1 for y-axis data

    const ctx = chartRef.current.getContext("2d"); // Get the context for the canvas

    // Clean up the previous chart instance if it exists
    if (chartInstanceRef.current) {
      chartInstanceRef.current.destroy();
    }

    // Create the new chart instance
    chartInstanceRef.current = new Chart(ctx, {
      type: "bar", // Chart type: 'bar'
      data: {
        labels: labels, // X-axis labels (nutrient names)
        datasets: [
          {
            label: `100 gram ${data[0].name ? data[0].name : ""} `, 
            data: chartData, // Y-axis data (index + 1)
            backgroundColor: "rgba(75, 192, 192, 0.2)", // Background color of bars
            borderColor: "rgba(75, 192, 192, 1)", // Border color of bars
            borderWidth: 1, // Border width of bars
            barThickness: 5, // Reduce bar thickness
            borderRadius: 5, // Bar corner radius
          },
        ],
      },
      options: {
        indexAxis: "x", // Set the chart orientation to vertical
        responsive: true, // Make the chart responsive
        maintainAspectRatio: false, // Maintain the aspect ratio
        plugins: {
          tooltip: {
            enabled: true, // Enable tooltips
            callbacks: {
                label: (context) => {
                    // Access the nutrient name and value from the data
                    const nutrientName = labels[context.dataIndex];
                    const nutrientValue = chartData[context.dataIndex];
                    return `${nutrientName}: ${nutrientValue}`; // Display nutrient name and value
                  }, // Customize tooltip label
            },
            backgroundColor: "rgba(0, 0, 0, 0.8)", // Tooltip background color
            titleFont: {
              size: 8, // Font size for the title
            },
            bodyFont: {
              size: 8, // Font size for the body
            },
          },
        },
        scales: {
          x: {
            display: true, // Display the x-axis
            beginAtZero: true, // Start x-axis at zero
            grid: {
              display: false, // Hide the vertical grid lines
            },
          },
          y: {
            display: false, // Hide the y-axis
            grid: {
              display: false, // Hide the grid lines on the y-axis
            },
          },
        },
      },
    });

    // Cleanup on component unmount
    return () => {
      if (chartInstanceRef.current) {
        chartInstanceRef.current.destroy();
      }
    };
  }, [data]); // Update when `data` changes

  return (
    <div style={{ width: "100%", height: `241px`}} className="p-0 d-flex flex-column justify-content-center align-items-center">
      <canvas className="p-0" style={{ width: "100%", height: `100%`}} ref={chartRef} /> 
    </div>
  );
};


export default NutrientsGraph;
