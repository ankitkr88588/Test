import React from 'react';
import { BrowserRouter as Router, Route, Link, Switch } from 'react-router-dom';
import './App.css';

// Components
import Home from './Home';
import RootFiles from './RootFiles';
import StockRoms from './StockRoms';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <h1>Welcome to Your Infinix Page!</h1>
          <nav>
            <Link to="/">Home</Link>
            <Link to="/root-files">Infinix Root Files</Link>
            <Link to="/stock-roms">Infinix Stock ROMs</Link>
          </nav>
        </header>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/root-files" component={RootFiles} />
          <Route exact path="/stock-roms" component={StockRoms} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
