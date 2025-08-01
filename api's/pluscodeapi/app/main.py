from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware  # Adicione esta linha
from .pluscode_utils import decode_plus_code, generate_google_maps_link

app = FastAPI(title="Plus Code API")

# Configure CORS - ESSENCIAL para comunicação com o frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Mantenha seu frontend React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API a funcionar!"}

@app.get("/localizar")
async def localizar_plus_code(  # Adicione async
    code: str = Query(..., description="Plus Code completo ou curto"),
    ref_lat: float = Query(None, description="Latitude de referência para códigos curtos"),
    ref_lon: float = Query(None, description="Longitude de referência para códigos curtos")
):
    result = decode_plus_code(code, ref_lat, ref_lon)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    
    link = generate_google_maps_link(result["latitude"], result["longitude"])
    return {
        "plus_code": result["plus_code"],
        "latitude": result["latitude"],
        "longitude": result["longitude"],
        "google_maps_link": link,
        "message": "Localização encontrada com sucesso"  # Adicionado para o frontend
    }