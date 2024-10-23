import React, { createContext, useState, useContext, useCallback } from 'react';
import axios from 'axios';

const DetectionContext = createContext();

export const DetectionProvider = ({ children }) => {
  const [detectionsLoading, setDetectionsLoading] = useState(false);
  const [detectionError, setDetectionError] = useState('');
  const [success, setSuccess] = useState('');
  const [detection, setDetection] = useState(null);

  const resetState = useCallback(() => {
    setDetectionsLoading(false);
    setDetectionError('');
    setSuccess('');
  }, []);

  const handleApiCall = useCallback(async (apiCall, successMessage) => {
    resetState();
    setDetectionsLoading(true);

    try {
      const response = await apiCall();      
      setSuccess(successMessage); 
      setDetection(response.data);       
      return response.data;
    } catch (err) {
      setDetectionError(err.response?.data?.detail || 'An error occurred.');
      return null;
    } finally {
      setDetectionsLoading(false);
    }
  }, [resetState]);

  const getDetections = useCallback(async (file) => {
    const formData = new FormData();
    formData.append('file', file);
  
    return handleApiCall(() => axios.post('http://localhost:8002/detect/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    }), 'Detections fetched successfully!');
  }, [handleApiCall]);
  

  const value = {
    detection,
    detectionsLoading,
    detectionError,
    success,
    getDetections,
    setDetectionError,
  };

  return <DetectionContext.Provider value={value}>{children}</DetectionContext.Provider>;
};

export const useDetection = () => {
  const context = useContext(DetectionContext);
  if (!context) {
    throw new Error('useDetection must be used within a DetectionProvider');
  }
  return context;
};