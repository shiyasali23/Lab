import React, { useEffect } from 'react';
import { Container } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom'; 
import Header from '../Components/Header';
import ProfileSection from '../Components/ProfileSection';

const ProfilePage = () => {
  const navigate = useNavigate(); 

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      navigate('/login');
    }
  }, [navigate]); 

  return (
    <div className="profile-page">
      <Header/>
      <Container>
        <ProfileSection/>
      </Container>
    </div>
  );
};

export default ProfilePage;
