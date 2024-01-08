import React from 'react';

class DeviceDropdown extends React.Component {
  render() {
    return (
      <div>
        <select>
          <option value="infinix">Infinix</option>
          <option value="tecno">Tecno</option>
          <option value="itel">Itel</option>
        </select>

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
