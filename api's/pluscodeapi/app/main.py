from fastapi import FastAPI, HTTPException, Query
from .pluscode_utils import decode_plus_code, generate_google_maps_link
import webbrowser

app = FastAPI(title="Plus Code API")

@app.get("/")
def root():
    return {"message": "API a funcionar!"}

@app.get("/localizar")
def localizar_plus_code(
    code: str,
    ref_lat: float = Query(None, description="Latitude de referência para códigos curtos"),
    ref_lon: float = Query(None, description="Longitude de referência para códigos curtos")
):
    result = decode_plus_code(code, ref_lat, ref_lon)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    
    link = generate_google_maps_link(result["latitude"], result["longitude"])
    webbrowser.open_new_tab(link)
    return {
        "plus_code": result["plus_code"],
        "latitude": result["latitude"],
        "longitude": result["longitude"],
        "google_maps_link": link
    }
    