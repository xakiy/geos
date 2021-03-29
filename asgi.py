from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Wilayah_Indonesia
from pony.orm import db_session, raw_sql


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
@db_session
def getIndonesia():
    kode = "__"
    wil = Wilayah_Indonesia.select(lambda w: raw_sql('kode like "' + kode + '"'))
    if len(wil) > 0:
        return {
            "jumlah": len(wil),
            "data": [{"id": w.kode, "nama": w.nama} for w in wil]
        }


@app.get("/indonesia/{prov}")
@db_session
def getIndonesiaProv(prov: str):
    if prov and len(prov) == 2:
        kode = prov + '___'
    wil = Wilayah_Indonesia.select(lambda w: raw_sql('kode like "' + kode + '"'))
    if len(wil) > 0:
        return {
            "jumlah": len(wil),
            "data": [{"id": w.kode, "nama": w.nama} for w in wil]
        }


@app.get("/indonesia/{prov}/{kab}")
@db_session
def getIndonesiaKab(prov: str, kab: str):
    kode = ""
    if prov and len(prov) == 2:
        if kab and len(kab) == 2:
            kode = prov + '.' + kab + '___'
    wil = Wilayah_Indonesia.select(lambda w: raw_sql('kode like "' + kode + '"'))
    if len(wil) > 0:
        return {
            "jumlah": len(wil),
            "data": [{"id": w.kode, "nama": w.nama} for w in wil]
        }


@app.get("/indonesia/{prov}/{kab}/{kec}")
@db_session
def getIndonesiaKec(prov: str, kab: str, kec: str):
    kode = "__"
    if prov and len(prov) == 2:
        if kab and len(kab) == 2:
            if kec and len(kec) == 2:
                kode = prov + '.' + kab + '.' + kec + '_____'
    wil = Wilayah_Indonesia.select(lambda w: raw_sql('kode like "' + kode + '"'))
    if len(wil) > 0:
        return {
            "jumlah": len(wil),
            "data": [{"id": w.kode, "nama": w.nama} for w in wil]
        }
