import React from "react";
import { useAuth } from "../Contexts/AuthContext";
import { useModel } from "../Contexts/ModelContext";
import { useUser } from "../Contexts/UserContext";
import { useDetection } from "../Contexts/DetectionContext";

const AlertComponent = () => {
  const { authError, setAuthError } = useAuth();
  const { modelError, setModelError } = useModel();
  const { userError, setUserError } = useUser();
  const { detectionError, setDetectionError } = useDetection();

  // Handler to reset all errors
  const handleClose = () => {
    setAuthError('');
    setModelError('');
    setUserError('');
    setDetectionError('');
  };

  // Determine which error to display
  const displayError = authError || modelError || userError || detectionError;

  return (
    displayError ? (
      <div className="alert alert-dismissible alert-danger" style={{ width: '40%', height: '50px',margin: 'auto', position: 'fixed', top: '20px', left: '50%', transform: 'translateX(-50%)', zIndex: 9999 }}>
        <button
          type="button"
          className="btn-close"
          onClick={handleClose}
        ></button>
        <strong className="text-center d-block">{displayError}</strong>
      </div>
    ) : null
  );
};

export default AlertComponent;