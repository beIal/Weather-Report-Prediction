import React from 'react';
import PropTypes from 'prop-types';
import './ErrorAlert.css'; // Optional: Add some styles

const ErrorAlert = ({ message, onClose }) => {
  if (!message) return null; // Don't render if there's no message

  return (
    <div className="error-alert">
      <div className="error-content">
        <span className="error-message">{message}</span>
        <button className="close-btn" onClick={onClose}>X</button>
      </div>
    </div>
  );
};

// PropTypes for validation
ErrorAlert.propTypes = {
  message: PropTypes.string,
  onClose: PropTypes.func.isRequired,
};

export default ErrorAlert;
 
