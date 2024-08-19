import React, { useEffect } from "react";
import { Container } from "react-bootstrap";
import Header from "../Components/Header";
import { useNavigate } from "react-router-dom";

const HomePage = () => {
  const navigate = useNavigate();

  useEffect(() => {
    const handleStorageChange = (event) => {
      if (event.storageArea === localStorage && !localStorage.getItem("token")) {
        navigate("/login");
      }
    };
    window.addEventListener("storage", handleStorageChange);
    if (!localStorage.getItem("token")) {
      navigate("/login");
    }
    return () => window.removeEventListener("storage", handleStorageChange);
  }, [navigate]);

  return (
    <div className="d-flex flex-column min-vh-100">
      <Header isLoggedIn={true} />
      <Container className="d-flex flex-grow-1 align-items-center justify-content-center">
        {/* Page content here */}
      </Container>
    </div>
  );
};

export default HomePage;
