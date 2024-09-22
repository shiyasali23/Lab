import React, { useState, useMemo } from "react";
import { Row, Col } from "react-bootstrap";
import BarGraph from "./BarGraph";
import { useNutrient } from "../Contexts/NutrientContext";
import SpinnerComponent from "./SpinnerComponent";
import NutrientsGraph from "./NutrientsGraph";
import { useDetection } from "../Contexts/DetectionContext";

const FoodRecomendationComponent = ({ foodScores }) => {
  const { nutrient, nutrientLoading } = useNutrient();
  const { getDetections, detectionLoading } = useDetection();
  const [detectedFoods, setDetectedFoods] = useState(null);
  
  

  // Memoize the sorted scores so sorting only occurs when foodScores changes
  const sortedScores = useMemo(() => {
    return Array.isArray(foodScores)
      ? [...foodScores].sort((a, b) => b.score - a.score)
      : [];
  }, [foodScores]);

  const [imageSrc, setImageSrc] = useState(null);
  const [filteredNutrient, setFilteredNutrient] = useState(null);

  const handleFileChange = async (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setImageSrc(reader.result);
      };
      reader.readAsDataURL(file);
  
      const { data } = await getDetections(file); // Get detection data
      console.log(data);
  
      if (data && Array.isArray(data.items)) {
        // Check if data.items is an array
        const detectedFoodsData = data.items
          .map((item) => {
            // Find the food in foodScores that matches the detected item name
            const foodScore = sortedScores.find(
              (food) => food.food_name.toLowerCase() === item.name.toLowerCase()
            );
            return foodScore ? { ...foodScore } : null; // Copy the full foodScore object
          })
          .filter(Boolean); // Filter out null values
  
        setDetectedFoods(detectedFoodsData);
  
        // Step 1: Ensure nutrient data is available before proceeding
        if (nutrient && nutrient.length > 0 && data.items.length > 0) {
          const firstDetectedFood = data.items[0].name.toLowerCase();
  
          // Step 2: Find the nutrient data for the detected food in the `nutrient` array
          const matchedNutrient = nutrient.find(
            (item) => item.name.toLowerCase() === firstDetectedFood
          );
  
          // Step 3: Set the `filteredNutrient` state to the matched nutrient's array if found
          if (matchedNutrient) {
            setFilteredNutrient(matchedNutrient.nutrients); // Set the array of nutrients
          } else {
            setFilteredNutrient(null); // If no match found, set it to null
          }
        }
      }
    }
  };
  
  

  const suggestionArray = nutrient ? nutrient.map((item) => item.name) : null;
  const [searchTerm, setSearchTerm] = useState("");
  const [suggestions, setSuggestions] = useState([]);
  const [isButtonDisabled, setIsButtonDisabled] = useState(true);

  const handleSearch = (e) => {
    const query = e.target.value;
    setSearchTerm(query);

    // Filter suggestions based on user input
    if (query) {
      const filteredSuggestions = suggestionArray.filter((item) =>
        item.toLowerCase().includes(query.toLowerCase())
      );
      setSuggestions(
        filteredSuggestions.length ? filteredSuggestions : ["No items found"]
      );

      // Enable button only if the search term exactly matches an item in the list
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

  // New function to handle searching nutrients when the button is clicked
  const handleSearchSubmit = () => {
    if (nutrient && searchTerm) {
      // Filter nutrient data based on the search term
      const result = nutrient.filter((item) =>
        item.name.toLowerCase().includes(searchTerm.toLowerCase())
      );
      setFilteredNutrient(result.length > 0 ? result : null);
    }
  };
console.log(nutrient);


  return (
    <div className="d-flex flex-column h-100">
      <Row style={{ overflow: "auto" }} className="flex-grow-1">
        {/* Left Side (70% width) */}
        <Col md={8} className="d-flex flex-column">
          <Row className="d-flex flex-column justify-content-between h-100 w-100 align-items-center">
            {/* Left Top (split into two sections) */}
            <form
              md={6}
              style={{ border: "0px" }}
              className="w-50 p-0 h-100 card d-flex align-items-center justify-content-between"
            >
              {detectionLoading ? (
                <SpinnerComponent />
              ) : imageSrc ? (
                <div
                  style={{
                    width: "100%",
                    height: "220px",
                    margin: "0px",
                  }}
                  className="card p-1"
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
              className=" w-50 h-100 d-flex align-items-center justify-content-center"
            >
              {detectionLoading ? (
                <SpinnerComponent />
              ) : detectedFoods ? (
                <div className="h-100 p-0 overflow-auto w-100">
                  <BarGraph sortedScores={detectedFoods} />
                </div>
              ) : (
                <div>Upload image</div>
              )}
            </Col>
          </Row>
          <Row className="w-100 h-100 d-flex align-items-center justify-content-center">
            {nutrientLoading ? (
              <SpinnerComponent />
            ) : nutrient ? (
              <div className="overflow-auto w-100 h-100 p-0 d-flex flex-column justify-content-center align-items-center">
                <div
                  style={{
                    width: "100%",
                    height: "12%",
                    position: "relative",
                    left: "200px",
                  }}
                  className=" w-100 d-flex justify-content-center align-items-center"
                >
                  <form
                    // style={{height:'85%'}}
                    className="d-flex p-0 h-100"
                    onSubmit={(e) => e.preventDefault()}
                  >
                    <input
                      className="form-control w-75 me-sm-2"
                      type="search"
                      placeholder="Search"
                      value={searchTerm}
                      onChange={handleSearch}
                    />
                    <button
                      className="btn btn-dark btn-sm my-2 my-sm-0"
                      type="submit"
                      onClick={handleSearchSubmit} // Call search submit function
                      disabled={isButtonDisabled}
                    >
                      Search
                    </button>
                  </form>

                  {/* Suggestions Dropdown */}
                  {suggestions.length > 0 && (
                    <ul
                      className="list-group position-absolute"
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
                          className="list-group-item"
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

                <div className=" w-100 h-100 d-flex justify-content-center align-items-center">
                  {filteredNutrient ? (
                    <NutrientsGraph nutrientData={filteredNutrient} />
                  ) : (
                    <></>
                  )}
                </div>
              </div>
            ) : (
              <div className="d-flex align-items-center justify-content-center flex-grow-1">
                <span className="badge rounded-pill bg-secondary">
                  User Data not available
                </span>
              </div>
            )}
          </Row>
        </Col>

        {/* Right Side (30% width) */}
        <Col
          md={4}
          style={{ maxHeight: "76.5vh" }}
          className="d-flex flex-column card p-0"
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
