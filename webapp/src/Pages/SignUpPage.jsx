import React, { useState, useEffect } from 'react';
import { Container, Card, Form, Button, Alert, Spinner } from 'react-bootstrap';
import { Link, useNavigate } from 'react-router-dom';
import Header from '../Components/Header';
import { useAuth } from '../Contexts/AuthContext';

const SignUpPage = () => {
  const token = localStorage.getItem("token");
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    email: '',
    phone: '',
    gender: '',
    password: ''
  });
  const [errors, setErrors] = useState([]);
  const { signup, loading, error, success } = useAuth();
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const validateForm = () => {
    const validations = {
      firstName: { test: value => !!value.trim(), message: 'First name is required.' },
      lastName: { test: value => !!value.trim(), message: 'Last name is required.' },
      email: { test: value => !!value.trim(), message: 'Email is required.' },
      phone: { test: value => /^\d{10}$/.test(value), message: 'Phone number must be exactly 10 digits.' },
      gender: { test: value => value !== '', message: 'Gender is required.' },
      password: { test: value => !!value.trim(), message: 'Password is required.' },
    };

    return Object.keys(validations)
      .filter(field => !validations[field].test(formData[field]))
      .map(field => validations[field].message);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const validationErrors = validateForm();

    if (validationErrors.length > 0) {
      setErrors(validationErrors);
      return;
    }

    setErrors([]);
    const { firstName, lastName, email, phone, gender, password } = formData;
    
    const userData = {
      email: email.trim().toLowerCase(),
      password,
      first_name: capitalize(firstName),
      last_name: capitalize(lastName),
      phone_number: phone,
      gender,
    };

    await signup(userData);
  };

  useEffect(() => {
    if (token || success) {
      navigate('/home');
    }
  }, [token, success, navigate]);

  const capitalize = (str) => str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();

  const formFields = [
    { name: 'firstName', placeholder: 'First Name', type: 'text' },
    { name: 'lastName', placeholder: 'Last Name', type: 'text' },
    { name: 'email', placeholder: 'Email', type: 'email' },
    { name: 'phone', placeholder: 'Phone', type: 'tel' },
    { name: 'password', placeholder: 'Password', type: 'password' },
  ];

  const genderOptions = [
    { label: 'Select Gender', value: '' },
    { label: 'Male', value: 'male' },
    { label: 'Female', value: 'female' },
  ];

  return (
    <div className="d-flex flex-column min-vh-100">
      <Header isLoggedIn={false} />
      <Container className="d-flex flex-grow-1 align-items-center justify-content-center">
        <Card className="p-4 form-box" style={{ maxWidth: '400px', width: '100%' }}>
          <Card.Body>
            <h2 className="text-center mb-4">Sign Up</h2>
            <Form onSubmit={handleSubmit}>
              {loading && <div className="d-flex justify-content-center mb-3"><Spinner animation="border" /></div>}
              {(error || errors.length > 0) && (
                <Alert variant="danger">
                  <ul className="mb-0">
                    {error && <li>{error}</li>}
                    {errors.map((err, index) => <li key={index}>{err}</li>)}
                  </ul>
                </Alert>
              )}

              {formFields.map(({ name, placeholder, type }, index) => (
                <Form.Group key={index} controlId={`form${name}`} className="mb-4">
                  <Form.Control
                    type={type}
                    name={name}
                    placeholder={placeholder}
                    required
                    value={formData[name]}
                    onChange={handleChange}
                    className="form-input"
                  />
                </Form.Group>
              ))}

              <Form.Group controlId="formGender" className="mb-4">
                <Form.Control
                  as="select"
                  name="gender"
                  required
                  value={formData.gender}
                  onChange={handleChange}
                  className="form-input"
                >
                  {genderOptions.map((option, index) => (
                    <option key={index} value={option.value}>{option.label}</option>
                  ))}
                </Form.Control>
              </Form.Group>

              <Button className="w-100 form-button" variant="dark" type="submit">
                Sign Up
              </Button>
            </Form>
            <div className="login-footer mt-4 text-center">
              <Link to="/login" className="text-dark text-center text-decoration-none">
                Already have an account? Login
              </Link>
            </div>
          </Card.Body>
        </Card>
      </Container>
    </div>
  );
};

export default SignUpPage;
