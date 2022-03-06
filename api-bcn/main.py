from fastapi import FastAPI
from routers import persona

app = FastAPI()
app.include_router(persona.router)


@app.get("/")
async def root():
    return {"message":"Bienvenido a mi API"}

#lanzar la API en la terminal: uvicorn main:app
#lanzar y que se puede modificar: uvicorn main:app --reload
#primero los endpoints fijos y después parametrizados por niveles
