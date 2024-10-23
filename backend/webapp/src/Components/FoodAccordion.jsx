import React from 'react';
import { Accordion } from 'react-bootstrap';
import FoodBars from './FoodBars';

const FoodAccordion = ({ foodScores }) => {
  const groupedScores = foodScores.reduce((acc, food) => {
    const { category, sub_category, name, score } = food;

    if (!acc[category]) {
      acc[category] = {};
    }

    if (!acc[category][sub_category]) {
      acc[category][sub_category] = [];
    }

    acc[category][sub_category].push({ name, score });
    
    return acc;
  }, {});

  
  const length = foodScores ? foodScores.length : 0;

  return (
    <Accordion className="w-100 h-100">
      {Object.keys(groupedScores).map((category, index) => (
        <Accordion.Item eventKey={String(index)} key={index}>
          <Accordion.Header><h6>{category}</h6></Accordion.Header>
          <Accordion.Body>
            {Object.keys(groupedScores[category]).map((subCategory, subIndex) => (
              <div key={subIndex}>
                <h6>{subCategory}</h6>
                <ul>
                  {groupedScores[category][subCategory].map((foodItem, foodIndex) => {
                    const itemIndex = foodScores.findIndex(item => item.name === foodItem.name);
                    return (
                        <FoodBars length={length} food={foodItem.name} index={itemIndex} />
                    );
                  })}
                </ul>
              </div>
            ))}
          </Accordion.Body>
        </Accordion.Item>
      ))}
    </Accordion>
  );
};

export default FoodAccordion;
