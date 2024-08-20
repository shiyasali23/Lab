import React, { useEffect, useState } from 'react';
import { Container, Spinner } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom'; 
import Header from '../Components/Header';
import ProfileSection from '../Components/ProfileSection';
import { useUser } from '../Contexts/UserContext';
import BiometricsSection from '../Components/BiometricsSection';

const ProfilePage = () => {
  const navigate = useNavigate();
  const { getUser } = useUser();
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const fetchedUser = await getUser();
        if (fetchedUser) {
          setUser({
            firstName: fetchedUser.user.first_name || '',
            lastName: fetchedUser.user.last_name || '',
            email: fetchedUser.user.email || '',
            phone: fetchedUser.user.phone_number || '',
            gender: fetchedUser.user.gender || '',
            job: fetchedUser.user.job || '',
            city: fetchedUser.user.city || '',
            dateOfBirth: fetchedUser.user.date_of_birth || '',
            height: fetchedUser.user.height_cm || '',
            weight: fetchedUser.user.weight_kg || ''
          });
        }
      } catch (error) {
        console.error("Failed to fetch user data", error);
      } finally {
        setLoading(false);
      }
    };

    const token = localStorage.getItem("token");
    if (!token) {
      navigate('/login');
    } else {
      fetchUser();
    }
  }, [navigate, getUser]);

  if (loading) {
    return <Spinner animation="border" className="d-block mx-auto mt-5" />;
  }

  return (
    <div className="profile-page">
      <Header />
      <Container>
      <ProfileSection profileData={user} />
      <BiometricsSection/>
      </Container>
    </div>
  );
};

export default ProfilePage;
