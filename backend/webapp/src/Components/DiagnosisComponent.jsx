import React, { useEffect, useState } from "react";
import { useDiagnosis } from "../Contexts/DiagnosisContext";
import SpinnerComponent from "./SpinnerComponent";

const DiagnosisComponent = () => {
  const {
    getDiagnosis,
    diagnosisLoading,
    diagnosisPredictionLoading,
    getDiagnosisPrediction,
    diagnosisPrediction,
  } = useDiagnosis();

  const [diagnosisModel, setDiagnosisModel] = useState(null);

  useEffect(() => {
    const fetchModels = async () => {
      const fetchedModel = await getDiagnosis();
      if (fetchedModel) setDiagnosisModel(fetchedModel);
    };
    fetchModels();
  }, [getDiagnosis]);

  const featureNames = diagnosisModel
    ? JSON.parse(diagnosisModel.feature_names)
    : [];

  return (
    <div className="w-100 h-100">
      {diagnosisLoading ? (
        <SpinnerComponent />
      ) : !diagnosisModel ? (
        <div style={styles.centeredMessage}>
          <span className="badge rounded-pill bg-secondary">
            Conditions not available
          </span>
        </div>
      ) : (
        <div className="overflow-auto p-3 m-auto h-100 border">
          <div style={styles.featureGrid}>
            {featureNames.map((feature, index) => (
              <div key={index} className="form-check">
                <input
                  className="form-check-input"
                  type="checkbox"
                  id={`feature-${index}`}
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
