from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from openlocationcode import openlocationcode as olc
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable
import logging

router = APIRouter()
geolocator = Nominatim(user_agent="pluscode_api_cv_v3", timeout=10)

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.get("/pluscode")
def get_plus_code(
    lat: float = Query(..., description="Latitude em graus decimais", example=14.917039),
    lng: float = Query(..., description="Longitude em graus decimais", example=-23.507523)
):
    """
    Endpoint que retorna:
    - Plus Code de 11 caracteres
    - Dados de localização em Cabo Verde
    """
    try:
        # Validação básica das coordenadas
        if not (-90 <= lat <= 90) or not (-180 <= lng <= 180):
            return JSONResponse(
                content={"error": "Coordenadas inválidas"},
                status_code=400
            )

        # Consulta ao serviço de geolocalização
        location = geolocator.reverse((lat, lng), exactly_one=True, language='pt')
        
        if not location:
            logger.warning(f"Localização não encontrada para {lat},{lng}")
            return JSONResponse(
                content={"message": "Localização não encontrada"},
                status_code=404
            )

        address = location.raw.get('address', {})
        country = address.get('country', '').lower()

        # Verifica se é Cabo Verde
        if "cabo verde" not in country:
            return JSONResponse(
                content={"message": "Apenas localizações em Cabo Verde são suportadas"},
                status_code=400
            )

        # Processamento dos dados
        ilha = address.get('state', '')
        cidade = address.get('city') or address.get('town') or address.get('village', '')
        localidade = address.get('road') or address.get('neighbourhood', '')

        # Gera Plus Code com 11 caracteres (padrão Google Maps)
        plus_code = olc.encode(lat, lng, codeLength=11)

        # Determina o tipo de área
        if any(key in address for key in ['road', 'house', 'residential']):
            area_type = "urbana"
        elif any(key in address for key in ['village', 'town', 'city']):
            area_type = "povoado"
        else:
            area_type = "área não especificada"

        return JSONResponse(content={
            "plus_code": plus_code,
            "ilha": ilha,
            "cidade": cidade,
            "localidade": localidade,
            "tipo_area": area_type,
            "coordenadas": {"lat": lat, "lng": lng}
        })

    except GeocoderTimedOut:
        logger.error("Timeout no serviço de geolocalização")
        return JSONResponse(
            content={"error": "Serviço de geolocalização indisponível"},
            status_code=504
        )
    except GeocoderUnavailable:
        logger.error("Serviço de geolocalização offline")
        return JSONResponse(
            content={"error": "Serviço temporariamente indisponível"},
            status_code=503
        )
    except Exception as e:
        logger.error(f"Erro inesperado: {str(e)}")
        return JSONResponse(
            content={"error": "Erro interno no processamento"},
            status_code=500
        )