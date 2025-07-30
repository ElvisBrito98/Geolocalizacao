import React, { useState } from 'react';
import { MapContainer, TileLayer, useMap } from 'react-leaflet';
import Header from '../components/header';
import Footer from '../components/footer';
import 'leaflet/dist/leaflet.css';

// Componente para mudar a view do mapa
function ChangeView({ center, zoom }) {
  const map = useMap();
  map.setView(center, zoom);
  return null;
}

function Pluscodes() {
  const defaultPosition = [14.917039, -23.507523];
  const [mapCenter, setMapCenter] = useState(defaultPosition);
  const [zoom, setZoom] = useState(14);

  // Estados para inputs
  const [latInput, setLatInput] = useState('');
  const [lngInput, setLngInput] = useState('');
  const [pluscodeInput, setPluscodeInput] = useState('');

  // Apenas atualizam o centro do mapa, sem validações
  const handleSearchLatLng = (e) => {
    e.preventDefault();
    const lat = parseFloat(latInput);
    const lng = parseFloat(lngInput);
    setMapCenter([lat, lng]);
    setZoom(15);
  };

  const handleSearchPluscode = (e) => {
    e.preventDefault();
    // Aqui você vai chamar sua API para converter pluscode em lat/lng
    // Por enquanto só deixo o pluscode no console e mantenho o mapa
    console.log('Pluscode para buscar:', pluscodeInput);
    // Você pode depois setar o centro assim que receber resposta da API
  };

  return (
    <div className="App">
      <Header />

      <div className="container mt-4">
        <div className="row">
          <div className="col-md-9">
            <MapContainer
              center={mapCenter}
              zoom={zoom}
              style={{ height: '500px', width: '100%' }}
            >
              <ChangeView center={mapCenter} zoom={zoom} />
              <TileLayer
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
              />
              {/* Marker removido para não mostrar nenhum marcador */}
            </MapContainer>
          </div>

          <div className="col-md-3">
            <form onSubmit={handleSearchLatLng} className="mb-4">
              <h5>Buscar por Latitude/Longitude</h5>
              <div className="mb-3">
                <label htmlFor="latitude" className="form-label">
                  Latitude
                </label>
                <input
                  type="number"
                  step="any"
                  className="form-control"
                  id="latitude"
                  value={latInput}
                  onChange={(e) => setLatInput(e.target.value)}
                  placeholder="-23.55052"
                />
              </div>
              <div className="mb-3">
                <label htmlFor="longitude" className="form-label">
                  Longitude
                </label>
                <input
                  type="number"
                  step="any"
                  className="form-control"
                  id="longitude"
                  value={lngInput}
                  onChange={(e) => setLngInput(e.target.value)}
                  placeholder="-46.633308"
                />
              </div>
              <button type="submit" className="btn btn-primary w-100">
                Procurar
              </button>
            </form>

            <form onSubmit={handleSearchPluscode}>
              <h5>Buscar por Pluscode</h5>
              <div className="mb-3">
                <label htmlFor="pluscode" className="form-label">
                  Pluscode completo
                </label>
                <input
                  type="text"
                  className="form-control"
                  id="pluscode"
                  value={pluscodeInput}
                  onChange={(e) => setPluscodeInput(e.target.value)}
                  placeholder="7FG9V3Q2+G9"
                />
              </div>
              <button type="submit" className="btn btn-primary w-100">
                Procurar
              </button>
            </form>
          </div>
        </div>
      </div>

      <Footer />
    </div>
  );
}

export default Pluscodes;
