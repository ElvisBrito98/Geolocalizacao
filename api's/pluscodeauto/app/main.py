#apenas terra firme
""" from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from openlocationcode import openlocationcode as olc
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

router = APIRouter()
geolocator = Nominatim(user_agent="pluscode_api")

@router.get("/pluscode")
def get_plus_code(lat: float = Query(...), lng: float = Query(...)):
    try:
        location = geolocator.reverse((lat, lng), exactly_one=True, timeout=10)

        # Se não retornar localização
        if location is None:
            return JSONResponse(content={"message": "Endereço indisponível: coordenadas no mar"}, status_code=404)

        # Verificamos se tem elementos como aldeia, cidade, estrada, edifício etc.
        address = location.raw.get('address', {})
        if not any(key in address for key in ['road', 'residential', 'house', 'village', 'town', 'city', 'hamlet']):
            return JSONResponse(content={"message": "Endereço indisponível: coordenadas fora de terra firme"}, status_code=404)

        # Está em terra → retorna o código
        plus_code = olc.encode(lat, lng)
        return JSONResponse(content={"plus_code": plus_code})

    except GeocoderTimedOut:
        return JSONResponse(content={"error": "Erro de timeout ao verificar localização"}, status_code=504)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)
 """

#Terra firme, aguas nacionais e aguas internacionais
""" from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from openlocationcode import openlocationcode as olc
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

router = APIRouter()
geolocator = Nominatim(user_agent="pluscode_api")

@router.get("/pluscode")
def get_plus_code(lat: float = Query(...), lng: float = Query(...)):
    try:
        location = geolocator.reverse((lat, lng), exactly_one=True, timeout=10)

        if location is None:
            return JSONResponse(content={"message": "Coordenadas inválidas ou não reconhecidas"}, status_code=404)

        address = location.raw.get('address', {})

        # 🌍 Caso 1: Terra firme (tem estrada, vila, cidade, etc.)
        if any(key in address for key in ['road', 'residential', 'house', 'village', 'town', 'city', 'hamlet']):
            plus_code = olc.encode(lat, lng)
            return JSONResponse(content={"plus_code": plus_code})

        # 🌊 Caso 2: Mar sob jurisdição de um país
        elif 'country' in address:
            return JSONResponse(content={
                "message": f"Coordenadas em águas territoriais de {address['country']}"
            }, status_code=200)

        # 🌐 Caso 3: Águas internacionais (sem país)
        else:
            return JSONResponse(content={
                "message": "Coordenadas em águas internacionais"
            }, status_code=200)

    except GeocoderTimedOut:
        return JSONResponse(content={"error": "Erro de timeout ao verificar localização"}, status_code=504)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)
 """


#Cabo verde ou endereço invalido
""" from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from openlocationcode import openlocationcode as olc
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

router = APIRouter()
geolocator = Nominatim(user_agent="pluscode_api")

@router.get("/pluscode")
def get_plus_code(lat: float = Query(...), lng: float = Query(...)):
    try:
        location = geolocator.reverse((lat, lng), exactly_one=True, timeout=10)

        if location is None:
            return JSONResponse(content={"message": "Endereço inválido"}, status_code=404)

        address = location.raw.get('address', {})
        country = address.get('country')

        # Verifica se é Cabo Verde
        if country == "Cabo Verde":
            # Verifica se é terra firme (cidade, vila, estrada, etc.)
            if any(key in address for key in ['road', 'residential', 'house', 'village', 'town', 'city', 'hamlet']):
                plus_code = olc.encode(lat, lng)
                return JSONResponse(content={"plus_code": plus_code})
            else:
                return JSONResponse(content={"message": "Coordenadas em águas de Cabo Verde"}, status_code=200)
        else:
            return JSONResponse(content={"message": "Endereço inválido"}, status_code=404)

    except GeocoderTimedOut:
        return JSONResponse(content={"error": "Erro de timeout ao verificar localização"}, status_code=504)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)
"""

#sem retornar ilhas
 
from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from openlocationcode import openlocationcode as olc
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

router = APIRouter()
geolocator = Nominatim(user_agent="pluscode_api")

@router.get("/pluscode")
def get_plus_code(lat: float = Query(...), lng: float = Query(...)):
    try:
        location = geolocator.reverse((lat, lng), exactly_one=True, timeout=10)

        if location is None:
            return JSONResponse(content={"message": "Endereço inválido"}, status_code=404)

        address = location.raw.get('address', {})
        country = address.get('country')

        # Verifica se é Cabo Verde
        if country == "Cabo Verde":
            # Extrai informações adicionais
            ilha = address.get('state')  # normalmente a ilha vem como "state"
            cidade = address.get('city') or address.get('town') or address.get('village')
            localidade = address.get('neighbourhood') or address.get('suburb') or address.get('road') or address.get('hamlet')

            # Verifica se é terra firme (cidade, vila, estrada, etc.)
            if any(key in address for key in ['road', 'residential', 'house', 'village', 'town', 'city', 'hamlet']):
                plus_code = olc.encode(lat, lng)
                return JSONResponse(content={
                    "plus_code": plus_code,
                    "ilha": ilha,
                    "cidade": cidade,
                    "localidade": localidade
                })
            else:
                return JSONResponse(content={
                    "message": "Coordenadas em águas de Cabo Verde",
                    "ilha": ilha,
                    "cidade": cidade,
                    "localidade": localidade
                }, status_code=200)
        else:
            return JSONResponse(content={"message": "Endereço inválido"}, status_code=404)

    except GeocoderTimedOut:
        return JSONResponse(content={"error": "Erro de timeout ao verificar localização"}, status_code=504)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)
