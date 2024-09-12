import React, { useEffect, useState } from "react";
import { Button, Card, Form, Row, Spinner } from "react-bootstrap";
import { useModel } from "../Contexts/ModelContext";
import SpinnerComponent from "./SpinnerComponent";

const ModelsContainer = ({ latestBiometrics, profileData }) => {
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

  const preparePredictionData = (model, modelInputValues) => {
    const featureNames = JSON.parse(model.feature_names);
    return featureNames.reduce((acc, feature) => {
      let value = modelInputValues[feature] || "";
      if (!value) {
        value =
          feature === "Age"
            ? profileData.age
            : feature === "Gender"
            ? profileData.gender.toLowerCase()
            : feature === "BMI"
            ? profileData.bmi
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
    <Card className="primary-card">
      <h3 className="p-3 text-center card-title">Our AI Models</h3>
      {modelLoading ? (
        <SpinnerComponent />
      ) : models.length === 0 ? (
        <span className="badge m-auto rounded-pill bg-secondary">
          AI models are not available
        </span>
      ) : (
        models.map((model) => {
          const featureNames = JSON.parse(model.feature_names);
          const isPredictClicked = predictClickedForModel === model.id;
          const outputMaps = JSON.parse(model.output_maps);

          return (
            <Card className="p-3 mb-2 d-flex flex-column" key={model.id}>
              <h3 className="ml-50 card-title w-100">{model.name}:</h3>
              {latestBiometrics && profileData && (
                <Row>
                  {featureNames.map((feature, index) => {
                    const modelInputValues = inputValues[model.id] || {};
                    const value =
                      modelInputValues[feature] ||
                      (feature === "Age"
                        ? profileData.age
                        : feature === "Gender"
                        ? profileData.gender
                        : feature === "BMI"
                        ? profileData.bmi
                        : latestBiometrics.find(
                            (b) => b.biochemical.name === feature
                          )?.value || "");
                    const isMissing = isPredictClicked && value === "";

                    return (
                      <Form.Group
                        className="mb-3 col-lg-4 col-md-6 col-sm-12"
                        key={index}
                      >
                        <Form.Label>
                          {feature}
                          {isMissing && (
                            <span className="text-danger ms-1">* missing</span>
                          )}
                        </Form.Label>
                        <Form.Control
                          type="text"
                          value={value}
                          onChange={(e) =>
                            handleChange(feature, e.target.value, model.id)
                          }
                          className="form-input"
                          disabled={feature === "Age" || feature === "Gender"}
                        />
                      </Form.Group>
                    );
                  })}
                </Row>
              )}
              <Card className="d-flex flex-row p-3" style={{ width: "100%" }}>
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
                {Object.entries(outputMaps).map(([name, value], index) => (
                  <Button
                    key={value}
                    type="button"
                    className={`btn ${
                      prediction.some(
                        (pred) =>
                          pred.model_id === model.id && pred.prediction === name
                      )
                        ? ""
                        : "disabled"
                    }

                    ${
                      prediction?.some(
                        (pred) =>
                          pred.model_id === model.id && pred.prediction === name
                      )
                        ? index === 0 ? "btn-success" : "btn-danger"
                        : "btn-secondary"
                    } me-2`}
                    disabled={predictionLoading}
                  >
                    {predictionLoading ? (
                      <div style={{ display: "flex", alignItems: "center" }}>
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
                ))}
              </Card>
            </Card>
          );
        })
      )}
    </Card>
  );
};

export default ModelsContainer;
