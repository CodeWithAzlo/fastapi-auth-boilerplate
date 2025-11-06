from fastapi import FastAPI
from app.db import database
from app.models import models
from app.routes import user, auth

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="FastAPI Auth Boilerplate")

app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "FastAPI Boilerplate is running!"}
