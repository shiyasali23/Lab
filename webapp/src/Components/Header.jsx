import React from 'react';
import { Link } from 'react-router-dom';
import { useUser } from '../Contexts/UserContext';

const Header = () => {
  const { logout, setUser } = useUser();

  const token = localStorage.getItem('token');
  const isLoggedIn = !!token;

  const disabledStyle = {
    pointerEvents: 'none',
    display: 'none',
    cursor: 'not-allowed',
  };

  const handleLogout = async () => {
    localStorage.removeItem('token');
    setUser(null);
    await logout();
  };

  return (
    <header className="bg-white shadow-sm py-3">
      <div className="container">
        <div className="row align-items-center">
          <div className="col-4">
            <Link to="/home" className="text-dark text-center text-decoration-none">
              <h1 className="h4 mb-0 text-dark ms-4">Lab</h1>
            </Link>
          </div>
          <div className="col-8">
            <nav className="d-flex justify-content-end">
              <Link
                to="/profile"
                className="text-dark text-center text-decoration-none"
                style={!isLoggedIn ? disabledStyle : {}}
                aria-disabled={!isLoggedIn}
              >
                <i className="fa-regular fa-user d-block mb-1"></i>
                <span>Profile</span>
              </Link>
              <Link
                to="/hospital"
                className="text-dark text-center text-decoration-none"
                style={!isLoggedIn ? disabledStyle : {}}
                aria-disabled={!isLoggedIn}
              >
                <i className="fa-regular fa-hospital d-block mb-1"></i>
                <span>Hospital</span>
              </Link>
              <Link
                to="/history"
                className="text-dark text-center text-decoration-none"
                style={!isLoggedIn ? disabledStyle : {}}
                aria-disabled={!isLoggedIn}
              >
                <i className="fa-regular fa-file d-block mb-1"></i>
                <span>Report</span>
              </Link>
              {isLoggedIn && (
                <div
                  className="text-dark text-center text-decoration-none"
                  onClick={handleLogout} 
                  style={{ cursor: 'pointer' }}
                >
                  <i className="fa-solid fa-right-from-bracket d-block mb-1"></i>
                  <span>Logout</span>
                </div>
              )}
            </nav>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
