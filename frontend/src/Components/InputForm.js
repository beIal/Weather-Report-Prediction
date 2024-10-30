import React, { uesState } from 'react'; 
import { getPrediction } from '../api'; 
  
const InputForm = ({ setPrediction }) => {
    const [temperature, setTemperature] = useState('');
    const [humidity, setHumidity] = useState('');
    const [error, setError] = useState('');
  
    const handleSubmit = async (e) => {
      e.preventDefault();
      if (!temperature || !humidity) {
        setError('Please provide both temperature and humidity.');
        return;
      }
      try {
        const prediction = await getPrediction({ temperature, humidity });
        setPrediction(prediction);
      } catch (error) {
        setError(error);
      }
    };
  
    return (
      <form onSubmit={handleSubmit}>
        <input
          type="number"
          placeholder="Temperature"
          value={temperature}
          onChange={(e) => setTemperature(e.target.value)}
        />
        <input
          type="number"
          placeholder="Humidity"
          value={humidity}
          onChange={(e) => setHumidity(e.target.value)}
        />
        <button type="submit">Get Prediction</button>
        {error && <div className="error">{error}</div>}
      </form>
    );
  };
  
  export default InputForm;