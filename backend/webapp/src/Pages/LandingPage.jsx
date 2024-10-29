// src/LandingPage.js
import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import SpinnerComponent from "../Components/SpinnerComponent";
import { useAuth } from "../Contexts/AuthContext";

function LandingPage() {
  const { login, signup, authLoading } = useAuth();
  const navigate = useNavigate();

  const [isSignup, setSignup] = useState(false);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    email: '',
    phone_number: '',
    gender: '',
    password: ''
  });

  const token = localStorage.getItem("token");

  useEffect(() => {
    if (token) {
      navigate("/main");
    }
  }, [token, navigate]);

  const handleSignup = async (e) => {
    e.preventDefault();
    const result = await signup(formData);
    if (result && result.status) {
      navigate('/main');
    }
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    const result = await login(email, password);
    if (result && result.status) {
      navigate('/main');
    }
  };

  return (
    <div className="landing-page vh-100 w-100 d-flex align-items-center justify-content-center">
      <div className="welcome-section h-100 w-100 d-flex align-items-center justify-content-center">
        <div className="welcome-content p-5">
          <h1 className="display-4">Welcome to Biolabs</h1>
          <p className="lead mt-4">State-of-the-art personalized real-time healthcare, backed by
            cutting-edge diagnostics with advanced technology, leverages remote
            patient monitoring to deliver unparalleled patient outcomes.</p>
        </div>
      </div>
      <div className="form-section w-100 h-100 p-3 d-flex align-items-center justify-content-center">
        <form className="auth-form shadow-lg bg-light p-5" onSubmit={isSignup ? handleSignup : handleLogin}>
          <h2 className="text-center mb-5">{isSignup ? "Join Us" : "Login"}</h2>

          {isSignup && (
            <>
              <div className="row mb-3">
                <div className="col-md-6 mb-3 mb-md-0">
                  <label htmlFor="firstName" className="form-label">First Name</label>
                  <input
                    type="text"
                    className="form-control form-control-sm"
                    id="firstName"
                    placeholder="First Name"
                    required
                    onChange={(e) =>
                      setFormData(prev => ({ ...prev, first_name: e.target.value }))
                    }
                  />
                </div>
                <div className="col-md-6">
                  <label htmlFor="lastName" className="form-label">Last Name</label>
                  <input
                    type="text"
                    className="form-control form-control-sm"
                    id="lastName"
                    placeholder="Last Name"
                    required
                    onChange={(e) =>
                      setFormData(prev => ({ ...prev, last_name: e.target.value }))
                    }
                  />
                </div>
              </div>

              <div className="form-group mb-3">
                <label htmlFor="signupEmail" className="form-label">Email</label>
                <input
                  type="email"
                  className="form-control form-control-sm"
                  id="signupEmail"
                  placeholder="Email"
                  required
                  onChange={(e) =>
                    setFormData(prev => ({ ...prev, email: e.target.value }))
                  }
                />
              </div>

              <div className="form-group mb-3">
                <label htmlFor="phone" className="form-label">Phone</label>
                <input
                  type="tel"
                  className="form-control form-control-sm"
                  id="phone"
                  placeholder="Phone Number"
                  required
                  onChange={(e) =>
                    setFormData(prev => ({ ...prev, phone_number: e.target.value }))
                  }
                />
              </div>

              <div className="form-group mb-3">
                <label htmlFor="gender" className="form-label">Gender</label>
                <select
                  className="form-select form-select-sm"
                  id="gender"
                  required
                  onChange={(e) =>
                    setFormData(prev => ({ ...prev, gender: e.target.value }))
                  }
                >
                  <option value="">Select Gender</option>
                  <option value="male">Male</option>
                  <option value="female">Female</option>
                </select>
              </div>

              <div className="form-group mb-4">
                <label htmlFor="signupPassword" className="form-label">Password</label>
                <input
                  type="password"
                  className="form-control form-control-sm"
                  id="signupPassword"
                  placeholder="Password"
                  required
                  onChange={(e) =>
                    setFormData(prev => ({ ...prev, password: e.target.value }))
                  }
                />
              </div>
            </>
          )}

          {!isSignup && (
            <>
              <div className="form-group mb-3">
                <label htmlFor="loginEmail" className="form-label">Email</label>
                <input
                  type="email"
                  className="form-control form-control-sm"
                  id="loginEmail"
                  placeholder="Email"
                  required
                  onChange={(e) => setEmail(e.target.value)}
                />
              </div>

              <div className="form-group mb-4">
                <label htmlFor="loginPassword" className="form-label">Password</label>
                <input
                  type="password"
                  className="form-control form-control-sm"
                  id="loginPassword"
                  placeholder="Password"
                  required
                  onChange={(e) => setPassword(e.target.value)}
                />
              </div>
            </>
          )}

          <button type="submit" className="btn btn-primary w-100">
            {authLoading ? <SpinnerComponent /> : isSignup ? "Sign Up" : "Login"}
          </button>

          <div className="text-center mt-3 d-flex w-100 justify-content-evenly">
            <h6>{isSignup ? "Already have an account?" : "Don't have an account?"}</h6>
            <a
              onClick={(e) => {
                e.preventDefault();
                setSignup(!isSignup);
              }}
              href="/#"
              className="text-primary text-decoration-none"
              onMouseEnter={(e) => (e.target.style.textDecoration = "underline")}
              onMouseLeave={(e) => (e.target.style.textDecoration = "none")}
            >
              {isSignup ? "Login" : "Sign Up"}
            </a>
          </div>
        </form>
      </div>
    </div>
  );
}

export default LandingPage;
