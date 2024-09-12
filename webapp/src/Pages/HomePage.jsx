import React, { useEffect, useState } from "react";
import { Container} from "react-bootstrap";
import Header from "../Components/Header";
import { useNavigate } from "react-router-dom";
import HomeTop from "../Components/HomeTop";
import { useUser } from "../Contexts/UserContext";
import HomeMiddle from "../Components/HomeMiddle";
import HomeBottom from "../Components/HomeBottom";
import ModelsContainer from "../Components/ModelsContainer";

const HomePage = () => {
  const navigate = useNavigate();
  const { getUser, user } = useUser();
  const [profileData, setProfileData] = useState(null);
  const [healthScore, setHealthScore] = useState(null);
  const [conditions, setConditions] = useState(null);
  const [latestBiometrics, setLatestBiometrics] = useState(null);
  const [biometrics, setBiometrics] = useState([]);
  const [foodScore, setFoodScore] = useState(null);

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
      const { weight_kg, height_cm, date_of_birth } = user.user || {};
      const bmi = weight_kg && height_cm ? weight_kg / (height_cm / 100) ** 2 : null;
      const age = date_of_birth ? Math.floor((new Date() - new Date(date_of_birth)) / (1000 * 60 * 60 * 24 * 365.25)) : null;
  
      setProfileData({
        ...user.user,
        bmi: bmi ? bmi.toFixed(2) : null,
        age
      });
      setHealthScore(user.health_score || null);
      setConditions(user.conditions || null);
      setLatestBiometrics(user.latest_biometrics || null);
      setFoodScore(user.food_scores || null);
      setBiometrics(user.biometrics || []);
    }
  }, [user]);
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
        <ModelsContainer latestBiometrics={latestBiometrics} profileData={profileData}/>
        <HomeBottom foodScore={foodScore} biometrics={biometrics}/>
      </Container>
    </div>
  );
};

export default HomePage;
