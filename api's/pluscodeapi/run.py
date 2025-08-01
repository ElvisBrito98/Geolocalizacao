#uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
#http://localhost:5000/localizar?code=849VCWC8%2BR9

from app.main import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)


