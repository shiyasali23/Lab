import React, { useMemo, useState } from "react";
import { useNutrient } from "../Contexts/NutrientContext";
import SpinnerComponent from "./SpinnerComponent";
import { useDetection } from "../Contexts/DetectionContext";
import NutrientsGraph from "./NutrientsGraph";
import BarGraph from "./BarGraph";

const FoodRecomendationComponent = ({ foodScores }) => {
  const { nutrient, nutrientLoading } = useNutrient();
  const { getDetections, detectionLoading } = useDetection();
  const [imageSrc, setImageSrc] = useState(null);
  const [searchTerm, setSearchTerm] = useState("");
  const [isButtonDisabled, setIsButtonDisabled] = useState(true);
  const [suggestions, setSuggestions] = useState([]);
  const [nutrientData, setnutrientData] = useState(null);
  const suggestionArray = nutrient ? nutrient.map((item) => item.name) : null;
  const [detectedFoods, setDetectedFoods] = useState(null);

  const sortedScores = useMemo(() => {
    return Array.isArray(foodScores)
      ? [...foodScores].sort((a, b) => b.score - a.score)
      : [];
  }, [foodScores]);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      const imageUrl = URL.createObjectURL(file);
      setImageSrc(imageUrl);
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const file = document.getElementById("imageUpload").files[0];
    const { data } = await getDetections(file);

    if (data && Array.isArray(data.items)) {
        const detectedFoodsData = data.items
            .map((item) => {
                const foodScore = foodScores.find(
                    (food) => food.food_name.toLowerCase() === item.name.toLowerCase()
                );
                return foodScore ? { ...foodScore } : null;
            })
            .filter(Boolean);

        const sortedDetectedFoods = detectedFoodsData.sort((a, b) => b.score - a.score);
        setSearchTerm(sortedDetectedFoods[0].food_name);
        setDetectedFoods(sortedDetectedFoods);
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

    setIsButtonDisabled(!filteredSuggestions.includes(query.toLowerCase()));
  } else {
    setSuggestions([]);
    setIsButtonDisabled(true);
  }
};

const handleSelect = (item) => {
  if (item !== "No items found") {
    setSearchTerm(item);
    setIsButtonDisabled(false);
  }
  setSuggestions([]);
};

const handleSearchSubmit = () => {
  if (nutrient && searchTerm) {
    const result = nutrient.filter((item) =>
      item.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setnutrientData(result.length > 0 ? result : null);
  } else {
    setnutrientData(null);
  }
};
  

  return (
    <div className="w-100 h-100 border d-flex justify-content-center align-items-center">
      <div className="w-100 h-100 border d-flex flex-column align-items-center justify-content-center overflow-auto">
        <div className="w-100 h-100 border d-flex">
          <div className="w-100 h-100 border d-flex flex-column">
            {detectionLoading ? (
              <SpinnerComponent />
            ) : (
              <div className="w-100 h-100 border d-flex flex-column justify-content-center align-items-center">
                {/* Image Display */}
                <div
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
                  className="w-100 border d-flex justify-content-center"
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
          <div className="w-100 h-100 border d-flex overflow-auto">
            {detectionLoading ? (
              <SpinnerComponent />
            ) : detectedFoods && detectedFoods.length > 0 ? (
              <BarGraph scoreData={detectedFoods} passedHeight={"30px"} />
            ) : (
              <h6 className="m-auto text-center">Nothing to detect</h6>
            )}
          </div>
        </div>
        <div className="w-100 h-100 p-0 border d-flex flex-column justify-content-space-between align-items-center">
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
                className="border w-100 d-flex justify-content-center align-items-center"
              >
                <form
                  className="border d-flex p-0 h-100"
                  onSubmit={(e) => e.preventDefault()}
                  style={{ position: "absolute", right: "5%" }}
                >
                  <input
                    className="border form-control p-0 me-sm-2"
                    type="search"
                    placeholder="Search"
                    value={searchTerm}
                    onChange={handleSearch}
                  />
                  <button
                    className="border btn btn-dark btn-sm my-2 my-sm-0"
                    type="submit"
                    onClick={handleSearchSubmit}
                    disabled={isButtonDisabled}
                  >
                    Search
                  </button>
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
        className="h-100 border d-flex align-items-center justify-content-center overflow-auto"
      >
        {foodScores ? (
          <BarGraph scoreData={sortedScores}/>
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
