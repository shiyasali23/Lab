import React, { useState } from "react";
import { Row, Col } from "react-bootstrap";
import BarGraph from "./BarGraph";

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
    <div className="d-flex flex-column h-100">
      <Row style={{ overflow: "auto" }} className="flex-grow-1">
        {/* Left Side (70% width) */}
        <Col md={8} className=" d-flex flex-column">
          <Row className="flex-grow-1">
            {/* Left Top (split into two sections) */}
            <form
  md={6}
  className="border p-0 col d-flex flex-column align-items-center justify-content-center"
>
  {imageSrc ? (
    <div
      style={{ 
        width: "100%", 
        height: "200px", /* Set a fixed height */
        overflow: "hidden",
        position: "relative" /* Ensure that the image is positioned properly */
      }}
      className="card p-0"
    >
      <img
        src={imageSrc}
        style={{ 
          width: "100%", 
          height: "100%", 
          objectFit: "cover",
          position: "absolute", /* Ensure the image covers the div completely */
          top: 0,
          left: 0
        }}
        alt="Uploaded"
      />
    </div>
  ) : (
    <input
      type="file"
      id="imageUpload"
      name="image"
      accept="image/*"
      className="form-control"
      onChange={handleFileChange}
    />
  )}
  {imageSrc && (
    <button type="submit" className="btn btn-dark mt-3">
      Analyse
    </button>
  )}
</form>


            <Col
              md={6}
              className=" d-flex align-items-center justify-content-center"
            >
              Left Top Right
            </Col>
          </Row>
          <Row className="flex-grow-1">
            {/* Left Bottom */}
            <Col className=" d-flex align-items-center justify-content-center">
              Left Bottom
            </Col>
          </Row>
        </Col>

        {/* Right Side (30% width) */}
        <Col
          md={4}
          style={{ maxHeight: "76.5vh" }}
          className=" d-flex flex-column card p-0"
        >
          {foodScores ? (
            <div
              style={{
                height: `${sortedScores.length * 20}px`,
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
        </Col>
      </Row>
    </div>
  );
};

export default FoodRecomendationComponent;
