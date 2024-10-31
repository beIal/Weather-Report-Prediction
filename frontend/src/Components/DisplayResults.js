import React from 'react'; 
import PropTypes from 'prop-types'; 

const ResultDisplay = ({ result }) => { 
    return ( 
        <div>
        {result && <p>{result}</p>}
      </div>
    );
}; 

ResultDisplay.PropTypes = { 
    result: PropTypes.string,
}; 

export default ResultDisplay;