import React from 'react';
import './header.css';
import logo from '../logo.png';

function Header() {
  return (
    <div className="header">
      {/* Faixa branca com logotipo à esquerda */}
      <div className="top-bar">
        <img src={logo} alt="Logo" className="logo" />
      </div>

      {/* Barra vermelha com menu alinhado à esquerda */}
      <nav className="nav-bar">
        <ul className="menu">
          <li><a href="#" className="home-button" title="Início">Home</a></li>
          <li><a href="#">Codigo Postal</a></li>
          <li><a href="#">Plus Codes</a></li>
        </ul>
      </nav>
    </div>
  );
}

export default Header;
