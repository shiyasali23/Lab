import React from 'react';
import { Button } from 'react-bootstrap';

const FormButton = ({ type, variant, children }) => {
  return (
    <Button variant={variant} type={type} className="w-100 form-button">
      {children}
    </Button>
  );
};

export default FormButton;
