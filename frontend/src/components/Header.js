import React from 'react';
import { Link } from 'react-router-dom';
import './header.css';
import logo from '../logo.png';

function Header() {
  return (
    <div className="pc-header">
      <div className="pc-top-bar">
        <img src={logo} alt="Logo" className="pc-logo" />
      </div>

      <nav className="pc-nav-bar">
        <ul className="pc-menu">
          <li><Link to="/" className="pc-home-button" title="Início">Home</Link></li>
          <li><a href="#">Codigo Postal</a></li>
          <li><Link to="/pluscodes">Plus Codes</Link></li>
        </ul>
      </nav>
    </div>
  );
}

export default Header;
