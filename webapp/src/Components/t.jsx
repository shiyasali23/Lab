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
    <header className="">
      <div className="container">
        <div className="row align-items-center">
          <div className="col-4">
            <Link to="/home" className="text-dark text-center text-decoration-none">
              <h1 className="h4 mb-0 text-dark ms-4">Bio labs</h1>
            </Link>
          </div>
          <div className="col-8">
            <nav className="d-flex justify-content-end">
            <Link
                to="/camera"
                className="text-dark text-center text-decoration-none"
                style={!isLoggedIn ? disabledStyle : {}}
                aria-disabled={!isLoggedIn}
              >
                <i className="fa-solid fa-camera"></i>
                <span>Scan</span>
              </Link>
              <Link
                to="/profile"
                className="text-dark text-center text-decoration-none"
                style={!isLoggedIn ? disabledStyle : {}}
                aria-disabled={!isLoggedIn}
              >
                <i className="fa-solid fa-user d-block mb-1"></i>
                <span>Profile</span>
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

const styles = {
  header: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: '10px 20px',
    position: 'relative',
    height: '15vh',
  },
  logo: {
    position: 'absolute',
    left: '50%',
    transform: 'translateX(-50%)',
    textDecoration: 'none',
  },
  rightComponents: {
    marginLeft: '1000px',
    display: 'flex',
    gap: '35px',
  },
  component: {
    marginLeft: '15px',
  },
};


export default Header;


