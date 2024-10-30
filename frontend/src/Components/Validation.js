import React from 'react'; 
import { Line } from 'react-chartjs-2'; 

const Visualization = ({ data }) => {
    const chartData = {
      labels: data.timestamps,
      datasets: [
        {
          label: 'Temperature Trend',
          data: data.temperatures,
          fill: false,
          borderColor: 'blue',
        },
      ],
    };
  
    return <Line data={chartData} />;
  };
  
  export default Visualization;