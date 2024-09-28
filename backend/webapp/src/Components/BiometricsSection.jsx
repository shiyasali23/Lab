import React, { useState, useEffect } from 'react';
import { Card, Form, Button, Alert, Spinner, Accordion } from 'react-bootstrap';
import { useUser } from '../Contexts/UserContext';

const BiometricsSection = ({ biometrics }) => {
  const { userLoading, createBiometrics } = useUser();
  const [biometricsData, setBiometricsData] = useState({});
  const [localError, setLocalError] = useState('');

  useEffect(() => {
    const initialData = {};
    biometrics.forEach(item => {
      initialData[item.biochemical.id] = item.value !== null ? item.value.toString() : '';
    });
    setBiometricsData(initialData);
  }, [biometrics]);

  const handleChange = (id, value) => {
    setBiometricsData(prev => ({ ...prev, [id]: value }));
  };

  const handleSubmit = async (category, items) => {
    setLocalError('');

    // Prepare data for submission
    const updatedBiometrics = items
      .map(item => {
        const newValue = biometricsData[item.biochemical.id];
        const oldValue = item.value !== null ? item.value.toString() : '';
        
        // Check if there is any change
        if (newValue !== oldValue) {
          return {
            biochemical_id: item.biochemical.id,
            value: newValue === '' ? null : parseFloat(newValue),
          };
        }
        return null;
      })
      .filter(item => item !== null); // Remove null values

    if (updatedBiometrics.length === 0) {
      setLocalError('No changes detected.');
      return;
    }

    try {
      await createBiometrics(updatedBiometrics)
    } catch (err) {
      console.error('Biometrics update error:', err);
    }
  };

  const isExpired = (date) => {
    return date && new Date(date) < new Date();
  };

  const isCategoryExpired = (category) => {
    return category.some(item => isExpired(item.expired_date));
  };

  const groupedBiometrics = biometrics.reduce((acc, item) => {
    if (!acc[item.biochemical.category]) {
      acc[item.biochemical.category] = [];
    }
    acc[item.biochemical.category].push(item);
    return acc;
  }, {});

  if (userLoading) {
    return <Spinner animation="border" className="d-block mx-auto mt-5" />;
  }

  return (
    <Card className="primary-card mt-4">
      <Card.Body>
        <h2 className="text-start mb-4">Biometrics</h2>
        {localError && <Alert variant="danger" className="mb-4">{localError}</Alert>}
        <Accordion>
          {Object.entries(groupedBiometrics).map(([category, items], index) => (
            <Accordion.Item eventKey={index.toString()} key={category}>
              <Accordion.Header>
                {category}
                {isCategoryExpired(items) && <span className="text-danger ms-2">*Expired</span>}
              </Accordion.Header>
              <Accordion.Body>
                <Form onSubmit={(e) => {
                  e.preventDefault();
                  handleSubmit(category, items);
                }}>
                  <div className="row">
                    {items.map((item) => (
                      <Form.Group className="mb-3 col-lg-4 col-md-6 col-sm-12" key={item.biochemical.id}>
                        <Form.Label className={isExpired(item.expired_date) ? 'text-danger' : ''}>
                          {item.biochemical.name}
                          {isExpired(item.expired_date) && <span className="text-danger ms-1">* expired</span>}
                        </Form.Label>
                        <Form.Control
                          type="number"
                          step="0.01"
                          value={biometricsData[item.biochemical.id] || ''}
                          onChange={(e) => handleChange(item.biochemical.id, e.target.value)}
                          className="form-input"
                        />
                      </Form.Group>
                    ))}
                  </div>
                  <Button className="save-btn mt-3" variant="dark" type="submit" disabled={userLoading}>
                    {userLoading ? "Saving..." : `Save Changes`}
                  </Button>
                </Form>
              </Accordion.Body>
            </Accordion.Item>
          ))}
        </Accordion>
      </Card.Body>
    </Card>
  );
};

export default BiometricsSection;
