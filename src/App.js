import React from 'react';
import './DeviceDropdown.css'; // Import CSS for styling (create this file)

class DeviceDropdown extends React.Component {
  render() {
    return (
      <div className="container">
        <h1>Welcome to Device Selector</h1>
        <div className="dropdown">
          <select className="dropdown-select">
            <option value="select">Select a Device</option>
            <option value="infinix">Infinix</option>
            <option value="tecno">Tecno</option>
            <option value="itel">Itel</option>
          </select>
        </div>

        {/* Insert the AdSense script */}
        <script
          async
          src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5956825596826996"
          crossorigin="anonymous"
        ></script>
      </div>
    );
  }
}

export default DeviceDropdown;
