import React, { useEffect, useState } from 'react';
import { Container, Spinner, Alert } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';
import Header from '../Components/Header';
import ProfileSection from '../Components/ProfileSection';
import BiometricsSection from '../Components/BiometricsSection';
import { useUser } from '../Contexts/UserContext';

const ProfilePage = () => {
  const navigate = useNavigate();
  const { getUser, user, loading, error } = useUser();
  const [profileData, setProfileData] = useState(null);
  const [biometrics, setBiometrics] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      navigate('/login');
    } else {
      getUser();
    }
  }, [navigate, getUser]);

  useEffect(() => {
    if (user) {
      setProfileData(user.user);
      setBiometrics(user.biometrics);
    }
  }, [user]);

  if (loading) {
    return <Spinner animation="border" className="d-block mx-auto mt-5" />;
  }

  if (error) {
    return <Alert variant="danger" className="d-block mx-auto mt-5">{error}</Alert>;
  }

  return (
    <div className="profile-page">
      <Header />
      <Container>
        {profileData && <ProfileSection userProfile={profileData} />}
        {biometrics && <BiometricsSection biometrics={biometrics} />}
      </Container>
    </div>
  );
};

export default ProfilePage;
