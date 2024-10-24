import React, { useEffect, useState } from "react";
import { useDiagnosis } from "../Contexts/DiagnosisContext";
import SpinnerComponent from "./SpinnerComponent";
import PredictionModal from "./PredictionModal"; 

const DiagnosisComponent = ({ userData }) => {
  const {
    getDiagnosis,
    diagnosisLoading,
    diagnosisPredictionLoading,
    getDiagnosisPrediction,
  } = useDiagnosis();

  const [diagnosisModel, setDiagnosisModel] = useState(null);
  const [checkedFeatures, setCheckedFeatures] = useState([]);
  const [isModalOpen, setModalOpen] = useState(false); 
  const [predictionData, setPredictionData] = useState(null); 

  useEffect(() => {
    const fetchModels = async () => {
      const fetchedModel = await getDiagnosis();
      if (fetchedModel) setDiagnosisModel(fetchedModel);
    };
    fetchModels();
  }, [getDiagnosis]);

  const featureNames = diagnosisModel ? diagnosisModel.feature_names : {};

  const handleCheckboxChange = (feature) => {
    setCheckedFeatures((prev) => {
      const updatedFeatures = [...prev];
      if (updatedFeatures.includes(feature)) {
        return updatedFeatures.filter((f) => f !== feature);
      } else {
        return [...updatedFeatures, feature];
      }
    });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (checkedFeatures.length > 0) {
      const inputData = {};
      Object.keys(featureNames).forEach((category) => {
        featureNames[category].forEach((feature) => {
          if (feature === "Gender") {
            inputData[feature] = userData.gender ? userData.gender : null;
          } else {
            inputData[feature] = checkedFeatures.includes(feature) ? 1 : 0;
          }
        });
      });

      const formData = {
        model: diagnosisModel.id,
        data: inputData,
      };
      console.log(formData);
      
      // setPredictionData("hi"); 
      // setModalOpen(true); 

      // const prediction = await getDiagnosisPrediction(formData);

      // if (prediction) {
      //   setPredictionData(prediction); 
      //   setModalOpen(true); 
      // }
    }

    setCheckedFeatures([]);
  };

  const handleCloseModal = () => {
    setModalOpen(false); 
    setPredictionData(null); 
  };

  return (
    <div className="w-100 h-100">
      {diagnosisLoading ? (
        <SpinnerComponent />
      ) : !diagnosisModel ? (
        <div style={styles.centeredMessage}>
          <span className="badge rounded-pill bg-secondary">
            Diagnosis model not available
          </span>
        </div>
      ) : (
        <form onSubmit={handleSubmit} className="overflow-auto p-1 m-auto h-100 border position-relative">
          <div style={{ paddingBottom: "18px" }}>
            {Object.keys(featureNames).map((category, index) => (
              <div key={index} className="mb-1 card w-100 p-3">
                <h6 className="card-title mb-3">{category}</h6>
                <div style={styles.featureGrid}>
                  {featureNames[category].map((feature, index) => (
                    <div key={index} className="form-check">
                      <input
                        className="form-check-input"
                        type="checkbox"
                        id={`feature-${index}`}
                        checked={checkedFeatures.includes(feature)}
                        onChange={() => handleCheckboxChange(feature)}
                      />
                      <label
                        className="form-check-label"
                        htmlFor={`feature-${index}`}
                      >
                        {feature}
                      </label>
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
          <button
            type="submit"
            className="btn btn-primary position-sticky"
            disabled={diagnosisPredictionLoading}
            style={{
              bottom: "8px",
              left: "50%",
              transform: "translateX(-50%)",
              zIndex: 1000,
              borderRadius: "0px",
              display: Object.keys(checkedFeatures).length > 0 ? "block" : "none",
            }}
          >
            {diagnosisPredictionLoading ? <SpinnerComponent /> : "Diagnose"}
          </button>
          {isModalOpen && (
            <PredictionModal
              prediction={predictionData}
              onClose={handleCloseModal}
            />
          )}
        </form>
      )}
    </div>
  );
};

const styles = {
  centeredMessage: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    height: "100%",
    width: "100%",
  },
  featureGrid: {
    display: "grid",
    gridTemplateColumns: "repeat(4, 1fr)",
    gap: "10px",
  },
};

export default DiagnosisComponent;
