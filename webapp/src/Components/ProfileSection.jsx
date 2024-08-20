import React, { useContext, useState, useEffect } from "react";
import { Card, Form, Button, Alert, Spinner } from "react-bootstrap";
import FormField from "./FormField"; 
import { useUser } from "../Contexts/UserContext";

const ProfileSection = () => {
  const { loading, getUser, updateUser, deactivateUser } = useUser();
  
  const [profileData, setProfileData] = useState({
    firstName: '',
    lastName: '',
    email: '',
    phone: '',
    gender: '',
    job: '',
    city: '',
    dateOfBirth: '',
    height: '',
    weight: ''
  });
  
  const [originalProfileData, setOriginalProfileData] = useState({});
  const [status, setStatus] = useState({ loading: false, errors: [], success: false });

  useEffect(() => {
    const fetchUser = async () => {
      const fetchedUser = await getUser();
      if (fetchedUser) {
        const userData = {
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
        };
        setProfileData(userData);
        setOriginalProfileData(userData); // Store original data
      }
    };
    fetchUser();
  }, [getUser]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setProfileData({ ...profileData, [name]: value });
  };

  const validateForm = (data) => {
    const validations = {
      firstName: "First name is required.",
      lastName: "Last name is required.",
      email: "Email is required.",
      phone: "Phone number must be exactly 10 digits.",
      gender: "Gender is required.",
    };

    return Object.keys(validations)
      .filter((field) => {
        const value = data[field];
        return field === "phone" ? !/^\d{10}$/.test(value) : !value.trim();
      })
      .map((field) => validations[field]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const errors = validateForm(profileData);
    if (errors.length > 0) {
      setStatus({ ...status, errors });
      return;
    }

    // Prepare the updated fields
    const updatedFields = Object.keys(profileData).reduce((acc, key) => {
      const value = profileData[key];
      if (value !== originalProfileData[key]) {
        acc[key] = value === '' ? null : value; // Convert empty strings to null
      }
      return acc;
    }, {});

    if (Object.keys(updatedFields).length === 0) {
      setStatus({ ...status, errors: ["No changes detected."], success: false });
      return;
    }

    setStatus({ ...status, loading: true });
    const updatedUser = await updateUser({
      first_name: updatedFields.firstName,
      last_name: updatedFields.lastName,
      email: updatedFields.email,
      phone_number: updatedFields.phone,
      gender: updatedFields.gender,
      job: updatedFields.job,
      city: updatedFields.city,
      date_of_birth: updatedFields.dateOfBirth,
      height_cm: updatedFields.height,
      weight_kg: updatedFields.weight,
    });
    setStatus({
      ...status,
      loading: false,
      success: !!updatedUser,
      errors: updatedUser ? [] : ["Failed to update profile."],
    });
  };

  const handleDeactivate = async () => {
    setStatus({ ...status, loading: true });
    await deactivateUser();
    setStatus({ ...status, loading: false });
  };

  return (
    <Card className="profile-card">
      <Card.Body>
        <span
          style={{ color: "red", cursor: "pointer" }}
          className="me-4 mb-4 text-end d-block mb-1"
          onClick={handleDeactivate}
        >
          <i className="me-2 text-end fa-regular fa-trash-can"></i>
          Delete Account
        </span>

        <Form onSubmit={handleSubmit}>
          {loading && (
            <Spinner animation="border" className="d-block mx-auto mb-4" />
          )}
          {status.errors.length > 0 && (
            <Alert variant="danger">
              <ul className="mb-0">
                {status.errors.map((err, index) => (
                  <li key={index}>{err}</li>
                ))}
              </ul>
            </Alert>
          )}
          {status.success && !status.loading && (
            <Alert variant="success">Profile updated successfully!</Alert>
          )}
          <div className="row">
            {[
              { name: "firstName", label: "First Name", type: "text" },
              { name: "lastName", label: "Last Name", type: "text" },
              { name: "email", label: "Email", type: "email" },
              { name: "phone", label: "Phone Number", type: "text" },
              { name: "gender", label: "Gender", type: "text" },
              { name: "job", label: "Job", type: "text" },
              { name: "city", label: "City", type: "text" },
              { name: "dateOfBirth", label: "Date of Birth", type: "date" },
              { name: "height", label: "Height (cm)", type: "number" },
              { name: "weight", label: "Weight (kg)", type: "number" },
            ].map(({ name, label, type }) => (
              <FormField
                key={name}
                name={name}
                label={label}
                type={type}
                value={profileData[name]}
                onChange={handleChange}
              />
            ))}
          </div>
          <Button
            className="save-btn"
            variant="dark"
            type="submit"
            disabled={loading}
          >
            {loading ? "Saving..." : "Save Changes"}
          </Button>
        </Form>
      </Card.Body>
    </Card>
  );
};

export default ProfileSection;
