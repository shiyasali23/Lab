import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useUser } from "../Contexts/UserContext";
import Header from "../Components/Header";
import ProfileComponent from "../Components/ProfileComponent";
import AnalyticsComponent from "../Components/AnalyticsComponent";
import ModelsComponent from "../Components/ModelsComponent";
import FoodRecomendationComponent from "../Components/FoodRecomendationComponent";
import SpinnerComponent from "../Components/SpinnerComponent";
import { useNutrient } from "../Contexts/NutrientContext";
import DiagnosisComponent from "../Components/DiagnosisComponent";

const MainPage = () => {
  const navigate = useNavigate();
  const { getUser, user, userLoading } = useUser();
  const { getNutrients } = useNutrient();

  const [userData, setUserData] = useState(null);
  const [healthScore, setHealthScore] = useState(null);
  const [conditions, setConditions] = useState(null);
  const [latestBiometrics, setLatestBiometrics] = useState(null);
  const [biometrics, setBiometrics] = useState([]);
  const [foodScores, setFoodScores] = useState(null);
  const [activeTab, setActiveTab] = useState("profile");

  const token = localStorage.getItem("token");

  useEffect(() => {
    if (!token) {
      navigate("/login");
    } else {
      getUser();
      getNutrients();
    }
  }, [navigate, token, getUser, getNutrients]);

  useEffect(() => {
    if (user) {
      const { weight_kg, height_cm, date_of_birth } = user.user || {};
      const bmi =
        weight_kg && height_cm ? weight_kg / (height_cm / 100) ** 2 : null;
      const age = date_of_birth
        ? Math.floor(
            (new Date() - new Date(date_of_birth)) /
              (1000 * 60 * 60 * 24 * 365.25)
          )
        : null;

      setUserData({ ...user.user, bmi: bmi ? bmi.toFixed(2) : null, age });
      setHealthScore(user.health_score || null);
      setConditions(user.conditions || null);
      setLatestBiometrics(user.latest_biometrics || null);
      setFoodScores(user.food_scores || null);
      setBiometrics(user.biometrics || []);
    }
  }, [user]);

  const handleTabClick = (id) => {
    setActiveTab(id);
  };

  const tabs = [
    {
      id: "profile",
      label: "Profile",
      icon: "fa-user",
      component: (
        <ProfileComponent
          userData={userData}
          healthScore={healthScore}
          conditions={conditions}
          latestBiometrics={latestBiometrics}
        />
      ),
    },
    {
      id: "analytics",
      label: "Analytics",
      icon: "fa-chart-column",
      component: <AnalyticsComponent biometrics={biometrics} />,
    },
    {
      id: "ai-models",
      label: "Ai Models",
      icon: " fa-brain",
      component: (
        <ModelsComponent
          userData={userData}
          latestBiometrics={latestBiometrics}
        />
      ),
    },
    {
      id: "diagnosis",
      label: "Diagnosis",
      icon: " fa-stethoscope",
      component: (
        <DiagnosisComponent
          userData={userData}
        />
      ),
    },
    {
      id: "food-recommendation",
      label: "Food Recommendation",
      icon: "fa-bowl-rice",
      component: <FoodRecomendationComponent foodScores={foodScores} />,
    },
  ];

  const TabButton = ({ id, label, icon }) => (
    <li className="nav-item" role="presentation">
      <button
        className={`nav-link ${activeTab === id ? "active" : ""} text-dark`}
        id={`${id}-tab`}
        onClick={() => handleTabClick(id)}
        type="button"
        role="tab"
        aria-controls={id}
        aria-selected={activeTab === id}
        style={styles.button}
      >
        <i className={`fa-solid ${icon}`}></i>
        <h6 style={styles.label}>{label}</h6>
      </button>
    </li>
  );

  return (
    <div>
      <Header />
      <div className="p-3" style={styles.container}>
        <ul
          className="d-flex justify-content-center align-items-center nav"
          role="tablist"
          style={styles.ul}
        >
          {tabs.map((tab) => (
            <TabButton key={tab.id} {...tab} />
          ))}
        </ul>
        <div style={styles.content} id="myTabContent" className="tab-content">
          {userLoading ? (
            <SpinnerComponent />
          ) : !userData ? (
            <div style={styles.centeredMessage}>
              <span className="badge rounded-pill bg-secondary">
                User Data not available
              </span>
            </div>
          ) : (
            tabs.map((tab) => (
              <div
                key={tab.id}
                className={`tab-pane fade w-100 h-100 ${
                  activeTab === tab.id ? "show active" : ""
                }`}
                id={tab.id}
                role="tabpanel"
                aria-labelledby={`${tab.id}-tab`}
              >
                {tab.component}
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
};

const styles = {
  button: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    flexDirection: "column",
    color: "black",
    width: "100%",
    height: "100%",
  },
  ul: {
    gap: "10px",
    height: "12%",
    border: "none",
    backgroundColor: "white",
  },
  container: {
    width: "99%",
    margin: "auto",
    height: "87vh",
  },
  content: {
    width: "100%",
    height: "88%",
  },
  centeredMessage: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    height: "100%",
    width: "100%",
  },
  label: {
    fontSize: "18px",
    letterSpacing: "1px",
    marginTop: "5px",
  },
};

export default MainPage;
