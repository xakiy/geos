from falcon import API, HTTPBadRequest, HTTPNotFound
from database import Wilayah_Indonesia
from pony.orm import db_session, raw_sql


app = application = API()
# implemented in Falcon Framework


def validCode(kode, length=2):
    return kode and kode.isdigit() and len(kode) == length


class Indonesia():
    @db_session
    def on_get(self, req, resp):
        kode = "__"
        wil = Wilayah_Indonesia.select(lambda w: raw_sql('kode like "' + kode + '"'))
        if len(wil) > 0:
            resp.media = {
                "jumlah": len(wil),
                "data": [{"id": w.kode, "nama": w.nama, "tipe": "provinsi"} for w in wil]
            }
        else:
            raise HTTPNotFound()


class Provinsi():
    @db_session
    def on_get(self, req, resp, prov, **params):
        if not validCode(prov):
            raise HTTPBadRequest()

        kode = prov + '___'
        wil = Wilayah_Indonesia.select(lambda w: raw_sql('kode like "' + kode + '"'))
        if len(wil) > 0:
            resp.media = {
                "jumlah": len(wil),
                "data": [{"id": w.kode, "nama": w.nama, "tipe": "kabupaten"} for w in wil]
            }
        else:
            raise HTTPNotFound()


class Kabupaten():
    @db_session
    def on_get(self, req, resp, prov, kab, **params):
        kode = ""
        if not validCode(prov) or not validCode(kab):
            raise HTTPBadRequest()

        kode = prov + '.' + kab + '___'
        wil = Wilayah_Indonesia.select(lambda w: raw_sql('kode like "' + kode + '"'))
        if len(wil) > 0:
            resp.media = {
                "jumlah": len(wil),
                "data": [{"id": w.kode, "nama": w.nama, "tipe": "kecamatan"} for w in wil]
            }
        else:
            raise HTTPNotFound()


class Kecamatan():
    @db_session
    def on_get(self, req, resp, prov, kab, kec, **params):
        kode = "__"
        if not validCode(prov) or not validCode(kab) or not validCode(kec):
            raise HTTPBadRequest()

        kode = prov + '.' + kab + '.' + kec + '_____'
        wil = Wilayah_Indonesia.select(lambda w: raw_sql('kode like "' + kode + '"'))
        if len(wil) > 0:
            resp.media = {
                "jumlah": len(wil),
                "data": [{"id": w.kode, "nama": w.nama, "tipe": "kelurahan"} for w in wil]
            }
        else:
            raise HTTPNotFound()


class Kelurahan():
    @db_session
    def on_get(self, req, resp, prov, kab, kec, kel, **params):
        kode = "__"
        if not validCode(prov) or not validCode(kab) or not validCode(kec) or \
                not validCode(kel, 4):
            raise HTTPBadRequest()

        kode = prov + '.' + kab + '.' + kec + '.' + kel
        wil = Wilayah_Indonesia.select(lambda w: raw_sql('kode like "' + kode + '"'))
        if len(wil) > 0:
            resp.media = {
                "jumlah": len(wil),
                "data": [{"id": w.kode, "nama": w.nama, "tipe": "kelurahan"} for w in wil]
            }
        else:
            raise HTTPNotFound()


app.add_route('/indonesia', Indonesia())
app.add_route('/indonesia/{prov}', Provinsi())
app.add_route('/indonesia/{prov}/{kab}', Kabupaten())
app.add_route('/indonesia/{prov}/{kab}/{kec}', Kecamatan())
app.add_route('/indonesia/{prov}/{kab}/{kec}/{kel}', Kelurahan())
