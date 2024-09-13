import React from "react";
import HealthScoreGraph from "./HealthScoreGraph";

const ProfileComponent = ({
  userData,
  latestBiometrics,
  conditions,
  healthScore,
}) => {
  const bmi = userData.bmi || null;
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

  const hyperBiochemicals =
    latestBiometrics?.filter((bio) => bio && bio.scaled_value < -1) || null;

  const hypoBiochemicals =
    latestBiometrics?.filter((bio) => bio && bio.scaled_value > 1) || null;

  const renderBiochemicalList = (biochemicals) => {
    return biochemicals.map((bio) => {
      const isExpired =
        bio.expired_date && new Date(bio.expired_date) <= new Date();
      return (
        <div
          key={bio.biochemical?.name || "unknown"}
          style={{
            marginRight: "5px",
            marginLeft: "10px",
            marginBottom: "5px",
            padding: "5px 10px",
            backgroundColor: "#E74C3C",
            color: "#FFFFFF",
            Radius: "5px",
            display: "inline-block",
            wordBreak: "break-word",
            fontSize: "13px",
            whiteSpace: "normal",
          }}
        >
          {bio.biochemical?.name || "Unknown"} ({bio.value || "N/A"})
          {isExpired && (
            <h6
              style={{
                letterSpacing: "1px",
                textAlign: "center",
                color: "white",
                fontSize: "8px",
                marginTop: "2px",
              }}
            >
              (expired)
            </h6>
          )}
        </div>
      );
    });
  };

  return (
    <div className="w-100 h-100  d-flex align-items-center justify-content-center">
      <div className=" w-100 h-100  d-flex flex-column align-items-center justify-content-center">
        <div className=" w-100 h-100  d-flex flex-column align-items-center justify-content-center">
          <div className=" w-100 h-50  d-flex flex-column justify-content-evenly">
            <h5>Hello {userData?.first_name || "User"}</h5>
            <strong>
              BMI:{" "}
              {bmi ? (
                <>
                  {userData.bmi}
                  <span style={{ color: bmiCategory.color }}>
                    ({bmiCategory.category})
                  </span>
                </>
              ) : (
                "Update weight and height"
              )}
            </strong>
          </div>
          <div className=" w-100 h-100  d-flex flex-column align-items-center justify-content-center">
            <div style={{ overflow: "auto" }} className="w-100 h-100  d-flex">
              <strong>Low</strong>
              <div style={{ overflow: "auto" }}>
                {hypoBiochemicals.length > 0
                  ? renderBiochemicalList(hypoBiochemicals)
                  : "No low biochemicals"}
              </div>
            </div>

            <div style={{ overflow: "auto" }} className=" w-100 h-100  d-flex">
              <strong>High</strong>
              <div style={{ overflow: "auto" }}>
                {hyperBiochemicals.length > 0
                  ? renderBiochemicalList(hyperBiochemicals)
                  : "No high biochemicals"}
              </div>
            </div>
          </div>
        </div>
        <div
          style={{ overflow: "auto" }}
          className=" w-100 card p-1 h-50  d-flex align-items-center justify-content-center"
        >
          {conditions.length > 0 ? (
            <div style={{ overflow: "auto" }}>
              {conditions.map((condition, index) => (
                <span
                  key={index}
                  className="badge bg-dark"
                  style={{ padding: "10px", fontSize: "12px", margin: "5px" }}
                >
                  {condition}
                </span>
              ))}
            </div>
          ) : (
            <div style={styles.centeredMessage}>
              <span className="badge rounded-pill bg-secondary">
                User Data not available
              </span>
            </div>
          )}
        </div>
      </div>
      <div className=" w-100 p-3 h-100 d-flex flex-column align-items-center justify-content-center">
        {healthScore ? (
          <HealthScoreGraph healthScore={healthScore} />
        ) : (
          <div style={styles.centeredMessage}>
            <span className="badge rounded-pill bg-secondary">
              User Data not available
            </span>
          </div>
        )}
      </div>
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
};
export default ProfileComponent;
