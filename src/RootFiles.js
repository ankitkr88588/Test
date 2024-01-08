import React from 'react';
import { Link } from 'react-router-dom';

const RootFiles = () => {
  return (
    <div className="content">
      <h2>Infinix Root Files</h2>
      <Link to="/root-files/build-number">Enter Build Number</Link>
    </div>
  );
}

export default RootFiles;
  
