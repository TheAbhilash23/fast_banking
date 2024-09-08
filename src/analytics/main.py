from fastapi import FastAPI
from authentication.routes import router as users_router

app = FastAPI()

# Include the routers from different packages
app.include_router(users_router, prefix="/users")
# app.include_router(items_router, prefix="/items")

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}
