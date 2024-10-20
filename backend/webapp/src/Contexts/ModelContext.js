import React, { createContext, useState, useContext, useCallback } from 'react';
import axios from 'axios';

const ModelContext = createContext();

export const ModelProvider = ({ children }) => {
  const [modelLoading, setModelLoading] = useState(false);
  const [predictionLoading, setPredictionLoading] = useState(false);
  const [modelError, setModelError] = useState('');
  const [success, setSuccess] = useState('');
  const [model, setModel] = useState(null);
  const [prediction, setPrediction] = useState([]);

  


  const resetState = useCallback(() => {
    setModelLoading(false);
    setPredictionLoading(false);
    setModelError('');
    setSuccess('');
  }, []);

  const setAuthHeader = useCallback(() => {
    const token = localStorage.getItem('token');
    if (token) {
      axios.defaults.headers.common['Authorization'] = `Token ${token}`;
    } else {
      delete axios.defaults.headers.common['Authorization'];
    }
  }, []);

  const handleApiCall = useCallback(async (apiCall, successMessage, isPrediction = false) => {
    resetState();
    if (isPrediction) {
      setPredictionLoading(true);
    } else {
      setModelLoading(true);
    }

    try {
      const response = await apiCall();
      if (isPrediction) {
        const newPrediction = response.data;
        setPrediction(prevPredictions => {
          const updatedPredictions = prevPredictions.filter(pred => pred.model_id !== newPrediction.model_id);
          return [...updatedPredictions, newPrediction];
        });
        setModelError('');
        return { data: response.data };
      } else {
        setModel(response.data);
        setSuccess(successMessage);
        setModelError('');
      }
      return response.data;
    } catch (err) {
      setModelError(err.response?.data?.error || 'An error occurred.');
      return null;
    } finally {
      if (isPrediction) {
        setPredictionLoading(false);
      } else {
        setModelLoading(false);
      }
    }
  }, [resetState]);

  const getModels = useCallback(() => 
    handleApiCall(() => axios.get('api/mlmodels/models_list/'), 'Models fetch successful!'),
  [handleApiCall]);

  const getPrediction = useCallback(async (predictionData) => {    
    return handleApiCall(() => axios.post('api/mlmodels/predict/', predictionData), '', true);
  }, [handleApiCall]);
  


  const value = { 
    model,
    modelLoading,
    predictionLoading,
    modelError,
    success,
    prediction,
    getModels,
    getPrediction,
    setModelError,
  };

  return <ModelContext.Provider value={value}>{children}</ModelContext.Provider>;
};

export const useModel = () => {
  const context = useContext(ModelContext);
  if (!context) {
    throw new Error('useModel must be used within a ModelProvider');
  }
  return context;
};
