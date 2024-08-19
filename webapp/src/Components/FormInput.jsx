import React from 'react';
import { Form } from 'react-bootstrap';

const FormInput = ({ controlId, type, placeholder, required, value, onChange }) => {
  return (
    <Form.Group controlId={controlId} className="mb-4">
      <Form.Control
        type={type}
        placeholder={placeholder}
        required={required}
        value={value}
        onChange={onChange}
        className="form-input"
      />
    </Form.Group>
  );
};

export default FormInput;
