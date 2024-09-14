import React, { useState } from "react";
import { Row, Col } from "react-bootstrap";
import BarGraph from "./BarGraph";
import image from "../assets/food.jpg";

const FoodRecomendationComponent = ({ foodScores }) => {
  const sortedScores = Array.isArray(foodScores)
    ? [...foodScores].sort((a, b) => b.score - a.score)
    : [];

  const [imageSrc, setImageSrc] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setImageSrc(reader.result);
      };
      reader.readAsDataURL(file); // Read file as data URL
    }
  };

  return (
    <div className="w-100 h-100 border  d-flex align-items-center justify-content-center">
      <div
        style={{
          width: "70%",
          height: "100%",
          overflow: "auto",
        }}
        className="h-100 border  d-flex flex-column align-items-center justify-content-center"
      >
        <div className="w-100 h-100 border  d-flex align-items-center justify-content-center">
          <form className="w-100 h-100 border  d-flex flex-column align-items-center justify-content-center">
            <div
              style={{
                width: "100%",
                height: "100%",
                padding: "1px",
                margin: "0px",
              }}
              className="card"
            >
              <img
              src={image}
                style={{
                  width: "380px",
                  height: "220px",
                  padding: "0px",
                  margin: "auto",
                  objectFit: "fill",
                }}
                alt="Uploaded"
                className="border"
              />
            </div>
            <button className="btn btn-primary">Analyse</button>
          </form>
          <div className="w-100 h-100 border  d-flex align-items-center justify-content-center">
            left-top-right
          </div>
        </div>
        <div className="w-100 h-100 border  d-flex align-items-center justify-content-center">
          left-bottom
        </div>
      </div>

      <div
        style={{
          width: "30%",
          maxHeight: "76.5vh", 
          overflow: "auto",
        }}
        className="h-100 border  d-flex align-items-center justify-content-center"
      >
        {foodScores ? (
            <div
              style={{
                width: "100%",
                overflow: "auto",
              }}
            >
              <BarGraph sortedScores={sortedScores} />
            </div>
          ) : (
            <div className="d-flex align-items-center justify-content-center flex-grow-1">
              <span className="badge rounded-pill bg-secondary">
                User Data not available
              </span>
            </div>
          )}
      </div>
    </div>
  );
};

export default FoodRecomendationComponent;
