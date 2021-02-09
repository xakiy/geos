from fastapi import FastAPI
from database import Wilayah_Indonesia
from pony.orm import db_session, raw_sql


app = FastAPI()
# initial fastAPI resource file

@app.get("/provinsi")
@db_session
def getProvinsi():
    wil = Wilayah_Indonesia.select(lambda w: raw_sql('kode like "__"'))
    if len(wil) > 0:
        return {
            "nama": "provinsi",
            "jumlah": len(wil),
            "data": [{"id": w.kode, "nama": w.nama} for w in wil]
        }


@app.get("/kabupaten/{prov}")
@db_session
def getKabupaten(prov: str):
    if len(prov) == 2:
        kab = prov + '___'
        wil = Wilayah_Indonesia.select(lambda w: raw_sql('kode like "' + kab + '"'))
        if len(wil) > 0:
            return {
                "nama": "kabupaten",
                "jumlah": len(wil),
                "data": [{"id": w.kode, "nama": w.nama} for w in wil]
            }
    else:
        print('ouch, 2 digit prov required')


@app.get("/kecamatan/{kab}")
@db_session
def getKecamatan(kab: str):
    if len(kab) == 5:
        kec = kab + '___'
        wil = Wilayah_Indonesia.select(lambda w: raw_sql('kode like "' + kec + '"'))
        if len(wil) > 0:
            return {
                "nama": "kecamatan",
                "jumlah": len(wil),
                "data": [{"id": w.kode, "nama": w.nama} for w in wil]
            }


@app.get("/kelurahan/{kec}")
@db_session
def getKelurahan(kec: str):
    if len(kec) == 8:
        kel = kec + '_____'
        wil = Wilayah_Indonesia.select(lambda w: raw_sql('kode like "' + kel + '"'))
        if len(wil) > 0:
            return {
                "nama": "kelurahan",
                "jumlah": len(wil),
                "data": [{"id": w.kode, "nama": w.nama} for w in wil]
            }
