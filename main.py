from fastapi import FastAPI
from routers import notifications
import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(notifications.router)

@app.get("/")
def read_root():
    return {"message": "Notification Service is running!"}