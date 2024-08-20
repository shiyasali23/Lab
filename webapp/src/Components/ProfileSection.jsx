import React, { useState, useEffect } from "react";
import { Card, Form, Button, Alert, Spinner } from "react-bootstrap";
import FormField from "./FormField";
import { useUser } from "../Contexts/UserContext";

const ProfileSection = ({ profileData }) => {
  const { loading, updateUser, deactivateUser, error } = useUser();

  const [profile, setProfile] = useState(profileData || {});
  const [originalProfileData, setOriginalProfileData] = useState(profileData || {});
  const [status, setStatus] = useState({ loading: false, errors: [], success: false });

  useEffect(() => {
    if (profileData) {
      setProfile(profileData);
      setOriginalProfileData(profileData);
    } else {
      setProfile({});
      setOriginalProfileData({});
    }
  }, [profileData]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setProfile({ ...profile, [name]: value });
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
    const errors = validateForm(profile);
    if (errors.length > 0) {
      setStatus({ ...status, errors });
      return;
    }

    const updatedFields = Object.keys(profile).reduce((acc, key) => {
      const value = profile[key];
      if (value !== originalProfileData[key]) {
        acc[key] = value === '' ? null : value;
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

  if (!profileData) {
    return (
      <Card className="profile-card">
        <Card.Body>
          <Alert variant="danger">Failed to load profile data.</Alert>
        </Card.Body>
      </Card>
    );
  }

  return (
    <Card className="profile-card">
      <Card.Body>
      <h2 className="text-start">Profile</h2>
        <span
          style={{ color: "red", cursor: "pointer" }}
          className=" mb-4 text-end d-block"
          onClick={handleDeactivate}
        >
          <i className="me-2 text-end fa-regular fa-trash-can"></i>
          Delete Account
        </span>

        <Form onSubmit={handleSubmit}>
          {status.loading && (
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
          {error && !status.loading && (
            <Alert variant="danger">{error}</Alert>
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
                value={profile[name] || ''}
                onChange={handleChange}
              />
            ))}
          </div>
          <Button
            className="save-btn"
            variant="dark"
            type="submit"
            disabled={status.loading}
          >
            {status.loading ? "Saving..." : "Save Changes"}
          </Button>
        </Form>
      </Card.Body>
    </Card>
  );
};

export default ProfileSection;
