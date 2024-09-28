import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { AuthProvider } from './Contexts/AuthContext';
import { UserProvider } from './Contexts/UserContext';
import { ModelProvider } from './Contexts/ModelContext';
import { NutrientProvider } from './Contexts/NutrientContext';
import { DetectionProvider } from './Contexts/DetectionContext';
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <AuthProvider>
    <UserProvider>
      <ModelProvider>
      <NutrientProvider>
      <DetectionProvider>
    <App />
   </DetectionProvider>
    </NutrientProvider>
    </ModelProvider>
    </UserProvider>
    </AuthProvider>
  </React.StrictMode>
);


reportWebVitals();
