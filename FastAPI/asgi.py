from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import regions


app = FastAPI()
# implementing sub-id query

origins = [
    "http://localhost",
    "http://localhost:8000",
    "https://nurulbayan.or.id",
    "https://www.nurulbayan.or.id"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/indonesia")
def get_provinces():
    data = regions.Indonesia.get_provinces()
    return data if data else {}


@app.get("/indonesia/{prov}")
def get_regencies(prov: str):
    try:
        data = regions.Indonesia.get_regencies(prov)
        if data:
            return data
        else:
            raise HTTPException(status_code=404, detail='404 Not Found')
    except TypeError:
        raise HTTPException(status_code=400, detail='400 Bad Request')


@app.get("/indonesia/{prov}/{kab}")
def get_districts(prov: str, kab: str):
    try:
        data = regions.Indonesia.get_districts(prov, kab)
        if data:
            return data
        else:
            raise HTTPException(status_code=404, detail='404 Not Found')
    except TypeError:
        raise HTTPException(status_code=400, detail='400 Bad Request')


@app.get("/indonesia/{prov}/{kab}/{kec}")
def get_localities(prov: str, kab: str, kec: str):
    try:
        data = regions.Indonesia.get_localities(prov, kab, kec)
        if data:
            return data
        else:
            raise HTTPException(status_code=404, detail='404 Not Found')
    except TypeError:
        raise HTTPException(status_code=400, detail='400 Bad Request')


@app.get("/indonesia/{prov}/{kab}/{kec}/{kel}")
def get_town(prov: str, kab: str, kec: str, kel: str):
    try:
        data = regions.Indonesia.get_town(prov, kab, kec, kel)
        if data:
            return data
        else:
            raise HTTPException(status_code=404, detail='404 Not Found')
    except TypeError:
        raise HTTPException(status_code=400, detail='400 Bad Request')
