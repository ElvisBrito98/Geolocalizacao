import React, { useState, useRef, useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup, useMapEvents } from 'react-leaflet';
import L from 'leaflet';
import Header from '../components/header';
import Footer from '../components/footer';
import 'leaflet/dist/leaflet.css';

// Configuração do ícone
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});

function MapClickHandler({ onDoubleClick }) {
  useMapEvents({
    dblclick(e) {
      onDoubleClick(e.latlng);
    }
  });
  return null;
}

function Pluscodes() {
  const defaultPosition = [14.917039, -23.507523];
  const [position, setPosition] = useState(defaultPosition);
  const [latInput, setLatInput] = useState('');
  const [lngInput, setLngInput] = useState('');
  const [pluscodeInput, setPluscodeInput] = useState('');
  const [apiResult, setApiResult] = useState(null);
  const [apiError, setApiError] = useState(null);
  const mapRef = useRef(null);

  // Atualização do mapa
  useEffect(() => {
    if (mapRef.current) {
      mapRef.current.flyTo(position, 16, { duration: 1 });
    }
  }, [position]);

  const searchAtPosition = async (lat, lng) => {
    try {
      const response = await fetch(`http://localhost:8000/api/pluscode?lat=${lat}&lng=${lng}`);
      const data = await response.json();
      
      if (!response.ok) throw new Error(data.error || 'Erro na API');
      
      setApiResult(data);
      setApiError(null);
    } catch (error) {
      setApiError(error.message);
    }
  };

  const handleMapDoubleClick = (latlng) => {
    const { lat, lng } = latlng;
    setPosition([lat, lng]);
    setLatInput(lat.toFixed(6));
    setLngInput(lng.toFixed(6));
    searchAtPosition(lat, lng);
  };

  const handleSearchLatLng = async (e) => {
    e.preventDefault();
    const lat = parseFloat(latInput);
    const lng = parseFloat(lngInput);
    
    if (!isNaN(lat) && !isNaN(lng)) {
      setPosition([lat, lng]);
      await searchAtPosition(lat, lng);
    }
  };

  // Formulário inativo de Plus Code
  const handlePluscodeSubmit = (e) => {
    e.preventDefault();
    setApiError("Funcionalidade em desenvolvimento");
    setApiResult({
      plus_code: pluscodeInput,
      message: "Busca por Plus Code estará disponível em breve"
    });
  };

  return (
    <div className="App">
      <Header />

      <div className="container mt-4">
        <div className="row">
          <div className="col-md-9">
            <MapContainer
              center={position}
              zoom={14}
              style={{ height: '500px', width: '100%' }}
              ref={mapRef}
              doubleClickZoom={false}
            >
              <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                attribution='&copy; OpenStreetMap'
              />
              <Marker position={position}>
                <Popup>
                  {apiResult?.plus_code || "Clique duas vezes para pesquisar"}
                </Popup>
              </Marker>
              <MapClickHandler onDoubleClick={handleMapDoubleClick} />
            </MapContainer>
          </div>

          <div className="col-md-3">
            {/* Formulário ativo - Coordenadas */}
            <form onSubmit={handleSearchLatLng} className="mb-4">
              <h5>Buscar por Coordenadas</h5>
              <div className="mb-3">
                <label className="form-label">Latitude</label>
                <input
                  type="number"
                  step="0.000001"
                  className="form-control"
                  value={latInput}
                  onChange={(e) => setLatInput(e.target.value)}
                  placeholder="14.917039"
                />
              </div>
              <div className="mb-3">
                <label className="form-label">Longitude</label>
                <input
                  type="number"
                  step="0.000001"
                  className="form-control"
                  value={lngInput}
                  onChange={(e) => setLngInput(e.target.value)}
                  placeholder="-23.507523"
                />
              </div>
              <button type="submit" className="btn btn-primary w-100">
                Buscar
              </button>
            </form>

            {/* Formulário inativo - Plus Code */}
            <form onSubmit={handlePluscodeSubmit} className="mb-4">
              <h5>Buscar por Plus Code</h5>
              <div className="mb-3">
                <label className="form-label">Código</label>
                <input
                  type="text"
                  className="form-control"
                  value={pluscodeInput}
                  onChange={(e) => setPluscodeInput(e.target.value)}
                  placeholder="7FG9V3Q2+G9"
                  disabled
                />
              </div>
              <button 
                type="submit" 
                className="btn btn-secondary w-100"
                disabled
              >
                Em Desenvolvimento
              </button>
            </form>

            {/* Resultados */}
            {apiResult && (
              <div className={`alert ${apiResult.message ? 'alert-info' : 'alert-success'}`}>
                {apiResult.plus_code && (
                  <>
                    <p><strong>Plus Code (11 dígitos):</strong> {apiResult.plus_code}</p>
                    <p><strong>Coordenadas:</strong> {position[0].toFixed(6)}, {position[1].toFixed(6)}</p>
                    {apiResult.ilha && <p><strong>Ilha:</strong> {apiResult.ilha}</p>}
                    {apiResult.cidade && <p><strong>Cidade:</strong> {apiResult.cidade}</p>}
                  </>
                )}
                {apiResult.message && <p>{apiResult.message}</p>}
              </div>
            )}

            {apiError && (
              <div className="alert alert-danger">
                {apiError}
              </div>
            )}
          </div>
        </div>
      </div>

      <Footer />
    </div>
  );
}

export default Pluscodes;