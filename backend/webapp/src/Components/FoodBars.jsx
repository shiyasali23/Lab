import React from "react";

const FoodBars = ({ length, FoodIndex, food }) => {

  const getColur = (FoodIndex, total) => {
    // Map the FoodIndex to a hue value between 120 (green) and 0 (red)
    const hue = 120 - (FoodIndex / total) * 120;
    return `hsl(${hue}, 100%, 50%)`;
  };

  const renderBars = (food, length, FoodIndex) => {
    const sections = Array.from({ length: length }, (_, i) => i + 1);
    const number = length - FoodIndex;
    const barColor = getColur(FoodIndex, length);
    return (
      <div style={{ height: "35px" }} className="d-flex align-items-center justify-content-space-between">
        <h6 className="m-auto" style={{ fontSize: "12px", width: "125px" }}>{food}</h6>
        <div className="d-flex w-100 align-items-center border">
          {sections.map((section, index) => (
            <div
              key={index}
              style={{
                flex: 1,
                height: "20px",
                backgroundColor: index < number ? barColor : "lightgray",
              }}
            ></div>
          ))}
        </div>
      </div>
    );
  };

  return (
    <div className="w-100 h-100">
      {renderBars(food, length, FoodIndex)}
    </div>
  );
};

export default FoodBars;
