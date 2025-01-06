from fastapi import FastAPI
from app.api.v1.endpoints import superadmin

app = FastAPI()

# Include routes
app.include_router(superadmin.router, prefix="/api/v1", tags=["SuperAdmin"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Restaurant Assistance API"}
