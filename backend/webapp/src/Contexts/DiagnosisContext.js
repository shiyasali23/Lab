import React, { createContext, useState, useContext, useCallback } from 'react';
import axios from 'axios';

const DiagnosisContext = createContext();

export const DiagnosisProvider = ({ children }) => {
  const [diagnosisLoading, setDiagnosisLoading] = useState(false);
  const [diagnosisPredictionLoading, setDiagnosisPredictionLoading] = useState(false);
  const [diagnosisError, setDiagnosisError] = useState('');
  const [success, setSuccess] = useState('');
  const [diagnosisModel, setDiagnosisModel] = useState(null);
  const [diagnosisPrediction, setDiagnosisPrediction] = useState([]);

  const resetState = useCallback(() => {
    setDiagnosisLoading(false);
    setDiagnosisPredictionLoading(false);
    setDiagnosisError('');
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
      setDiagnosisPredictionLoading(true);
    } else {
      setDiagnosisLoading(true);
    }

    try {
      const response = await apiCall();
      if (isPrediction) {
        setDiagnosisPrediction(response.data);
        setDiagnosisError('');
        return response.data;
      } else {
        setDiagnosisModel(response.data);
        setSuccess(successMessage);
        setDiagnosisError('');
      }
      return response.data;
    } catch (err) {
      setDiagnosisError(err.response?.data?.error || 'An error occurred.');
      return null;
    } finally {
      if (isPrediction) {
        setDiagnosisPredictionLoading(false);  
      } else {
        setDiagnosisLoading(false);
      }
    }
  }, [resetState]);

  const getDiagnosis = useCallback(() => 
    handleApiCall(() => axios.get('api/mlmodels/diagnosis/'), 'Diagnosis fetch successful!'),
  [handleApiCall]);

  const getDiagnosisPrediction = useCallback(async (predictionData) => {
    return handleApiCall(() => axios.post('api/mlmodels/predict/', predictionData), '', true);
  }, [handleApiCall]);

  const value = { 
    diagnosisModel,  
    diagnosisLoading,  
    diagnosisPredictionLoading,  
    diagnosisError,  
    success,
    diagnosisPrediction,  
    getDiagnosis,  
    getDiagnosisPrediction,  
    setDiagnosisError,  
  };

  return <DiagnosisContext.Provider value={value}>{children}</DiagnosisContext.Provider>;
};

export const useDiagnosis = () => {
  const context = useContext(DiagnosisContext);  
  if (!context) {
    throw new Error('useDiagnosis must be used within a DiagnosisProvider');
  }
  return context;
};
