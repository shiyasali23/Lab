import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../Contexts/AuthContext';

const Header = () => {
  const { logout } = useAuth();
  const navigate = useNavigate();
  
  const [isLoggedIn, setIsLoggedIn] = useState(!!localStorage.getItem('token'));

  const handleLogout = () => {
    // Immediately navigate to the login page
    navigate('/login');

    // Perform the logout operation in the background
    logout().then(() => {
      // Once logout completes, remove token from localStorage
      localStorage.removeItem('token');
      setIsLoggedIn(false); 
    }).catch((error) => {
      console.error("Error during logout: ", error);
    });
  };

  return (
    <div style={styles.header}>
      {/* Logo */}
      <Link to="/" className="text-dark text-center text-decoration-none" style={styles.logo}>
        <h2 className="text-dark">Biolabs</h2>
      </Link>

      {/* Right-aligned components */}
      <div style={styles.rightComponents}>
        {/* Component 1: Profile */}
        {isLoggedIn && (
          <Link
            to="/profile"
            className="text-dark text-center text-decoration-none"
            style={styles.component}
          >
            <i className="fa-solid fa-pen-to-square d-block mb-1"></i>
            <h6>Edit</h6>
          </Link>
        )}

        {/* Component 2: Logout */}
        {isLoggedIn && (
          <button
            className="text-dark text-center text-decoration-none"
            onClick={handleLogout}
            style={{ ...styles.component, cursor: 'pointer', background: 'none', border: 'none' }}
          >
            <i className="fa-solid fa-right-from-bracket d-block mb-1"></i>
            <h6>Logout</h6>
          </button>
        )}
      </div>
    </div>
  );
};
const styles = {
  header: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: '10px 20px',
    position: 'relative',  
    height: '12vh',
    zIndex: 1,  
  },
  logo: {
    position: 'absolute',
    left: '50%',
    transform: 'translateX(-50%)',
    textDecoration: 'none',
  },
  rightComponents: {
    display: 'flex',
    gap: '35px',
    marginLeft: '1000px',
  },
  component: {
    textAlign: 'center',
  },
};


export default Header;
