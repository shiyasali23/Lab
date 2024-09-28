import React, { useState, useEffect } from "react";
import { Container, Card, Form, Button, Alert } from "react-bootstrap";
import { Link, useNavigate } from "react-router-dom";
import Header from "../Components/Header";
import { useAuth } from "../Contexts/AuthContext";
import SpinnerComponent from "../Components/SpinnerComponent";

const LoginPage = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const { login, loading, error, success } = useAuth();
  const navigate = useNavigate();
  const token = localStorage.getItem("token");
  const handleSubmit = async (e) => {
    e.preventDefault();
    await login(email, password);
  };

  useEffect(() => {
    if (token || success) {
      navigate('/');
    }
  }, [token, success, navigate]);

  return (
    <div className="d-flex flex-column min-vh-100">
      <Header isLoggedIn={false} />
      <Container className="d-flex flex-grow-1 align-items-center justify-content-center">
        <Card
          className="p-4 form-box"
          style={{ maxWidth: "400px", width: "100%" }}
        >
          <Card.Body>
            <h2 className="text-center mb-4">Login</h2>
            <Form onSubmit={handleSubmit}>
              {loading && (
                <div className="d-flex justify-content-center mb-3">
                  <SpinnerComponent/>
                </div>
              )}
              {error && <Alert variant="danger">{error}</Alert>}

              <Form.Group controlId="formEmail" className="mb-4">
                <Form.Control
                  type="email"
                  placeholder="Email"
                  required
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="form-input"
                />
              </Form.Group>

              <Form.Group controlId="formPassword" className="mb-4">
                <Form.Control
                  type="password"
                  placeholder="Password"
                  required
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="form-input"
                />
              </Form.Group>

              <Button
                className="w-100 form-button"
                variant="dark"
                type="submit"
              >
                Login
              </Button>
            </Form>
            <div className="login-footer mt-4 d-flex justify-content-between">
              <Link
                to="/forgot-password"
                className="text-dark text-decoration-none"
              >
                Forgot Password?
              </Link>
              <Link to="/signup" className="text-dark text-decoration-none">
                Create Account
              </Link>
            </div>
          </Card.Body>
        </Card>
      </Container>
    </div>
  );
};

export default LoginPage;
