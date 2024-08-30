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
    <Card style={{border: 'none',
        marginTop: '1rem',
        width: '100%',
        padding: '0.5rem 0.5rem',}}>
      <Card.Body>
        <Row>
          <Col xs={12} md={6}>
           
            {biometrics ? (
              <div style={{ height: '600px', overflowY: 'auto' }}  className='primary-card'>
                 <h5 className="text-center mb-3">Biometrics Analytics</h5>
                <Accordion>
                  {Object.keys(categorizedBiometrics).map((category, index) => (
                    <Accordion.Item eventKey={index.toString()} key={index}>
                      <Accordion.Header>{category}</Accordion.Header>
                      <Accordion.Body>
                        {categorizedBiometrics[category].map((metric, i) => {
                          const key = Object.keys(metric)[0];
                          return (
                            <div key={i} style={{ marginBottom: '20px' }}>
                              <h6>{key}</h6>
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
              <div style={{ height: '1500px', overflowY: 'auto' }} className='primary-card'>
                <h5 className="text-center">Food Recommendation</h5>
                <BarGraph foodScore={foodScore} />
              </div>
            ) : (
              <span className="badge m-auto rounded-pill bg-secondary">Data not available</span>
            )}
          </Col>
        </Row>
      </Card.Body>
    </Card>
  );
};

export default HomeBottom;
