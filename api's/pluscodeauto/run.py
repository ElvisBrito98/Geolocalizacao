#uvicorn run:app --reload
#http://127.0.0.1:8000/pluscode?lat=14.933&lng=-23.513




from fastapi import FastAPI
from app.main import router

app = FastAPI()
app.include_router(router)

