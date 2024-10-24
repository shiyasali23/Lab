import React, { useMemo, useState } from "react";
import { useNutrient } from "../Contexts/NutrientContext";
import SpinnerComponent from "./SpinnerComponent";
import { useDetection } from "../Contexts/DetectionContext";
import NutrientsGraph from "./NutrientsGraph";
import FoodBars from "./FoodBars";
import FoodAccordion from "./FoodAccordion";

const FoodRecomendationComponent = ({ foodScores }) => {
  const { nutrient, nutrientLoading } = useNutrient();
  const { getDetections, detectionsLoading } = useDetection();
  const [imageSrc, setImageSrc] = useState(null);
  const [searchTerm, setSearchTerm] = useState("");
  const [suggestions, setSuggestions] = useState([]);
  const [nutrientData, setNutrientData] = useState(null);
  const suggestionArray = nutrient ? nutrient.map((item) => item.name) : [];
  const [detectedFoods, setDetectedFoods] = useState(null);

  const sortedFoodScores = foodScores?.sort((a, b) => b.score - a.score);
  const length = sortedFoodScores ? sortedFoodScores.length : 0;


  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      const imageUrl = URL.createObjectURL(file);
      setImageSrc(imageUrl);
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setDetectedFoods(null); 
    const file = document.getElementById("imageUpload").files[0];
  
    try {
      const response = await getDetections(file);
      
      if (response && response.data) {
        const detectedFoodsData = [];
        const { data } = response;         
        if (data && data.length > 0) {
          data.forEach((item) => {
            const matchedFoodIndex = sortedFoodScores.findIndex(
              foodItem => foodItem.name.toLowerCase() === item.toLowerCase()
            );

            if (matchedFoodIndex !== -1) { 
              const matchedFood = sortedFoodScores[matchedFoodIndex];
              detectedFoodsData.push({
                name: matchedFood.name,
                index: matchedFoodIndex 
              });
            }
          });
  
          const sortedDetectedFoods = detectedFoodsData.sort(
            (a, b) => b.score - a.score
          );
          setDetectedFoods(sortedDetectedFoods);
          if (sortedDetectedFoods.length > 0) {
            const highestScoreFood = sortedDetectedFoods[0].name;
            setSearchTerm(highestScoreFood);
            handleSearchSubmit(highestScoreFood);
          } 
        }
      }
    } catch (error) {
      console.error("Error detecting foods:", error);
    }
  };
  

  const handleSearchSubmit = (term) => {
    const searchValue = term || searchTerm;

    if (typeof searchValue !== "string") {
      setNutrientData(null);
      return;
    }

    if (nutrient && searchValue) {
      const result = nutrient.filter(
        (item) => item.name.toLowerCase() === searchValue.toLowerCase()
      );
      setNutrientData(result.length > 0 ? result : null);
    } else {
      setNutrientData(null);
    }
  };

  const handleSearch = (e) => {
    const query = e.target.value;
    setSearchTerm(query);

    if (query) {
      const filteredSuggestions = suggestionArray.filter((item) =>
        item.toLowerCase().includes(query.toLowerCase())
      );

      setSuggestions(
        filteredSuggestions.length ? filteredSuggestions : ["No items found"]
      );

      const queryExists = filteredSuggestions
        .map((item) => item.toLowerCase())
        .includes(query.toLowerCase());

      if (!queryExists) {
        console.log("Query not found in suggestions");
      }
    } else {
      setSuggestions([]);
    }
  };

  const handleSelect = (item) => {
    if (item !== "No items found") {
      setSearchTerm(item);
      handleSearchSubmit(item);
    }
    setSuggestions([]);
  };

  return (
    <div className="w-100 h-100 border d-flex justify-content-center align-items-center">
      <div className="w-100 h-100 border d-flex flex-column align-items-center justify-content-center overflow-auto">
        <div className="w-100 h-100 d-flex">
          <div className="w-100 h-100 border d-flex flex-column">
            {detectionsLoading ? (
              <SpinnerComponent />
            ) : (
              <div className="w-100 h-100 d-flex flex-column justify-content-center align-items-center">
                <div
                  className="d-flex flex-column justify-content-center align-items-center"
                  style={{
                    width: "200px",
                    height: "200px",
                    margin: "auto",
                  }}
                >
                  {imageSrc ? (
                    <img
                      src={imageSrc}
                      alt="Uploaded"
                      style={{
                        width: "100%",
                        height: "100%",
                        objectFit: "fill",
                      }}
                    />
                  ) : (
                    <h6 className="m-auto text-center">Uploaded Image</h6>
                  )}
                </div>
                <form
                  style={{ height: "20%" }}
                  onSubmit={handleSubmit}
                  className="w-100 d-flex justify-content-center"
                >
                  <input
                    type="file"
                    id="imageUpload"
                    name="image"
                    accept="image/*"
                    onChange={handleFileChange}
                    className="border form-control w-50 m-auto"
                  />
                  {imageSrc && (
                    <button type="submit" className="btn btn-primary m-auto">
                      Analyze
                    </button>
                  )}
                </form>
              </div>
            )}
          </div>
          <div className="w-100 border d-flex overflow-auto">
            {detectionsLoading ? (
              <SpinnerComponent />
            ) : detectedFoods && detectedFoods.length > 0 ? (
              <div className="w-100 p-5 d-flex flex-column overflow-auto ">
                {detectedFoods.map((food, index) => (
                  <FoodBars key={index} length={length} food={food.name} FoodIndex={food.index} />
                ))}
              </div>
            ) : (
              <h6 className="m-auto text-center">Nothing to detect</h6>
            )}
          </div>
        </div>
        <div className="w-100 h-100 p-0 d-flex flex-column justify-content-space-between align-items-center">
          {nutrientLoading ? (
            <SpinnerComponent />
          ) : (
            <>
              <div
                style={{
                  width: "100%",
                  height: "12%",
                  position: "relative",
                }}
                className="w-100 d-flex justify-content-center align-items-center"
              >
                <form
                  className="d-flex h-100 mt-2"
                  onSubmit={(e) => {
                    e.preventDefault();
                    handleSearchSubmit();
                  }}
                  style={{ position: "absolute" }}
                >
                  <input
                    className="form-control p-0 text-center"
                    type="search"
                    placeholder="Search"
                    value={searchTerm}
                    onChange={handleSearch}
                  />
                </form>
                {suggestions.length > 0 && (
                  <ul
                    className="border list-group position-absolute"
                    style={{
                      top: "100%",
                      left: "25%",
                      width: "50%",
                      zIndex: 1,
                    }}
                  >
                    {suggestions.map((suggestion, index) => (
                      <li
                        key={index}
                        className="border list-group-item"
                        onClick={() => handleSelect(suggestion)}
                        style={{
                          cursor:
                            suggestion !== "No items found"
                              ? "pointer"
                              : "default",
                        }}
                      >
                        {suggestion}
                      </li>
                    ))}
                  </ul>
                )}
              </div>
              {nutrientData && <NutrientsGraph data={nutrientData} />}
            </>
          )}
        </div>
      </div>
      <div
        style={{ width: "40%" }}
        className="h-100 p-1 border d-flex align-items-center justify-content-center overflow-auto"
      >
        {foodScores ? (
          <FoodAccordion foodScores={sortedFoodScores} />
        ) : (
          <div className="border d-flex align-items-center justify-content-center flex-grow-1">
            <span className="border badge rounded-pill bg-secondary">
              User Data not available
            </span>
          </div>
        )}
      </div>
    </div>
  );
};

export default FoodRecomendationComponent;
