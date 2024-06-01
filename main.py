from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from bd.database import engine, Base
from routes.movie import routeMovie
from routes.user import routeUser



app = FastAPI(
    title="Curso FastAPI",
    description="Primeros pasos creacion de apis con fastAPI",
    version="0.0.1",
)

app.include_router(routeMovie)
app.include_router(routeUser)

Base.metadata.create_all(bind=engine)


@app.get("/", tags=["Inicio"])
def read_root():
    return HTMLResponse("<h1>Hola mundo!!</h1>")



