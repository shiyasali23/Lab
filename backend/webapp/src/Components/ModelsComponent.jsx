import React, { useEffect, useState } from "react";
import { Button, Form, Row, Spinner } from "react-bootstrap";
import { useModel } from "../Contexts/ModelContext";
import SpinnerComponent from "./SpinnerComponent";

const ModelsComponent = ({ userData, latestBiometrics }) => {
  const {
    getModels,
    modelLoading,
    predictionLoading,
    getPrediction,
    prediction,
  } = useModel();
  const [models, setModels] = useState([]);
  const [predictClickedForModel, setPredictClickedForModel] = useState(null);
  const [inputValues, setInputValues] = useState({});

  useEffect(() => {
    const fetchModels = async () => {
      const fetchedModels = await getModels();
      if (fetchedModels) setModels(fetchedModels);
    };
    fetchModels();
  }, [getModels]);

  const handleChange = (feature, value, modelId) => {
    setInputValues((prev) => ({
      ...prev,
      [modelId]: {
        ...(prev[modelId] || {}),
        [feature]: value,
      },
    }));
  };
console.log(models);

  const preparePredictionData = (model, modelInputValues) => {
    const featureNames = JSON.parse(model.feature_names);
    return featureNames.reduce((acc, feature) => {
      let value = modelInputValues[feature] || "";
      if (!value) {
        value =
          feature === "Age"
            ? userData.age
            : feature === "Gender"
            ? userData.gender.toLowerCase()
            : feature === "BMI"
            ? userData.bmi
            : latestBiometrics.find((b) => b.biochemical.name === feature)
                ?.value || "";
      }
      acc[feature] =
        feature !== "Age" && feature !== "Gender" ? parseFloat(value) : value;
      return acc;
    }, {});
  };

  const handleClickPredict = async (modelId) => {
    const model = models.find((m) => m.id === modelId);
    const modelInputValues = inputValues[modelId] || {};
    const predictionData = preparePredictionData(model, modelInputValues);

    if (
      Object.keys(predictionData).every((feature) => predictionData[feature])
    ) {
      setPredictClickedForModel(modelId);
      try {
        getPrediction({
          ...predictionData,
          model_id: modelId,
        });
      } catch (error) {
        console.error("Error fetching prediction:", error);
      }
    } else {
      setPredictClickedForModel(modelId);
    }
  };

  return (
    <div className="w-100 h-100">
      <div className="d-flex gap-2" style={{ overflow: "auto" }}>
        {modelLoading ? (
          <SpinnerComponent />
        ) : models.length === 0 ? (
          <span className="badge m-auto rounded-pill bg-secondary">
            AI models are not available
          </span>
        ) : (
          models
            .map((model) => {
              const featureNames = JSON.parse(model.feature_names);
              const isPredictClicked = predictClickedForModel === model.id;
              const outputMaps = JSON.parse(model.output_maps);

              return (
                <div
                  className="p-3 border overflow-auto d-flex flex-column"
                  key={model.id}
                >
                  <h6 className="ml-50 mb-2 w-100">
                    {model.name}: {model.accuracy.toFixed(3)}% accurate
                  </h6>
                  {latestBiometrics && userData && (
                    <Row>
                      {featureNames.map((feature, index) => {
                        const modelInputValues = inputValues[model.id] || {};
                        const value =
                          modelInputValues[feature] ||
                          (feature === "Age"
                            ? userData.age
                            : feature === "Gender"
                            ? userData.gender
                            : feature === "BMI"
                            ? userData.bmi
                            : latestBiometrics.find(
                                (b) => b.biochemical.name === feature
                              )?.value || "");

                        const displayValue = value ?? ""; 
                        const isMissing =
                          isPredictClicked && displayValue === "";
                        const isHighestImpact =
                          feature === model.highest_feature_impact;

                        return (
                          <Form.Group
                            className="mb-3 col-lg-4 col-sm-12 col-sm-3"
                            key={index}
                          >
                            <Form.Label
                              className="form-label-small"
                              style={{
                                color: isHighestImpact ? "red" : "inherit",
                              }}
                            >
                              {feature}
                              {isMissing && (
                                <span className="text-danger ms-1">
                                  * missing
                                </span>
                              )}
                            </Form.Label>
                            <Form.Control
                              type="text"
                              value={displayValue}
                              onChange={(e) =>
                                handleChange(feature, e.target.value, model.id)
                              }
                              className="form-input-small"
                            />
                          </Form.Group>
                        );
                      })}
                    </Row>
                  )}
                  <div className="d-flex p-3" style={{ width: "100%" }}>
                    <Button
                      type="button"
                      style={{
                        width: "100px",
                        borderRadius: 0,
                        margin: "0 20px",
                      }}
                      className="btn btn-dark"
                      onClick={() => handleClickPredict(model.id)}
                      disabled={predictionLoading}
                    >
                      {predictionLoading ? (
                        <div style={{ display: "flex", alignItems: "center" }}>
                          <Spinner
                            animation="border"
                            size="sm"
                            style={{ marginRight: "8px" }}
                          />
                          <p style={{ margin: 0 }}>Predicting</p>
                        </div>
                      ) : (
                        "Predict"
                      )}
                    </Button>
                    {Object.entries(outputMaps).map(([name, value], index) => {
                      const isPredictionActive = prediction.some(
                        (pred) =>
                          pred.model_id === model.id && pred.prediction === name
                      );

                      return (
                        <Button
                          key={value}
                          type="button"
                          className={`btn btn-sm ${
                            isPredictionActive
                              ? index === 0
                                ? "btn-success"
                                : "btn-danger"
                              : "btn-secondary"
                          } ${isPredictionActive ? "" : "disabled"} me-2`}
                          disabled={predictionLoading}
                        >
                          {predictionLoading ? (
                            <div
                              style={{ display: "flex", alignItems: "center" }}
                            >
                              <Spinner
                                animation="border"
                                size="sm"
                                style={{ marginRight: "8px" }}
                              />
                              {name}
                            </div>
                          ) : (
                            name
                          )}
                        </Button>
                      );
                    })}
                  </div>
                </div>
              );
            })
        )}
      </div>
      <div className="w-100 h-20 d-flex border align-items-center justify-content-evenly">
        <h6 className="m-3 text-center">Upcoming models:-</h6>
        {[
          "Alzheimers Detection",
          "Kidney Condition",
          "Parkinsons Detection",
          "Cancer Detection",
        ].map((model, index) => (
          <strong
            key={index}
            className="p-2 m-3 border text-center"
            style={{ fontSize: "16px" }}
          >
            {model}
          </strong>
        ))}
      </div>
    </div>
  );
};

export default ModelsComponent;
