from falcon import API
from database import Wilayah_Indonesia
from pony.orm import db_session, raw_sql


app = application = API()
# implemented in Falcon Framework

class Indonesia():
    @db_session
    def on_get(self, req, resp):
        # print('indo')
        kode = "__"
        wil = Wilayah_Indonesia.select(lambda w: raw_sql('kode like "' + kode + '"'))
        if len(wil) > 0:
            resp.media = {
                "jumlah": len(wil),
                "data": [{"id": w.kode, "nama": w.nama} for w in wil]
            }


class Provinsi():
    @db_session
    def on_get(self, req, resp, prov, **params):
        # print('prov ', prov)
        if prov and len(prov) == 2:
            kode = prov + '___'
        wil = Wilayah_Indonesia.select(lambda w: raw_sql('kode like "' + kode + '"'))
        if len(wil) > 0:
            resp.media = {
                "jumlah": len(wil),
                "data": [{"id": w.kode, "nama": w.nama} for w in wil]
            }


class Kabupaten():
    @db_session
    def on_get(self, req, resp, prov, kab, **params):
        # print('prov ', prov)
        # print('kab ', kab)
        kode = ""
        if prov and len(prov) == 2:
            if kab and len(kab) == 2:
                kode = prov + '.' + kab + '___'
        wil = Wilayah_Indonesia.select(lambda w: raw_sql('kode like "' + kode + '"'))
        if len(wil) > 0:
            resp.media = {
                "jumlah": len(wil),
                "data": [{"id": w.kode, "nama": w.nama} for w in wil]
            }


class Kecamatan():
    @db_session
    def on_get(self, req, resp, prov, kab, kec, **params):
        # print('prov ', prov)
        # print('kab ', kab)
        # print('kec ', kec)
        kode = "__"
        if prov and len(prov) == 2:
            if kab and len(kab) == 2:
                if kec and len(kec) == 2:
                    kode = prov + '.' + kab + '.' + kec + '_____'
        wil = Wilayah_Indonesia.select(lambda w: raw_sql('kode like "' + kode + '"'))
        if len(wil) > 0:
            resp.media = {
                "jumlah": len(wil),
                "data": [{"id": w.kode, "nama": w.nama} for w in wil]
            }


app.add_route('/indonesia', Indonesia())
app.add_route('/indonesia/{prov}', Provinsi())
app.add_route('/indonesia/{prov}/{kab}', Kabupaten())
app.add_route('/indonesia/{prov}/{kab}/{kec}', Kecamatan())
