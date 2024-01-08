import React from 'react';
import { Link } from 'react-router-dom';

const StockRoms = () => {
  return (
    <div className="content">
      <h2>Infinix Stock ROMs</h2>
      <Link to="/stock-roms/build-number">Enter Build Number</Link>
    </div>
  );
}

export default StockRoms;
    
