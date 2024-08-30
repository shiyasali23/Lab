import React from "react";
import { Row, Col, Card } from "react-bootstrap";
import HealthScoreGraph from "./HealthScoreGraph";

const HomeTop = ({
  profileData,
  latesBiometrics,
  healthScore,
  conditions,
}) => {
  // Function to process the latest biometrics
  const processLatestBiometrics = (biometrics) => {
    if (!Array.isArray(biometrics)) {
      return { hypoBiochemicals: [], hyperBiochemicals: [] };
    }
    const now = new Date();
    const hypoBiochemicals = biometrics.filter(
      (bio) => bio && bio.scaled_value < -1
    );
    const hyperBiochemicals = biometrics.filter(
      (bio) => bio && bio.scaled_value > 1
    );
    return { hypoBiochemicals, hyperBiochemicals };
  };

  // Process the latest biometrics
  const { hypoBiochemicals, hyperBiochemicals } = processLatestBiometrics(latesBiometrics);
  
  const renderBiochemicalList = (biochemicals) => {
    return biochemicals.map((bio) => {
      const isExpired = bio.expired_date && new Date(bio.expired_date) <= new Date();
      return (
        <div
          key={bio.biochemical?.name || "unknown"}
          style={{
            marginRight: "5px",
            marginBottom: "5px", 
            padding: "5px 10px", 
            backgroundColor: "#E74C3C",
            color: "#FFFFFF",
            borderRadius: "5px",
            display: "inline-block",
            wordBreak: "break-word", 
            fontSize: "13px",
            whiteSpace: "normal",
          }}
        >
          {bio.biochemical?.name || "Unknown"} ({bio.value || "N/A"})
          {isExpired && (
            <h6 style={{ letterSpacing: "1px",textAlign: "center",color:'white',fontSize: "8px", marginTop: "2px" }}>
              (expired)
            </h6>
          )}
        </div>
      );
    });
  };

  const weight = profileData?.weight_kg;
  const height = profileData?.height_cm / 100; 
  const bmi = weight && height ? weight / height ** 2 : null;

  const getBmiCategory = (bmi) => {
    if (bmi < 18.5) return { category: "Underweight", color: "orange" };
    if (bmi >= 18.5 && bmi < 25) return { category: "Healthy", color: "green" };
    if (bmi >= 25 && bmi < 30)
      return { category: "Overweight", color: "yellow" };
    return { category: "Obesity", color: "red" };
  };

  const bmiCategory = bmi
    ? getBmiCategory(bmi)
    : { category: "N/A", color: "black" };

  return (
    <Card
      className="d-flex justify-content-between align-items-stretch primary-card"
      style={{ minHeight: "250px" }}
    >
      <Card.Body>
        <Row>
          <Col xs={12} md={6} className="mb-3 mb-md-0">
            {profileData ? (
              <>
                <h3>Hello {profileData.first_name || "User"}.</h3>
                {bmi && (
                  <h6>
                    BMI: {bmi.toFixed(2)}{" "}
                    <span style={{ color: bmiCategory.color }}>
                      ({bmiCategory.category})
                    </span>
                  </h6>
                )}
                <div className="p-2 m-3">
                  {hypoBiochemicals.length > 0 && (
                    <h6 className="card-title">
                      Low {renderBiochemicalList(hypoBiochemicals)}
                    </h6>
                  )}
                  {hyperBiochemicals.length > 0 && (
                    <h6 className="card-title">
                      High {renderBiochemicalList(hyperBiochemicals)}
                    </h6>
                  )}
                </div>
                {hypoBiochemicals.length === 0 &&
                  hyperBiochemicals.length === 0 && (
                    <div>All your biometrics are within normal range.</div>
                  )}
                {conditions && conditions.length > 0 && (
                  <Card className="mt-3">
                    <Card.Body>
                      <h5 className="mb-2">You may have</h5>
                      <div
                        className="card-text"
                        style={{
                          display: "flex",
                          flexWrap: "wrap",
                          gap: "7px",
                        }}
                      >
                        {conditions.map((condition, index) => (
                          <span
                            key={index}
                            className="badge bg-dark"
                            style={{ padding: "10px", fontSize: "12px" }}
                          >
                            {condition}
                          </span>
                        ))}
                      </div>
                    </Card.Body>
                  </Card>
                )}
              </>
            ) : (
              <span className="badge m-auto rounded-pill bg-secondary">
                Please Refresh Page
              </span>
            )}
          </Col>

          <Col xs={12} md={6}>
            <div
              style={{
                overflow: "auto",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                padding: "0px",
                height: "400px",
              }}
            >
              {Array.isArray(healthScore) && healthScore.length > 0 ? (
                <HealthScoreGraph healthScore={healthScore} />
              ) : (
                <span className="badge m-auto rounded-pill bg-secondary">
                  Health score not available
                </span>
              )}
            </div>
          </Col>
        </Row>
      </Card.Body>
    </Card>
  );
};

export default HomeTop;