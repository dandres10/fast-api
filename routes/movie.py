from fastapi import  HTTPException, Path, Query, Request, Depends
from fastapi.responses import  JSONResponse
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials
from pydantic import BaseModel, Field
from typing import Optional
from user_jwt import  validateToken
from bd.database import Session
from models.movie import Movie as ModelMovie
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter

routeMovie = APIRouter()


class BearerJWT(HTTPBearer):
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        auth = await super().__call__(request)
        data = validateToken(auth.credentials)
        if data["email"] != "marlon@gmail.com":
            raise HTTPException(status_code=403, detail="Credenciales invalidas")

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(default="titulo", min_length=3, max_length=60)
    overview: str = Field(default="descripcion", min_length=5, max_length=60)
    year: int = Field(default="2023")
    rating: float = Field(ge=1, le=10)
    category: str = Field(default="categoria", min_length=3, max_length=15)


@routeMovie.get("/movies", tags=["Movie"], dependencies=[Depends(BearerJWT())])
def get_movies():
    db = Session()
    data = db.query(ModelMovie).all()
    return JSONResponse(content=jsonable_encoder(data))


@routeMovie.get("/movies/{id}", tags=["Movie"])
def get_movie(id: int = Path(ge=1, le=100)):
    db = Session()
    data = db.query(ModelMovie).filter(ModelMovie.id == id).first()
    if not data:
        return JSONResponse(
            status_code=404, content={"message": "no se encontraron datos"}
        )
    return JSONResponse(status_code=200, content=jsonable_encoder(data))


@routeMovie.get("/movies/", tags=["Movie"])
def get_movies_by_category(category: str = Query(min_length=3, max_length=15)):
    db = Session()
    data = db.query(ModelMovie).filter(ModelMovie.category == category).all()
    if not data:
        return JSONResponse(
            status_code=404, content={"message": "no se encontraron datos"}
        )
    return JSONResponse(status_code=200, content=jsonable_encoder(data))


@routeMovie.post("/movies", tags=["Movie"], status_code=201)
def create_by_movie(movie: Movie):
    db = Session()
    newMovie = ModelMovie(**movie.model_dump())
    db.add(newMovie)
    db.commit()
    return JSONResponse(content={"message": "se ha cargado una nueva pelicula"})


@routeMovie.put("/movies/{id}", tags=["Movie"])
def update_movie(id: int, movie: Movie):
    db = Session()
    data = db.query(ModelMovie).filter(ModelMovie.id == id).first()
    if not data:
        return JSONResponse(
            status_code=404, content={"message": "no se encontro el recurso"}
        )

    data.title = movie.title
    data.overview = movie.overview
    data.year = movie.year
    data.rating = movie.rating
    data.category = movie.category
    db.commit()
    return JSONResponse(content={"message": "Se ha modificado la pelicula"})


@routeMovie.delete("/movies/{id}", tags=["Movie"])
def delete_movie(id: int):
    db = Session()
    data = db.query(ModelMovie).filter(ModelMovie.id == id).first()
    if not data:
        return JSONResponse(
            status_code=404, content={"message": "no se encontro el recurso"}
        )
    db.delete(data)
    db.commit()
    return JSONResponse(
        content={
            "message": "Se ha eliminado la pelicula",
            "movie": jsonable_encoder(data),
        }
    )