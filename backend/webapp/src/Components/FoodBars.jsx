import React from "react";

const FoodBars = ({ length, index, food }) => {
 
  const renderBars = (food, number) => {
    const sections = Array.from({ length: length }, (_, i) => i + 1);

    return (
      <div style={{ height: "35px" }} className="d-flex align-items-center justify-content-space-between"> 
        <h6 className="m-auto" style={{ fontSize: "12px", width: "125px" }}>{food}</h6>
        <div className="d-flex w-100 align-items-center border "> 
          {sections.map((section, index) => (
            <div
              key={index}
              style={{
                flex: 1,
                height: "20px",
                backgroundColor: index < number ? "green" : "lightgray",
              }}
            ></div>
          ))}
        </div>
      </div>
    );
  };

  return (
    <div className="w-100 h-100">
      {renderBars(food, length - index)}
    </div>
  );
};

export default FoodBars;
