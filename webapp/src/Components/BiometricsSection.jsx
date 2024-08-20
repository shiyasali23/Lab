import React, { useState, useEffect } from 'react';
import { Card, Form, Button, Alert, Spinner } from 'react-bootstrap';
import { useBiometrics } from '../Contexts/BiometricsContext';
import FormField from './FormField'; 

const BiometricsSection = ({ user }) => {
  const { biometrics, loading, error, fetchBiometrics } = useBiometrics();
  const [formValues, setFormValues] = useState({});
  const [status, setStatus] = useState({ loading: false, errors: [], success: false });

  useEffect(() => {
    fetchBiometrics();
  }, [fetchBiometrics]);

  useEffect(() => {
    if (biometrics.length > 0) {
      const initialFormValues = biometrics.reduce((acc, biochemical) => {
        acc[biochemical.name] = '';
        return acc;
      }, {});
      setFormValues(initialFormValues);
    }
  }, [biometrics]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormValues((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus((prev) => ({ ...prev, loading: true, errors: [], success: false }));

    try {
      setStatus((prev) => ({ ...prev, success: true }));
    } catch (err) {
      setStatus((prev) => ({ ...prev, errors: [err.message] }));
    } finally {
      setStatus((prev) => ({ ...prev, loading: false }));
    }
  };

  if (loading) return <div className="text-center mb-4"><Spinner animation="border" /></div>;
  if (error) return <Alert variant="danger">{error}</Alert>;

  return (
    <Card className="profile-card mt-4">
      <Card.Body>
        <h2 className="text-start me-4 mb-4">Biometrics</h2>
        <Form onSubmit={handleSubmit}>
          {status.loading && <div className="text-center mb-4"><Spinner animation="border" /></div>}
          {status.errors.length > 0 && (
            <Alert variant="danger">
              <ul className="mb-0">
                {status.errors.map((err, index) => <li key={index}>{err}</li>)}
              </ul>
            </Alert>
          )}
          {status.success && !status.loading && (
            <Alert variant="success">Biometrics updated successfully!</Alert>
          )}
          <div className="row">
            {biometrics.map((biochemical) => (
              <FormField
                key={biochemical.id}
                name={biochemical.name}
                label={biochemical.name}
                value={formValues[biochemical.name]}
                onChange={handleChange}
              />
            ))}
          </div>
          <Button
            className="save-btn"
            variant="dark"
            type="submit"
            disabled={status.loading}
          >
            {status.loading ? 'Saving...' : 'Save Changes'}
          </Button>
        </Form>
      </Card.Body>
    </Card>
  );
};

export default BiometricsSection;
