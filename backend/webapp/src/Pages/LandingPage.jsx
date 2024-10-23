// src/LandingPage.js
import React from 'react';


function LandingPage() {
  return (
    <div className="LandingPage">
      {/* Main container */}
      <div className="container-fluid landing-page">
        <div className="row align-items-center vh-100">
          {/* Left Side - Animation & Text */}
          <div className="col-md-7 text-left p-5">
            <div className="welcome-animation">
              <h1 className="display-4">Welcome to Biolabs</h1>
              <p className="lead mt-4">
                A space where healing meets trust. We provide state-of-the-art medical care with a focus on wellness, compassion, and advanced research.
              </p>
            </div>
            {/* Add a calming image */}
            <img
              src="https://via.placeholder.com/600x400"
              alt="Biolabs Hospital"
              className="img-fluid rounded shadow-lg mt-4"
            />
          </div>

          {/* Right Side - Login/Signup */}
          <div className="col-md-5 d-flex flex-column justify-content-center align-items-center bg-light p-5 shadow-lg">
            <h2 className="text-center mb-4">Join Us</h2>
            <form className="w-100">
              {/* Signup Form */}
              <div className="form-group mb-3">
                <label for="signupEmail">Email</label>
                <input
                  type="email"
                  className="form-control"
                  id="signupEmail"
                  placeholder="Enter email"
                />
              </div>
              <div className="form-group mb-3">
                <label for="signupPassword">Password</label>
                <input
                  type="password"
                  className="form-control"
                  id="signupPassword"
                  placeholder="Password"
                />
              </div>
              <div className="form-group mb-4">
                <label for="confirmPassword">Confirm Password</label>
                <input
                  type="password"
                  className="form-control"
                  id="confirmPassword"
                  placeholder="Confirm Password"
                />
              </div>
              <button type="submit" className="btn btn-primary w-100 mb-3">
                Sign Up
              </button>
              <hr />
              {/* Login */}
              <h5 className="text-center">Already have an account?</h5>
              <div className="form-group mb-3">
                <label for="loginEmail">Email</label>
                <input
                  type="email"
                  className="form-control"
                  id="loginEmail"
                  placeholder="Enter email"
                />
              </div>
              <div className="form-group mb-4">
                <label for="loginPassword">Password</label>
                <input
                  type="password"
                  className="form-control"
                  id="loginPassword"
                  placeholder="Password"
                />
              </div>
              <button type="submit" className="btn btn-outline-primary w-100">
                Log In
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

export default LandingPage;
