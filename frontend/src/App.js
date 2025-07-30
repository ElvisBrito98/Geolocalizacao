import './App.css';
import logo from './logo.png'; 



function App() {
  return (
    <div className="App">
      {/* Faixa branca com logotipo à esquerda*/}
      <div className="top-bar">
        <img src={logo} alt="Logo" className="logo" />
      </div>

      {/* Barra vermelha com menu alinhado à esquerda */}
      <nav className="nav-bar">
        <ul className="menu">
          <li><a href="#" className="home-button" title="Início">Home</a></li>
          <li><a href="#">Codigo Postal</a></li>
          <li><a href="#">Plus Codes</a></li>
          {/* <li><a href="#">FERRAMENTAS</a></li> */}
          {/* <li><a href="#">PRODUTOS</a></li> */}
        </ul>
      </nav>

      {/* Espaço publicitário */}
      <div className="ad-space">
        <p>Espaço reservado para futuras publicidades</p>
      </div>
    </div>
  );
}

export default App;
