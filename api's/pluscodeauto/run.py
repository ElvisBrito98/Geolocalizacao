#uvicorn run:app --reload
#http://localhost:8000/api/pluscode?lat=14.916973&lng=-23.507579
 #uvicorn run:app --reload --port 8000



from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.main import router

app = FastAPI()

# Configuração CORS crítica
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # URL do seu frontend React
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")  # Prefixo opcional para versionamento

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Acessível em toda a rede