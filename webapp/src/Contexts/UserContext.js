import React, { createContext, useState, useContext, useCallback } from 'react';
import axios from 'axios';

const UserContext = createContext();

const API_URL = process.env.REACT_APP_API_URL;

export const UserProvider = ({ children }) => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [user, setUser] = useState(null);
  const token = localStorage.getItem('token');

  axios.defaults.headers.common['Authorization'] = `Token ${token}`;

  const resetState = useCallback(() => {
    setLoading(false);
    setError('');
    setSuccess('');
  }, []);

  const handleApiCall = useCallback(async (apiCall, successMessage) => {
    resetState();
    setLoading(true);

    try {
      const response = await apiCall();
      setSuccess(successMessage);
      setUser(response.data);
      return response.data;
    } catch (err) {
      setError(err.response?.data?.error || 'An error occurred.');
      return null;
    } finally {
      setLoading(false);
    }
  }, [resetState]);

  const getUser = useCallback(() => 
    handleApiCall(() => axios.get(`${API_URL}api/services/user/`), 'User details fetched successfully.'),
  [handleApiCall]);

  const updateUser = useCallback((userData) => 
    handleApiCall(() => axios.patch(`${API_URL}api/services/user/update/`, userData), 'User updated successfully.'),
  [handleApiCall]);

  const deactivateUser = useCallback(() => 
    handleApiCall(
      async () => {
        await axios.post(`${API_URL}api/services/user/deactivate/`);
        localStorage.removeItem('token'); // Remove the token from local storage
        setUser(null); // Set user to null
      },
      'User account deactivated successfully!'
    ),
  [handleApiCall]);

  const createBiometrics = useCallback((biometricsData) => 
    handleApiCall(() => axios.post(`${API_URL}api/services/biometrics/create/`, biometricsData), 'Biometrics created successfully.'),
  [handleApiCall]);

  const logout = useCallback(() => 
    handleApiCall(
      async () => {
        await axios.post(`${API_URL}api/services/logout/`);
        localStorage.removeItem('token');
        setUser(null);
      },
      'Logged out successfully!'
    ),
  [handleApiCall]);
  

  const value = {
    user,
    loading,
    error,
    success,
    getUser,
    updateUser,
    deactivateUser,
    createBiometrics,
    logout,
  };

  return <UserContext.Provider value={value}>{children}</UserContext.Provider>;
};

export const useUser = () => {
  const context = useContext(UserContext);
  if (!context) {
    throw new Error('useUser must be used within a UserProvider');
  }
  return context;
};
