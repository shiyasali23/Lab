import React, { useState } from "react";
import Header from "../Components/Header";

const CameraPage = () => {
  const [image, setImage] = useState(null);

  return (
    <div style={{ height: "90vh", width: "100vw" }}>
      <Header />
      <div className="container-fluid h-100 d-flex flex-wrap">
        {/* Left section */}
        <div className="col-12 col-md-6 h-100 d-flex flex-column justify-content-center align-items-center">
          <div className="w-100 h-50 d-flex flex-column justify-content-center align-items-center border border-dark p-2">
            <div className="w-100 h-100 d-flex justify-content-center align-items-center border border-dark">
              <img className="w-100 h-100 border border-dark" src="" alt="" />
            </div>
            <div className="w-100 h-10 d-flex justify-content-center align-items-center p-1">
              <button type="button" className="btn btn-dark">
                {image ? "Analyze" : "Upload Image"}
              </button>
            </div>
          </div>
          <div className="w-100 h-50 d-flex justify-content-center align-items-center border border-dark">
            food nutrition graph
          </div>
        </div>

        {/* Right section */}
        <div className="col-12 col-md-6 h-100 d-flex justify-content-between">
          <div className="w-100 h-100 d-flex flex-column justify-content-center align-items-center border border-dark">
            <div className="w-100 p-1 h-50 d-flex justify-content-center align-items-center border border-dark">
              prediction result graph
            </div>
            <div className="w-100 p-1 h-100 d-flex justify-content-center align-items-center border border-dark">
              food categories accordion
            </div>
          </div>
          <div style={{overflow: 'auto'}} className="w-100 h-100 d-flex justify-content-center align-items-center border border-dark">
            Food score full graph
          </div>
        </div>
      </div>
    </div>
  );
};

export default CameraPage;
