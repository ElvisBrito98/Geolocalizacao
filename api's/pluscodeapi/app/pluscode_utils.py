from openlocationcode import openlocationcode as olc

def decode_plus_code(plus_code: str, reference_lat: float = None, reference_lon: float = None):
    try:
        # Se o código não for completo e houver referência, completa-o
        if not olc.isFull(plus_code):
            if reference_lat is None or reference_lon is None:
                return {"error": "Código curto fornecido. Precisas enviar latitude e longitude de referência."}
            plus_code = olc.recoverNearest(plus_code, reference_lat, reference_lon)
        
        decoded = olc.decode(plus_code)
        return {
            "plus_code": plus_code,
            "latitude": decoded.latitudeCenter,
            "longitude": decoded.longitudeCenter
        }
    except Exception as e:
        return {"error": str(e)}

def generate_google_maps_link(lat: float, lon: float) -> str:
    return f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"