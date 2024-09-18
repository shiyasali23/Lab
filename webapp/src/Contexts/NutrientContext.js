import React, { createContext, useState, useContext, useCallback } from 'react';
import axios from 'axios';

const NutrientContext = createContext();

export const NutrientProvider = ({ children }) => {
  const [nutrientLoading, setNutrientLoading] = useState(false);
  const [nutrientError, setNutrientError] = useState('');
  const [success, setSuccess] = useState('');
  const [nutrient, setNutrient] = useState(null);
console.log(nutrient);

  const resetState = useCallback(() => {
    setNutrientLoading(false);
    setNutrientError('');
    setSuccess('');
  }, []);

  const handleApiCall = useCallback(async (apiCall, successMessage) => {
    resetState();
    setNutrientLoading(true);

    try {
      const response = await apiCall();
      console.log('hic');
      
      setSuccess(successMessage); 
      setNutrient(response.data); 
      return response.data;
    } catch (err) {
      setNutrientError(err.response?.data?.error || 'An error occurred.');
      return null;
    } finally {
      setNutrientLoading(false);
    }
  }, [resetState]);

  const getNutrients = useCallback(() => 
    handleApiCall(() => axios.get('api/adminpanel/foods/'), 'Nutrients fetched successfully!'),
  [handleApiCall]);


  const value = {
    nutrient,
    nutrientLoading,
    nutrientError,
    success,
    getNutrients,
  };

  return <NutrientContext.Provider value={value}>{children}</NutrientContext.Provider>;
};

export const useNutrient = () => {
  const context = useContext(NutrientContext);
  if (!context) {
    throw new Error('useNutrient must be used within a NutrientProvider');
  }
  return context;
};
