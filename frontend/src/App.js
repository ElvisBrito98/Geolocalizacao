import './App.css';
import Header from './components/header';
import Footer from './components/footer'; // 👈 Importa o Footer

function App() {
  return (
    <div className="App">
      <Header />

      {/* Espaço publicitário */}
      <div className="ad-space">
        <p>Espaço reservado para futuras publicidades</p>
      </div>

      <Footer /> {/* 👈 Chama o Footer */}
    </div>
  );
}

export default App;
