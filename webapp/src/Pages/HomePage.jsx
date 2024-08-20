import React, { useEffect } from "react";
import { Container } from "react-bootstrap";
import Header from "../Components/Header";
import { useNavigate } from "react-router-dom";

const HomePage = () => {
  const navigate = useNavigate()
  const token = localStorage.getItem('token');
  useEffect(() => {
   if(!token) navigate('/login');

  }, [navigate]);

  return (
    <div className="d-flex flex-column min-vh-100">
      <Header isLoggedIn={false} />
      <Container className="d-flex flex-grow-1 align-items-center justify-content-center"></Container>
    </div>
  );
};

export default HomePage;