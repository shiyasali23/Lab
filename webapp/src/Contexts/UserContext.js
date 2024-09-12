import React, { createContext, useState, useContext, useCallback, useEffect } from 'react';
import axios from 'axios';

const UserContext = createContext();


export const UserProvider = ({ children }) => {
  const [userLoading, setUserLoading] = useState(false);
  const [userError, setUserError] = useState('');
  const [success, setSuccess] = useState('');
  const [user, setUser] = useState(null);

  const resetState = useCallback(() => {
    setUserLoading(false);
    setUserError('');
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
    setUserLoading(true);
    setAuthHeader();

    try {
      const response = await apiCall();
      setSuccess(successMessage);
      setUser(response.data);     
      return response.data;
    } catch (err) {
      setUserError(err.response?.data?.error || 'An error occurred.');
      return null;
    } finally {
      setUserLoading(false);
    }
  }, [resetState, setAuthHeader]);

  const getUser = useCallback(() =>
    handleApiCall(() => axios.get(`api/services/user/`), 'User details fetched.'),
  [handleApiCall]);

  const updateUser = useCallback((userData) => 
    handleApiCall(() => axios.patch(`api/services/userupdate/`, userData), 'User updated.'),
  [handleApiCall]);


  const createBiometrics = useCallback((biometricsData) => 
    handleApiCall(() => axios.post(`api/services/biometrics/create/`, biometricsData), 'Biometrics created.'),
  [handleApiCall]);

  const deactivateUser = useCallback(() => 
    handleApiCall(
      async () => {
        await axios.post(`api/services/user/deactivate/`);
        localStorage.removeItem('token');
        setAuthHeader(); 
        setUser(null);
      },
      'User account deactivated'
    ),
  [handleApiCall, setAuthHeader]);



  const logout = useCallback(() => 
    handleApiCall(
      async () => {
        await axios.post(`api/services/logout/`);
        localStorage.removeItem('token');
        setAuthHeader(); 
        setUser(null);
      },
      'Logged out!'
    ),
  [handleApiCall, setAuthHeader]);

  const value = {
    user,
    userLoading,
    userError,
    setUserError,
    getUser,
    updateUser,
    deactivateUser,
    createBiometrics,
    logout,
    setUser
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
