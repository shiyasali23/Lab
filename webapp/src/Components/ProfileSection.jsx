import React, { useState, useEffect } from "react";
import { Card, Form, Button, Alert, Spinner } from "react-bootstrap";
import { useUser } from "../Contexts/UserContext";

const ProfileSection = ({ userProfile }) => {
  const { loading, updateUser, deactivateUser, error } = useUser();
  const [profile, setProfile] = useState({});
  const [originalProfileData, setOriginalProfileData] = useState({});
  const [localStatus, setLocalStatus] = useState({ errors: [], success: false });

  useEffect(() => setProfile(userProfile || {}), [userProfile]);
  useEffect(() => setOriginalProfileData(userProfile || {}), [userProfile]);

  const handleChange = (e) => setProfile({ ...profile, [e.target.name]: e.target.value });

  const validateForm = (data) => {
    const validations = { first_name: "First name is required", last_name: "Last name is required", email: "Email is required", phone_number: "Phone number must be exactly 10 digits", gender: "Gender is required" };
    return Object.keys(validations).filter((field) => (field === "phone_number" ? !/^\d{10}$/.test(data[field]) : !data[field].trim())).map((field) => validations[field]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const errors = validateForm(profile);
    if (errors.length) return setLocalStatus({ errors, success: false });

    const updatedFields = Object.keys(profile).reduce((acc, key) => {
      const value = profile[key];
      if (value !== originalProfileData[key] && value !== false) {
        acc[key] = value === '' ? null : value;
      }
      return acc;
    }, {});

    if (!Object.keys(updatedFields).length) {
      setLocalStatus({ errors: ["No changes detected."], success: false });
      return;
    }

    const updatedUser = await updateUser(updatedFields);
    setLocalStatus({
      errors: updatedUser ? [] : ["Failed to update profile."],
      success: !!updatedUser,
    });
  };

  const handleDeactivate = async () => await deactivateUser();

  return (
    <Card className="primary-card">
      <Card.Body>
        <h2 className="text-start">Profile</h2>
        <p style={{ cursor: "pointer" }} className="mb-4 text-end d-block text-danger" onClick={handleDeactivate}><i className="me-2 text-end fa-regular fa-trash-can"></i>Delete Account</p>
        {loading && <Spinner animation="border" className="d-block mx-auto mb-4" />}
        {error && <Alert variant="danger" className="mb-4">{error}</Alert>}
        {localStatus.errors.length > 0 && <Alert variant="danger" className="mb-4"><ul className="mb-0">{localStatus.errors.map((err, i) => <li key={i}>{err}</li>)}</ul></Alert>}
        {localStatus.success && <Alert variant="success" className="mb-4">Profile updated successfully!</Alert>}
        <Form onSubmit={handleSubmit}>
          <div className="row">
            {["first_name", "last_name", "email", "phone_number", "gender", "job", "city", "date_of_birth", "height_cm", "weight_kg", "address"].map((field) => (
              <Form.Group className="mb-3 col-lg-3 col-md-4 col-sm-6" key={field}>
                <Form.Label>{field.replace(/_/g, " ").replace(/\b\w/g, (c) => c.toUpperCase())}</Form.Label>
                <Form.Control type={field === "date_of_birth" ? "date" : field === "height_cm" || field === "weight_kg" ? "number" : "text"} name={field} value={profile[field] || ""} onChange={handleChange} className="form-input" />
              </Form.Group>
            ))}
          </div>
          <Button className="save-btn" variant="dark" type="submit" disabled={loading}>{loading ? "Saving..." : "Save Changes"}</Button>
        </Form>
      </Card.Body>
    </Card>
  );
};

export default ProfileSection;