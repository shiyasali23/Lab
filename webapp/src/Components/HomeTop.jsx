import React from "react";
import { Row, Col, Card } from "react-bootstrap";
import HealthScoreGraph from "./HealthScoreGraph";

const HomeTop = ({ profileData, latestBiometrics, healthScore }) => {
  const processLatestBiometrics = (biometrics) => {
    if (!Array.isArray(biometrics)) {
      return { hypoBiochemicals: [], hyperBiochemicals: [] };
    }
    const now = new Date();
    const validBiometrics = biometrics.filter(
      (bio) => bio && bio.expired_date && new Date(bio.expired_date) > now
    );
    const hypoBiochemicals = validBiometrics.filter(
      (bio) => bio.scaled_value < -1
    );
    const hyperBiochemicals = validBiometrics.filter(
      (bio) => bio.scaled_value > 1
    );
    return { hypoBiochemicals, hyperBiochemicals };
  };

  const { hypoBiochemicals, hyperBiochemicals } =
    processLatestBiometrics(latestBiometrics);

  const renderBiochemicalList = (biochemicals) => {
    return biochemicals.map((bio) => (
      <span
        key={bio.biochemical?.name || "unknown"}
        style={{ color: "red", marginRight: "5px" }}
      >
        {bio.biochemical?.name || "Unknown"} ({bio.value || "N/A"})
      </span>
    ));
  };

  return (
    <Row
      className="d-flex justify-content-between align-items-stretch"
      style={{ marginTop: "20px", height: "350px", width: "100%" }}
    >
      <Col xs={12} md={6} className="mb-3 mb-md-0">
        <Card className="primary-card" style={{ height: "350px" }}>
          <Card.Body>
            {profileData ? (
              <>
                <h2>Hello {profileData.first_name || "User"}.</h2>
                <h6>
                  {hypoBiochemicals.length > 0 && (
                    <>Low: {renderBiochemicalList(hypoBiochemicals)}</>
                  )}
                </h6>
                <h6>
                  {hyperBiochemicals.length > 0 && (
                    <>
                      High: {renderBiochemicalList(hyperBiochemicals)}
                    </>
                  )}
                </h6>
                <h6>
                  {hypoBiochemicals.length === 0 &&
                    hyperBiochemicals.length === 0 &&
                    "All your biometrics are within normal range."}
                </h6>
              </>
            ) : (
              <h2>Loading profile data...</h2>
            )}
          </Card.Body>
        </Card>
      </Col>
      <Col xs={12} md={6}>
        <Card className="primary-card" style={{ height: "350px" }}>
          <Card.Body
            style={{
              height: "350px",
              overflow: "auto",
              backgroundColor: "#e9ecef",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
            }}
          >
            {Array.isArray(healthScore) && healthScore.length > 0 ? (
              <HealthScoreGraph healthScore={healthScore} />
            ) : (
              <h2>Health score not available</h2>
            )}
          </Card.Body>
        </Card>
      </Col>
    </Row>
  );
};

export default HomeTop;
