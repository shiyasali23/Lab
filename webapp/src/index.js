import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { AuthProvider } from './Contexts/AuthContext';
import { BiometricsProvider } from './Contexts/BiometricsContext';
import { UserProvider } from './Contexts/UserContext';
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <AuthProvider>
    <BiometricsProvider>
    <UserProvider>
    <App />
    </UserProvider>
    </BiometricsProvider>
    </AuthProvider>
  </React.StrictMode>
);


reportWebVitals();
