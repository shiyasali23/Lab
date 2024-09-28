import React, { createContext, useState, useContext, useCallback } from 'react';
import axios from 'axios';

const AuthContext = createContext();


export const AuthProvider = ({ children }) => {
  const [authLoading, setAuthLoading] = useState(false);
  const [authError, setAuthError] = useState('');
  const [success, setSuccess] = useState('');
  const [user, setUser] = useState(null);

  const resetState = useCallback(() => {
    setAuthLoading(false);
    setAuthError('');
    setSuccess('');
  }, []);

  const handleApiCall = useCallback(async (apiCall, successMessage) => {
    resetState();
    setAuthLoading(true);

    try {
      const response = await apiCall();
      setSuccess(successMessage);
      setUser(response.data);
      localStorage.setItem('token', response.data.token);
      return response.data;
    } catch (err) {
      setAuthError(err.response?.data?.error || 'An error occurred.');
      return null;
    } finally {
      setAuthLoading(false);
    }
  }, [resetState]);

  const signup = useCallback((userData) => 
    handleApiCall(() => axios.post(`api/services/signup/`, userData), 'Signup successful!'),
  [handleApiCall]);

  const login = useCallback((email, password) => 
    handleApiCall(() => axios.post(`api/services/login/`, { email, password }), 'Login successful!'),
  [handleApiCall]);
  
  const logout = useCallback((email, password) => 
    handleApiCall(() => axios.post(`api/services/logout/`, { email, password }), 'Logout successful!'),
  [handleApiCall]);


  const value = {
    user,
    authLoading,
    authError,
    setAuthError,
    success,
    signup,
    login,
    logout
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
