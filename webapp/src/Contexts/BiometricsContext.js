import React, { createContext, useState, useContext, useCallback } from 'react';
import axios from 'axios';

const BiometricsContext = createContext();

const API_URL = process.env.REACT_APP_API_URL;

export const BiometricsProvider = ({ children }) => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [biometrics, setBiometrics] = useState([]);
  console.log(biometrics);
  
  const resetState = useCallback(() => {
    setLoading(false);
    setError('');
  }, []);

  const handleApiCall = useCallback(async (apiCall) => {
    resetState();
    setLoading(true);

    try {
      const response = await apiCall();
      setBiometrics(response.data);
      return response.data;
    } catch (err) {
      setError(err.response?.data?.error || 'An error occurred.');
      return null;
    } finally {
      setLoading(false);
    }
  }, [resetState]);

  const fetchBiometrics = useCallback(() => 
    handleApiCall(() => axios.get(`${API_URL}api/adminpanel/biochemicals/`)),
  [handleApiCall]);

  const value = {
    biometrics,
    loading,
    error,
    fetchBiometrics,
  };

  return (
    <BiometricsContext.Provider value={value}>
      {children}
    </BiometricsContext.Provider>
  );
};

export const useBiometrics = () => {
  const context = useContext(BiometricsContext);
  if (!context) {
    throw new Error('useBiometrics must be used within a BiometricsProvider');
  }
  return context;
};
