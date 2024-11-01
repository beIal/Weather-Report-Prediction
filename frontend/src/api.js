import axios from 'axios'; 

const API_URL = 'http://localhost:8000'; 

export const classifyWeather = async (inputData) => { 
    try { 
        const response = await axios.post('${API_URL}/predict/classification', inputData); 
        return response.data.prediction;
    } catch (error) { 
        throw error.response ? error.response.data.detail : 'Network error';
    }
}; 

export const regressWeather = async (inputData) => { 
    try { 
        const response = await axios.post('${API_URL}/predict/regression', inputData); 
        return response.data.prediction;
    } catch (error) { 
        throw error.response ? error.response.data.detail : 'Network error';
    }
};