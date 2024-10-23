import React from 'react';
import PropTypes from 'prop-types';

const PredictionModal = ({ prediction, onClose }) => {
  return (
    <div className="modal" style={styles.modal}>
      <div className="modal-content">
        <span className="close" onClick={onClose} style={styles.closeButton}>
          &times;
        </span>
        <h2>Prediction Result</h2>
        <h2>{prediction}</h2>
      </div>
    </div>
  );
};

PredictionModal.propTypes = {
  prediction: PropTypes.object.isRequired,
  onClose: PropTypes.func.isRequired,
};

const styles = {
  modal: {
    display: 'flex',
    position: 'fixed',
    zIndex: 1,
    left: 0,
    top: 0,
    width: '100%',
    height: '100%',
    overflow: 'auto',
    backgroundColor: 'rgba(0,0,0,0.5)', 
    justifyContent: 'center',
    alignItems: 'center',
  },
  closeButton: {
    float: 'right',
    fontSize: '28px',
    fontWeight: 'bold',
    cursor: 'pointer',
  },
};

export default PredictionModal;
