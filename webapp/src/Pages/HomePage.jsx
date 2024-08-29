import React, { useEffect, useState } from "react";
import { Container, Spinner, Alert } from "react-bootstrap";
import Header from "../Components/Header";
import { useNavigate } from "react-router-dom";
import HomeTop from "../Components/HomeTop";
import { useUser } from "../Contexts/UserContext";
import HomeMiddle from "../Components/HomeMiddle";

const HomePage = () => {
  const navigate = useNavigate();
  const { getUser, user, loading, error } = useUser();
  const [profileData, setProfileData] = useState(null);
  const [healthScore, setHealthScore] = useState(null);
  const [conditions, setConditions] = useState(null);
  const [latestBiometrics, setLatestBiometrics] = useState(null);

  const token = localStorage.getItem("token");

  useEffect(() => {
    if (!token) {
      navigate("/login");
    } else {
      getUser();
    }
  }, [navigate, token, getUser]);

  useEffect(() => {
    if (user) {
      setProfileData(user.user || null);
      setHealthScore(user.health_score || null);
      setConditions(user.conditions || null);
      setLatestBiometrics(user.latest_biometrics || null);
    }
  }, [user]);

  if (loading) {
    return <Spinner animation="border" className="d-block mx-auto mt-5" />;
  }

  if (error) {
    return (
      <Alert variant="danger" className="d-block mx-auto mt-5">
        {error}
      </Alert>
    );
  }

  console.log(latestBiometrics);
  
  const biometrics = user ? user.biometrics || [] : [];

  return (
    <div className="min-vh-100">
      <Header isLoggedIn={!!token} />
      <Container className="d-flex flex-grow-1 align-items-center justify-content-center flex-column">
        <HomeTop
          profileData={profileData}
          healthScore={healthScore}
          conditions={conditions}
          latesBiometrics={latestBiometrics}
        />
        <HomeMiddle
          biometrics={biometrics}
        />
      </Container>
    </div>
  );
};

export default HomePage;
