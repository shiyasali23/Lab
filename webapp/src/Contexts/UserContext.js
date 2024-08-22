import React, { createContext, useState, useContext, useCallback, useEffect } from 'react';
import axios from 'axios';

const UserContext = createContext();

const API_URL = process.env.REACT_APP_API_URL;

export const UserProvider = ({ children }) => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [user, setUser] = useState(null);

  const resetState = useCallback(() => {
    setLoading(false);
    setError('');
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

  useEffect(() => {
    setAuthHeader(); 
  }, [setAuthHeader]);

  const handleApiCall = useCallback(async (apiCall, successMessage) => {
    resetState();
    setLoading(true);
    setAuthHeader();

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
  }, [resetState, setAuthHeader]);

  const getUser = useCallback(() =>
    handleApiCall(() => axios.get(`${API_URL}api/services/user/`), 'User details fetched.'),
  [handleApiCall]);

  const updateUser = useCallback((userData) => 
    handleApiCall(() => axios.patch(`${API_URL}api/services/user/update/`, userData), 'User updated.'),
  [handleApiCall]);

  const deactivateUser = useCallback(() => 
    handleApiCall(
      async () => {
        await axios.post(`${API_URL}api/services/user/deactivate/`);
        localStorage.removeItem('token');
        setAuthHeader(); 
        setUser(null);
      },
      'User account deactivated'
    ),
  [handleApiCall, setAuthHeader]);

  const createBiometrics = useCallback((biometricsData) => 
    handleApiCall(() => axios.post(`${API_URL}api/services/biometrics/create/`, biometricsData), 'Biometrics created.'),
  [handleApiCall]);

  const logout = useCallback(() => 
    handleApiCall(
      async () => {
        await axios.post(`${API_URL}api/services/logout/`);
        localStorage.removeItem('token');
        setAuthHeader(); 
        setUser(null);
      },
      'Logged out!'
    ),
  [handleApiCall, setAuthHeader]);

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
