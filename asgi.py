from fastapi import FastAPI
from database import Wilayah_Indonesia
from pony.orm import db_session, raw_sql


app = FastAPI()
# implementing sub-id query

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
