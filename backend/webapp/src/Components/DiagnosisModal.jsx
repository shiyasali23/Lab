import React from "react";
import PropTypes from "prop-types";
import ProbabilityBars from "./ProbabilityBars";
import CenteredMessage from "./CenteredMessage";

const DiagnosisModal = ({ prediction, onClose }) => {
  const sortedProbabilities = prediction.probability
    ? Object.fromEntries(
        Object.entries(prediction.probability)
          .sort(([, valueA], [, valueB]) => valueB - valueA)
          .slice(0, 5)
      )
    : null;

  console.log(sortedProbabilities);

  return (
    <div className="modal" style={styles.modal}>
      <div style={styles.modalContent} className="modal-content">
        <i
          className="fa-solid fa-xmark"
          onClick={onClose}
          style={styles.closeButton}
        ></i>
        <div className="d-flex w-100 h-100 overflow-auto justify-content-center align-items-center">
          <div className="d-flex w-100 h-100 card overflow-auto gap-2 flex-column p-3 justify-content-center">
          <h4 className="w-100 card-header">{prediction.prediction}</h4>

            <div className="card p-2 d-flex">
              <h5 className="card-title">Medications</h5>
              <ul style={styles.predictionGrid}>
                {prediction.medications.map((medication) => (
                  <span class="badge bg-dark">{medication}</span>
                ))}
              </ul>
            </div>
            <div className="card p-2 d-flex">
              <h5 className="card-title">Precautions</h5>
              <ul style={styles.predictionGrid}>
                {prediction.precautions.map((precautions) => (
                  
                  <li style={styles.diagnosisLi}>{precautions}</li>
                ))}
              </ul>
            </div>
            <div className="card p-2 d-flex">
              <h5 className="card-title">Diets</h5>
              <ul style={styles.predictionGrid}>
                {prediction.diets.map((diets) => (
                  <li style={styles.diagnosisLi}>{diets}</li>
                ))}
              </ul>
            </div>
          </div>
          <div
            style={{ width: "80%", height: "85%" }}
            className="d-flex flex-column p-5 justify-content-center align-items-center"
          >
            {!sortedProbabilities ? (
              <CenteredMessage text={"Probabilities not found"} />
            ) : (
              <ProbabilityBars sortedProbabilities={sortedProbabilities} />
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

DiagnosisModal.propTypes = {
  prediction: PropTypes.object.isRequired,
  onClose: PropTypes.func.isRequired,
};

const styles = {
  modal: {
    display: "flex",
    position: "fixed",
    zIndex: 1,
    left: 0,
    top: 0,
    width: "100%",
    height: "100%",
    backgroundColor: "rgba(0,0,0,0.5)",
    justifyContent: "center",
    alignItems: "center",
  },
  modalContent: {
    width: "98%",
    height: "650px",
    position: "relative",
    backgroundColor: "white",
    Radius: "8px",
    overflow: "hidden",
  },
  closeButton: {
    position: "absolute",
    right: "40px",
    top: "20px",
    fontSize: "28px",
    fontWeight: "bold",
    cursor: "pointer",
  },
  predictionGrid: {
    display: "grid",
    gap: "10px",
    gridTemplateColumns: "repeat(3, 1fr)",
    alignItems: "center",
  },
  diagnosisLi:{
    fontSize: "14px",
    fontWeight: "600",
    color: "black",
  }
};

export default DiagnosisModal;
