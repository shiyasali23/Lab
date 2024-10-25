import React, { useEffect, useState } from "react";
import { Button, Form, Spinner } from "react-bootstrap";
import { useModel } from "../Contexts/ModelContext";
import SpinnerComponent from "./SpinnerComponent";
import CenteredMessage from "./CenteredMessage";

const ModelsComponent = ({ userData, latestBiometrics }) => {
  const { getModels, modelLoading, predictionLoading, getPrediction } =
    useModel();

  const [models, setModels] = useState(null);
  const [userInputs, setUserInputs] = useState([]); 

  useEffect(() => {
    const fetchModels = async () => {
      const data = await getModels();
      if (data) {
        setModels(data);
        const newUserInputs = data.map((items) => {
          const newitems = {
            model: items.id,
            data: {},
          };

          JSON.parse(items.feature_names).forEach((featureName) => {
            newitems.data[featureName] = findInputValue(featureName);
          });

          return newitems;
        });
        setUserInputs(newUserInputs);
      }
    };

    fetchModels();
  }, [getModels]);

  const findInputValue = (featureName) => {
    const userAttributes = {
      Age: userData.age,
      Gender: userData.gender,
      BMI: userData.bmi,
    };

    if (featureName in userAttributes) {
      return userAttributes[featureName] || "";
    }

    const matchedBiometric = latestBiometrics.find(
      (biometric) => biometric.biochemical.name === featureName
    );

    return matchedBiometric ? matchedBiometric.value : "";
  };

  const handleChange = (e, featureName, modelId) => {
    const newValue = e.target.value;

    setUserInputs((prevInputs) => {
      const updatedInputs = [...prevInputs];
      const modelIndex = updatedInputs.findIndex(
        (item) => item.model === modelId
      );

      if (modelIndex !== -1) {
        updatedInputs[modelIndex].data[featureName] =
          featureName === "Gender" ? newValue : parseFloat(newValue);
      }

      return updatedInputs;
    });
  };


  const renderInputs = (featureName, featureValue, modelId) => {
    return (
      <Form.Group className="" key={featureName}>
        <Form.Label className="form-label-small">{featureName}</Form.Label>
        <Form.Control
          value={featureValue}
          type={featureName === "Gender" ? "text" : "number"}
          className="form-input-small"
          readOnly={featureName === "Age" || featureName === "Gender" ? true : false}
          onChange={(e) => handleChange(e, featureName, modelId)}
          required
        />
      </Form.Group>
    );
  };
  
  const renderPredictions = (modelId) => {
    const model = models.find((model) => model.id === modelId);
    const outputMap = JSON.parse(model.output_maps); 
  
    return (
      <div className="w-100 p-2 gap-2 d-flex justify-content-center align-items-center">
        {Object.keys(outputMap).map((prediction) => (
          <button key={prediction} className="btn btn-primary">
            {prediction}
          </button>
        ))}
      </div>
    );
  };
  

  return (
    <div className="w-100 h-100 d-flex gap-2 flex-column ">
      <div className="w-100 h-100 d-flex gap-2 justify-content-center align-items-center">
        {modelLoading ? (
          <SpinnerComponent />
        ) : userInputs.length === 0 ? (
          <CenteredMessage text={"Models not found"} />
        ) : (
          <>
            {userInputs.map((items, index) => (
              <div
                key={index}
                style={{ width: "50%" }}
                className="h-100 card d-flex flex-column border"
              >
                <h6 className="card-header text-center w-100">
                  {models.find((model) => model.id === items.model).name}:{" "}
                  {models
                    .find((model) => model.id === items.model)
                    .accuracy.toFixed(2)}
                  % accurate
                </h6>
                <form style={styles.featureGrid} className="w-100 h-100 p-2">
                  {Object.entries(items.data).map(
                    ([featureName, featureValue]) =>
                      renderInputs(featureName, featureValue, items.model)
                  )}
                </form>
                <div
                  style={{ height: "15%" }}
                  className="w-100 d-flex flex-column p-2"
                >
                  {predictionLoading ? (
                    <SpinnerComponent />
                  ) : (
                    <div className="w-100 d-flex justify-content-center align-items-center">
                      <button
                        style={{ width: "30%" }}
                        className="btn btn-primary m-auto"
                      >
                        Predict
                      </button>
                      {renderPredictions(items.model)}
                    </div>
                  )}
                </div>
              </div>
            ))}
          </>
        )}
      </div>
      <div style={{ height: "15%" }} className="w-100 border">
        bottom
      </div>
    </div>
  );
};

const styles = {
  featureGrid: {
    display: "grid",
    gap: "10px",
    gridTemplateColumns: "repeat(3, 1fr)",
    alignItems: "center",
  },
};

export default ModelsComponent;
