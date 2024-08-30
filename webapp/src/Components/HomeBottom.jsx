import React from 'react';
import { Card, Row, Col, Accordion } from 'react-bootstrap';
import LineGraph from './LineGraph'; // Import the LineGraph component
import BarGraph from './BarGraph';

const HomeBottom = ({ foodScore, biometrics }) => {
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
          <Col xs={12} md={6} style={{ maxHeight: '1450px', overflowY: 'auto' }}>
            {biometrics ? (
              <div style={{ height: 'auto', overflowY: 'auto' }} className='primary-card'>
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
              </div>
            ) : (
              <span className="badge m-auto rounded-pill bg-secondary">Data not available</span>
            )}
          </Col>
          <Col xs={12} md={6}>
            {foodScore ? (
              <div style={{ height: '1450px', overflowY: 'auto' }} className='primary-card'>
                <h5 className="text-center">Food Recommendation</h5>
                <BarGraph foodScore={foodScore} />
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
