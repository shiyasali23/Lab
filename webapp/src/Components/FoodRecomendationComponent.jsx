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
      reader.readAsDataURL(file); 
    }
  };

  return (
    <div className="d-flex flex-column h-100">
      <Row style={{ overflow: "auto" }} className="flex-grow-1">
        {/* Left Side (70% width) */}
        <Col md={8} className=" d-flex flex-column">
          <Row className="d-flex flex-column justify-content-between h-100 w-100 align-items-center">
            {/* Left Top (split into two sections) */}

            <form
              md={6}
              className="w-50 p-0 h-100 border-none card d-flex align-items-center justify-content-between"
            >
              {imageSrc ? (
                <div
                  style={{
                    width: "100%",
                    height: "220px",
                    margin: "0px",
                  }}
                  className="card"
                >
                  <img
                    src={imageSrc}
                    style={{
                      width: "100%",
                      height: "100%",
                      padding: "0px",
                      margin: "0",
                      objectFit: "fill",
                    }}
                    alt="Uploaded"
                  />
                  <button className="btn w-25 m-auto btn-primary mt-2">
                    Analyze
                  </button>
                </div>
              ) : (
                <input
                  type="file"
                  id="imageUpload"
                  name="image"
                  accept="image/*"
                  className="form-control m-auto w-75"
                  onChange={handleFileChange}
                />
              )}
            </form>

            <Col
              md={6}
              className="w-50 h-100  d-flex align-items-center justify-content-center"
            >
              Left Top Right
            </Col>
          </Row>
          <Row className="w-100 h-100 d-flex align-items-center justify-content-center">
            {/* Left Bottom */}
            Left Bottom
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
