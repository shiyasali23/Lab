import React from 'react';
import { Link } from 'react-router-dom';

const Header = ({ handleLogout, isLoggedIn, disabledStyle }) => {
  return (
    <div style={styles.header}>
      {/* Logo */}
      <Link to="/home" className="text-dark text-center text-decoration-none" style={styles.logo}>
        <h2 className="text-dark">Biolabs</h2>
      </Link>

      {/* Right-aligned components */}
      <div style={styles.rightComponents}>
        {/* Component 1: Profile */}
        <Link
          to="/profile"
          className="text-dark text-center text-decoration-none"
          style={!isLoggedIn ? { ...styles.component, ...disabledStyle } : styles.component}
          aria-disabled={!isLoggedIn}
        >
          <i className="fa-solid fa-pen-to-square d-block mb-1"></i>
          <h6>Edit</h6>
        </Link>

        {/* Component 2: Logout */}
        <div
          className="text-dark text-center text-decoration-none"
          onClick={handleLogout}
          style={{ ...styles.component, cursor: 'pointer' }}
        >
          <i className="fa-solid fa-right-from-bracket d-block mb-1"></i>
          <h6>Logout</h6>
        </div>
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
  
};

export default Header;
