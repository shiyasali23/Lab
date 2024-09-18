import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const ToggleSwitch = () => {
  const [isFoodSelected, setIsFoodSelected] = useState(true);

  const handleToggle = () => {
    setIsFoodSelected(!isFoodSelected);
  };

  return (
    <div style={{ width: "170px" ,height: "100%", position: "relative", left: "130px", margin:'auto' }} className="d-flex border align-items-center">
      <span className="me-2">Food</span>
      <div className="form-check form-switch">
        <input
          className="form-check-input"
          type="checkbox"
          id="foodCategoryToggle"
          checked={!isFoodSelected}
          onChange={handleToggle}
        />
        <label className="form-check-label" htmlFor="foodCategoryToggle">
          Category
        </label>
      </div>
    </div>
  );
};

export default ToggleSwitch;
