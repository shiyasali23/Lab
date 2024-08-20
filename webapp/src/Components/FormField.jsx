// src/components/FormField.js

import React from 'react';
import { Form } from 'react-bootstrap';

const FormField = ({ name, label, value, onChange, type = "text", options }) => {
  return (
    <Form.Group className="mb-3 col-lg-3 col-md-4 col-sm-6">
      <Form.Label>{label}</Form.Label>
      {type === "select" ? (
        <Form.Control
          as="select"
          name={name}
          value={value || ''}
          onChange={onChange}
          className="form-input"
        >
          {options.map((option) => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))}
        </Form.Control>
      ) : (
        <Form.Control
          type={type}
          name={name}
          value={value || ''}
          onChange={onChange}
          className="form-input"
        />
      )}
    </Form.Group>
  );
};

export default FormField;
