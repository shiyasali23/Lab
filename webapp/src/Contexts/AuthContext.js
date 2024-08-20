import React, { createContext, useState, useContext, useCallback } from 'react';
import axios from 'axios';

const AuthContext = createContext();

const API_URL = process.env.REACT_APP_API_URL;

export const AuthProvider = ({ children }) => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [user, setUser] = useState(null);

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
      localStorage.setItem('token', response.data.token);
      return response.data;
    } catch (err) {
      setError(err.response?.data?.error || 'An error occurred.');
      return null;
    } finally {
      setLoading(false);
    }
  }, [resetState]);

  const signup = useCallback((userData) => 
    handleApiCall(() => axios.post(`${API_URL}api/services/signup/`, userData), 'Signup successful!'),
  [handleApiCall]);

  const login = useCallback((email, password) => 
    handleApiCall(() => axios.post(`${API_URL}api/services/login/`, { email, password }), 'Login successful!'),
  [handleApiCall]);


  const value = {
    user,
    loading,
    error,
    success,
    signup,
    login,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};
