import React, { useState, useEffect } from 'react';
import { Container, Card, Form, Button, Alert, Spinner } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';
import Header from '../Components/Header';

const mockUser = {
  first_name: 'John',
  last_name: 'Doe',
  email: 'john.doe@example.com',
  phone_number: '1234567890',
  gender: 'male',
  job: 'Software Developer',
  city: 'San Francisco',
  date_of_birth: '1990-01-01',
  height: '180',
  weight: '75'
};

const formFields = [
  { name: 'firstName', label: 'First Name', type: 'text' },
  { name: 'lastName', label: 'Last Name', type: 'text' },
  { name: 'email', label: 'Email', type: 'email' },
  { name: 'phone', label: 'Phone', type: 'tel' },
  { name: 'gender', label: 'Gender', type: 'select', options: [
    { label: 'Select Gender', value: '' },
    { label: 'Male', value: 'male' },
    { label: 'Female', value: 'female' },
    { label: 'Other', value: 'other' },
  ]},
  { name: 'job', label: 'Job', type: 'text' },
  { name: 'city', label: 'City', type: 'text' },
  { name: 'dateOfBirth', label: 'Date of Birth', type: 'date' },
  { name: 'height', label: 'Height (cm)', type: 'number' },
  { name: 'weight', label: 'Weight (kg)', type: 'number' },
];

const validateForm = (formData) => {
  const validations = {
    firstName: { test: value => !!value.trim(), message: 'First name is required.' },
    lastName: { test: value => !!value.trim(), message: 'Last name is required.' },
    email: { test: value => !!value.trim(), message: 'Email is required.' },
    phone: { test: value => /^\d{10}$/.test(value), message: 'Phone number must be exactly 10 digits.' },
    gender: { test: value => value !== '', message: 'Gender is required.' },
  };

  return Object.keys(validations)
    .filter(field => !validations[field].test(formData[field]))
    .map(field => validations[field].message);
};

const FormField = ({ name, label, type, options, value, onChange }) => (
  <Form.Group key={name} className="mb-3 col-lg-3 col-md-4 col-sm-6">
    <Form.Label>{label}</Form.Label>
    {type === 'select' ? (
      <Form.Control as="select" name={name} value={value} onChange={onChange} className="form-input">
        {options.map(option => <option key={option.value} value={option.value}>{option.label}</option>)}
      </Form.Control>
    ) : (
      <Form.Control type={type} name={name} value={value} onChange={onChange} className="form-input" />
    )}
  </Form.Group>
);

const ProfilePage = () => {
  const token = localStorage.getItem("token");
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    email: '',
    phone: '',
    gender: '',
    job: '',
    city: '',
    dateOfBirth: '',
    height: '',
    weight: ''
  });
  const [status, setStatus] = useState({ errors: [], success: false, loading: false });
  const navigate = useNavigate();

  useEffect(() => {
    if (!token) {
      navigate('/login');
    } else {
      setFormData({
        firstName: mockUser.first_name,
        lastName: mockUser.last_name,
        email: mockUser.email,
        phone: mockUser.phone_number,
        gender: mockUser.gender,
        job: mockUser.job,
        city: mockUser.city,
        dateOfBirth: mockUser.date_of_birth,
        height: mockUser.height,
        weight: mockUser.weight
      });
    }
  }, [token, navigate]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const validationErrors = validateForm(formData);

    if (validationErrors.length > 0) {
      setStatus({ errors: validationErrors, success: false, loading: false });
      return;
    }

    setStatus({ errors: [], success: false, loading: true });

    // Simulate an API call
    setTimeout(() => {
      setStatus({ errors: [], success: true, loading: false });
    }, 1000);
  };

  return (
    <div className="profile-page">
      <Header isLoggedIn={true} />
      <Container>
        <Card className="profile-card">
          <Card.Body>
            <Form onSubmit={handleSubmit}>
              {status.loading && <div className="text-center mb-4"><Spinner animation="border" /></div>}
              {status.errors.length > 0 && (
                <Alert variant="danger">
                  <ul className="mb-0">
                    {status.errors.map((err, index) => <li key={index}>{err}</li>)}
                  </ul>
                </Alert>
              )}
              {status.success && !status.loading && <Alert variant="success">Profile updated successfully!</Alert>}
              <div className="row">
                {formFields.map(field => (
                  <FormField
                    key={field.name}
                    name={field.name}
                    label={field.label}
                    type={field.type}
                    options={field.options}
                    value={formData[field.name]}
                    onChange={handleChange}
                  />
                ))}
              </div>
              <Button className="save-btn" variant="dark" type="submit" disabled={status.loading}>
                {status.loading ? 'Saving...' : 'Save Changes'}
              </Button>
            </Form>
          </Card.Body>
        </Card>
        <Card className="profile-card">
          <Card.Body>
          <h2 className="text-start me-4 mb-4">Biometrics</h2>
          <Form onSubmit={handleSubmit}>
              
              <div className="row">
                {formFields.map(field => (
                  <FormField
                    key={field.name}
                    name={field.name}
                    label={field.label}
                    type={field.type}
                    options={field.options}
                    value={formData[field.name]}
                    onChange={handleChange}
                  />
                ))}
              </div>
              <Button className="save-btn" variant="dark" type="submit" disabled={status.loading}>
                {status.loading ? 'Saving...' : 'Save Changes'}
              </Button>
            </Form>
          </Card.Body>
        </Card>
      </Container>
    </div>
  );
};

export default ProfilePage;
