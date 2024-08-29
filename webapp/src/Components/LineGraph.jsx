import React, { useRef, useEffect } from 'react';
import Chart from 'chart.js/auto';
import annotationPlugin from 'chartjs-plugin-annotation'; // Import the plugin

// Register the annotation plugin
Chart.register(annotationPlugin);

const LineGraph = ({ data }) => {
  const chartRef = useRef(null);
  const chartInstance = useRef(null);

  useEffect(() => {
    const dataKey = Object.keys(data)[0];
    const chartData = data[dataKey];

    if (!chartData || !Array.isArray(chartData.values) || chartData.values.length === 0) {
      console.error("No valid data provided", data);
      return;
    }

    const ctx = chartRef.current?.getContext('2d');
    if (!ctx) {
      console.error("Canvas context is not available");
      return;
    }

    if (chartInstance.current) {
      chartInstance.current.destroy();
    }

    const values = chartData.values.map(item => item.value);
    const dates = chartData.values.map(item => new Date(item.created).toLocaleDateString('en-GB', {
      day: '2-digit',
      month: '2-digit',
      year: '2-digit',
    }));

    const healthyMin = chartData.healthy_min;
    const healthyMax = chartData.healthy_max;
    const healthyMean = (healthyMin + healthyMax) / 2;

    chartInstance.current = new Chart(ctx, {
      type: 'line',
      data: {
        labels: dates,
        datasets: [
          {
            label: dataKey,
            data: values,
            borderColor: 'rgba(75,192,192,1)',
            backgroundColor: 'rgba(75,192,192,0.2)',
            tension: 0.4,
            fill: false,
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
            ticks: {
              color: '#F7FAFC',
            },
            grid: {
              borderColor: '#F7FAFC',
            },
            offset: true,
          },
          y: {
            title: {
              display: true,
            },
            suggestedMin: Math.min(healthyMin, ...values) - 10,
            suggestedMax: Math.max(healthyMax, ...values) + 10,
            ticks: {
              color: '#F7FAFC',
            },
            grid: {
              borderColor: '#F7FAFC',
            },
            padding: {
              top: 20,
              bottom: 20,
            },
          },
        },
        plugins: {
          legend: {
            display: true,
            position: 'top',
            labels: {
              color: '#F7FAFC',
            },
          },
          annotation: {
            annotations: {
              line1: {
                type: 'line',
                yMin: healthyMin,
                yMax: healthyMin,
                borderColor: 'rgba(255, 99, 132, 0.5)',
                borderWidth: 2,
                borderDash: [10, 5],
                label: {
                  content: 'Healthy Min',
                  enabled: true,
                  position: 'left'
                }
              },
              line2: {
                type: 'line',
                yMin: healthyMax,
                yMax: healthyMax,
                borderColor: 'rgba(54, 162, 235, 0.5)',
                borderWidth: 2,
                borderDash: [10, 5],
                label: {
                  content: 'Healthy Max',
                  enabled: true,
                  position: 'left'
                }
              },
              line3: {
                type: 'line',
                yMin: healthyMean,
                yMax: healthyMean,
                borderColor: 'rgba(75, 192, 192, 0.5)',
                borderWidth: 2,
                label: {
                  content: 'Healthy Mean',
                  enabled: true,
                  position: 'left'
                }
              }
            }
          }
        },
      },
    });

    return () => {
      if (chartInstance.current) {
        chartInstance.current.destroy();
      }
    };
  }, [data]);

  return (
    <div style={{ backgroundColor: '#192232', width: '100%', height: '300px', position: 'relative' }}>
      <canvas ref={chartRef} style={{ width: '100%', height: '100%' }} />
    </div>
  );
};

export default LineGraph;
