import React from 'react';
import { Form } from 'react-bootstrap';

const FormSelect = ({ controlId, options, required, value, onChange }) => {
  return (
    <Form.Group controlId={controlId} className="mb-4">
      <Form.Control
        as="select"
        required={required}
        value={value}
        onChange={onChange}
        className="form-input"
      >
        {options.map((option, index) => (
          <option key={index} value={option.value}>
            {option.label}
          </option>
        ))}
      </Form.Control>
    </Form.Group>
  );
};

export default FormSelect;
