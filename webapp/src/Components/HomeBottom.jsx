import React from 'react';
import { Card, Row, Col, Accordion } from 'react-bootstrap';
import LineGraph from './LineGraph'; // Import the LineGraph component
import BarGraph from './BarGraph';

const HomeBottom = ({ foodScore, biometrics }) => {
  const sortedScores = Array.isArray(foodScore) ? [...foodScore].sort((a, b) => b.score - a.score) : [];

  // Group biometrics by category
  const categorizedBiometrics = biometrics.reduce((acc, metric) => {
    const key = Object.keys(metric)[0];
    const category = metric[key].category;

    if (!acc[category]) {
      acc[category] = [];
    }
    acc[category].push(metric);
    return acc;
  }, {});

  // Group food items by category
  const categorizedFoods = sortedScores.reduce((acc, food) => {
    const { category } = food;
    if (!acc[category]) {
      acc[category] = [];
    }
    acc[category].push(food);
    return acc;
  }, {});

  return (
    <div style={{
      border: 'none',
      marginTop: '1rem',
      width: '100%',
      padding: '0.5rem 0.5rem',
      boxShadow: 'none',
      backgroundColor: 'white'
    }}>
      <Card.Body>
        <Row>
          <Col xs={12} md={6} style={{ height: '1450px', display: 'flex', flexDirection: 'column' }}>
            <div style={{ flex: 1, overflowY: 'auto' }} className='primary-card'>
              {biometrics ? (
                <>
                  <h5 className="text-center mb-3">Biometrics Analytics</h5>
                  <Accordion>
                    {Object.keys(categorizedBiometrics).map((category, index) => (
                      <Accordion.Item eventKey={index.toString()} key={index}>
                        <Accordion.Header><h5>{category}</h5></Accordion.Header>
                        <Accordion.Body>
                          {categorizedBiometrics[category].map((metric, i) => {
                            const key = Object.keys(metric)[0];
                            const lastValue = metric[key].values[metric[key].values.length - 1];
                            const isExpired = new Date(lastValue.expired_date) < new Date();
                            
                            return (
                              <div key={i} style={{ marginBottom: '20px' }}>
                                <h6>
                                  {key}{' '}
                                  {isExpired && (
                                    <span style={{ color: 'red' }}>
                                      *Expired on {new Date(lastValue.expired_date).toLocaleDateString('en-GB')}
                                    </span>
                                  )}
                                </h6>
                                <LineGraph data={metric} />
                              </div>
                            );
                          })}
                        </Accordion.Body>
                      </Accordion.Item>
                    ))}
                  </Accordion>
                </>
              ) : (
                <span className="badge m-auto rounded-pill bg-secondary">Data not available</span>
              )}
            </div>
            <div style={{ flex: 1, overflowY: 'auto', marginTop: '1rem' }} className='primary-card'>
              {categorizedFoods ? (
                <>
                  <h5 className="text-center mb-3">Recommended Food by Category</h5>
                  <Accordion>
                    {Object.keys(categorizedFoods).map((subCategory, index) => (
                      <Accordion.Item eventKey={index.toString()} key={subCategory}>
                        <Accordion.Header><h5>{subCategory}</h5></Accordion.Header>
                        <Accordion.Body>
                          <div className="d-flex flex-wrap justify-content-center">
                            {categorizedFoods[subCategory].map((food) => (
                              <div
                                key={food.id}
                                style={{
                                  width: '100px',
                                  margin: '0.5rem',
                                  textAlign: 'center',
                                  border: '1px solid #ccc',
                                  borderRadius: '8px',
                                  padding: '0.5rem',
                                  boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
                                }}
                              >
                                <img
                                  src={food.image}
                                  alt={food.food_name}
                                  style={{
                                    width: '60px',
                                    height: '60px',
                                    objectFit: 'cover',
                                    borderRadius: '50%',
                                    marginBottom: '0.5rem',
                                  }}
                                />
                                <p style={{ fontSize: '0.9rem', margin: '0' }}>{food.food_name}</p>
                              </div>
                            ))}
                          </div>
                        </Accordion.Body>
                      </Accordion.Item>
                    ))}
                  </Accordion>
                </>
              ) : (
                <span className="badge m-auto rounded-pill bg-secondary">Data not available</span>
              )}
            </div>
          </Col>
          <Col xs={12} md={6} style={{height: '1450px', display: 'flex' }}>
            {foodScore ? (
              <div style={{ flex: 1, overflowY: 'auto' }} className='primary-card'>
                <h5 className="text-center">Food Recommendation</h5>
                <BarGraph sortedScores={sortedScores} />
              </div>
            ) : (
              <span className="badge m-auto rounded-pill bg-secondary">Data not available</span>
            )}
          </Col>
        </Row>
      </Card.Body>
    </div>
  );
};

export default HomeBottom;
