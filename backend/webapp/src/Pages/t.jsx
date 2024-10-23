import React, { useRef, useEffect, useState, } from "react";
import Chart from "chart.js/auto";

const BarGraph = ({ scoreData, passedHeight }) => {

  
  const [chartData, setChartData] = useState(null);
  const chartRef = useRef(null); // Reference to the canvas element
  const chartInstanceRef = useRef(null); // Reference to the Chart.js instance


  useEffect(() => {
    if (!chartRef.current) return;


    // Extract labels and data
    const labels = scoreData.map((food) => food.food_name);
    const data = scoreData.map((food) => food.score);

    const ctx = chartRef.current.getContext("2d"); // Get the context for the canvas

    // Clean up the previous chart instance if it exists
    if (chartInstanceRef.current) {
      chartInstanceRef.current.destroy();
    }

    // Create the new chart instance
    chartInstanceRef.current = new Chart(ctx, {
      type: "bar", // Chart type: 'bar'
      data: {
        labels: labels, // X-axis labels (food names)
        datasets: [
          {
            label: "Food Score", // Label for the dataset
            data: data, // Y-axis data (food scores)
            backgroundColor: data.map(
              (value) => `rgba(${255 - value * 50}, ${value * 50}, 0, 0.7)`
            ), // Background color of bars
            borderColor: "rgba(0, 0, 0, 0.1)", // Border color of bars
            borderWidth: 0, // Border width of bars
            barThickness: "6", // Bar thickness ('flex' adjusts thickness to fit the chart area)
            maxBarThickness: undefined, // Maximum bar thickness (default is undefined)
            minBarLength: 0, // Minimum bar length (default is 0)
            borderRadius: 0, // Bar corner radius (default is 0)
            borderSkipped: "bottom", // Border not drawn on the specified edge (default is 'bottom')
          },
        ],
      },
      options: {
        indexAxis: "y", // Set the chart orientation to horizontal
        responsive: true, // Make the chart responsive (default is true)
        maintainAspectRatio: false, // Maintain the aspect ratio (default is true)
        plugins: {
          legend: {
            display: false, // Display legend (default is true)
            position: "top", // Position of the legend (default is 'top')
            align: "center", // Alignment of the legend (default is 'center')
            labels: {
              boxWidth: 40, // Width of the legend box (default is 40)
              padding: 10, // Padding between legend items (default is 10)
              color: "#666", // Color of legend text (default is '#666')
              font: {
                family: "'Helvetica Neue', 'Helvetica', 'Arial', sans-serif", // Font family (default)
                size: 12, // Font size (default is 12)
                style: "normal", // Font style (default is 'normal')
                lineHeight: 1.2, // Line height (default is 1.2)
                weight: null, // Font weight (default is null)
              },
            },
          },
          tooltip: {
            enabled: true, // Enable tooltips (default is true)
            mode: "nearest", // Interaction mode (default is 'nearest')
            intersect: true, // Tooltip appears when hovering over an item (default is true)
            callbacks: {
              label: (context) => `Score: ${context.raw.toFixed(2)}`, // Customize tooltip label
            },
            backgroundColor: "rgba(0, 0, 0, 0.8)", // Tooltip background color (default is 'rgba(0, 0, 0, 0.8)')
            titleFont: {
              family: "'Helvetica Neue', 'Helvetica', 'Arial', sans-serif", // Font family for the title (default)
              size: 12, // Font size for the title (default is 12)
              style: "bold", // Font style for the title (default is 'bold')
              weight: null, // Font weight for the title (default is null)
              lineHeight: 1.2, // Line height for the title (default is 1.2)
            },
            titleColor: "#fff", // Tooltip title color (default is '#fff')
            bodyFont: {
              family: "'Helvetica Neue', 'Helvetica', 'Arial', sans-serif", // Font family for the body (default)
              size: 12, // Font size for the body (default is 12)
              style: "normal", // Font style for the body (default is 'normal')
              weight: null, // Font weight for the body (default is null)
              lineHeight: 1.2, // Line height for the body (default is 1.2)
            },
            bodyColor: "#fff", // Tooltip body color (default is '#fff')
          },
        },
        scales: {
          x: {
            display: false, // Hide the x-axis
            beginAtZero: true, // Start x-axis at zero (default is true)
            grid: {
              display: false, // Hide x-axis grid lines (default is true)
              color: "rgba(0, 0, 0, 0.1)", // Color of grid lines (default is 'rgba(0, 0, 0, 0.1)')
              lineWidth: 1, // Grid line width (default is 1)
              drawBorder: false, // Draw border on the axis (default is true)
              drawOnChartArea: true, // Draw grid lines on the chart area (default is true)
              drawTicks: true, // Draw ticks on the axis (default is true)
              tickLength: 8, // Length of ticks (default is 8)
              tickColor: "#666", // Color of ticks (default is '#666')
              tickWidth: 1, // Width of ticks (default is 1)
              offset: false, // Offset grid lines (default is false)
            },
            ticks: {
              display: false, // Hide x-axis ticks
              autoSkip: true, // Automatically skip ticks (default is true)
              maxRotation: 50, // Maximum rotation for ticks (default is 50)
              minRotation: 0, // Minimum rotation for ticks (default is 0)
              mirror: false, // Flip the tick labels (default is false)
              padding: 3, // Padding between ticks and chart (default is 3)
              align: "center", // Alignment of ticks (default is 'center')
              crossAlign: "near", // Cross alignment of ticks (default is 'near')
            },
          },
          y: {
            display: true, // Display the y-axis (default is true)
            grid: {
              display: false, // Hide y-axis grid lines (default is true)
              color: "rgba(0, 0, 0, 0.1)", // Color of grid lines (default is 'rgba(0, 0, 0, 0.1)')
              lineWidth: 1, // Grid line width (default is 1)
              drawBorder: false, // Draw border on the axis (default is true)
              drawOnChartArea: true, // Draw grid lines on the chart area (default is true)
              drawTicks: true, // Draw ticks on the axis (default is true)
              tickLength: 8, // Length of ticks (default is 8)
              tickColor: "#666", // Color of ticks (default is '#666')
              tickWidth: 1, // Width of ticks (default is 1)
              offset: false, // Offset grid lines (default is false)
            },
            ticks: {
              display: true, // Display y-axis ticks (default is true)
              autoSkip: true, // Automatically skip ticks (default is true)
              maxRotation: 50, // Maximum rotation for ticks (default is 50)
              minRotation: 0, // Minimum rotation for ticks (default is 0)
              mirror: false, // Flip the tick labels (default is false)
              padding: 10, // Padding between ticks and chart (default is 3)
              align: "center", // Alignment of ticks (default is 'center')
              crossAlign: "near", // Cross alignment of ticks (default is 'near')
              font: {
                family: "'Helvetica Neue', 'Helvetica', 'Arial', sans-serif", // Font family for y-axis labels (default)
                size: 12, // Font size for y-axis labels (default is 12)
                style: "normal", // Font style for y-axis labels (default is 'normal')
                lineHeight: 1.2, // Line height for y-axis labels (default is 1.2)
                weight: "bold", // Font weight for y-axis labels (customized to bold)
              },
            },
          },
        },
        layout: {
          padding: {
            left: 0, // Padding on the left side of the chart (default is 0)
            right: 0, // Padding on the right side of the chart (default is 0)
            top: 0, // Padding on the top of the chart (default is 0)
            bottom: 0, // Padding on the bottom of the chart (default is 0)
          },
        },
        animation: {
          duration: 1000, // Animation duration in milliseconds (default is 1000)
          easing: "easeOutQuart", // Easing function for the animation (default is 'easeOutQuart')
          delay: 0, // Delay before starting the animation (default is 0)
          loop: false, // Whether to loop the animation (default is false)
        },
        interaction: {
          mode: "nearest", // Interaction mode (default is 'nearest')
          intersect: true, // Interaction only when the cursor intersects an element (default is true)
        },
        elements: {
          bar: {
            backgroundColor: "rgba(0, 0, 0, 0.1)", // Default background color for bars
            borderColor: "rgba(0, 0, 0, 0.1)", // Default border color for bars
            borderWidth: 0, // Default border width for bars
            borderRadius: 0, // Default border radius for bars
            borderSkipped: "bottom", // Default skipped border (bottom)
            barThickness: "flex", // Default bar thickness ('flex' to adjust based on chart size)
            maxBarThickness: undefined, // Maximum bar thickness (default is undefined)
            minBarLength: 0, // Minimum bar length (default is 0)
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
  }, [scoreData]);

  return (
    <div style={{ width: "100%", height: `${scoreData.length * 32}px` }}>
      <canvas
        ref={chartRef}
        style={{ width: "100%" }}
      />
    </div>
  );
};

export default BarGraph;
