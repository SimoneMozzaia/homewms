import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import homepage, item
from backend.services.database import Base, engine

app = FastAPI()

origins = [
    'http://localhost:3000'
]

Base.metadata.create_all(bind=engine)
app.add_middleware(CORSMiddleware, allow_origins=origins)
app.include_router(homepage.router)
app.include_router(item.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

