import React, { useEffect, useState } from 'react';
import { Container } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';
import Header from '../Components/Header';
import ProfileSection from '../Components/ProfileSection';
import BiometricsSection from '../Components/BiometricsSection';
import { useUser } from '../Contexts/UserContext';

const ProfilePage = () => {
  const navigate = useNavigate();
  const { getUser, user } = useUser();
  const [profileData, setProfileData] = useState(null);
  const [biometrics, setBiometrics] = useState(null);
  const token = localStorage.getItem("token");

  useEffect(() => {
    if (!token) {
      navigate('/login');
    } else {
      getUser();
    }
  }, [navigate, token, getUser]);
  
  useEffect(() => {
    if (user) {
      setProfileData(user.user);
      setBiometrics(user.latest_biometrics);
    }
  }, [user]);
  
  return (
    <div className="profile-page">
      <Header />
      <Container>
        {profileData && <ProfileSection userProfile={profileData} onUpdate={getUser} />}
        {biometrics && <BiometricsSection biometrics={biometrics} onUpdate={getUser} />}
      </Container>
    </div>
  );
};

export default ProfilePage;
