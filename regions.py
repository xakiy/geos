from database import Wilayah as Wilayah_Indonesia
from pony.orm import db_session, raw_sql


def validateCode(kode, length=2):
    if not (kode and kode.isdigit() and len(kode) == length):
        raise TypeError('Invalid Params: "{}"'.format(kode))


class Indonesia():
    @staticmethod
    @db_session
    def get_provinces():
        wil = Wilayah_Indonesia.select(lambda w: raw_sql('kode like "__"'))
        if len(wil) > 0:
            return {
                "jumlah": len(wil),
                "data": [{"id": w.kode, "nama": w.nama.title(), "tipe": "provinsi"} for w in wil]
            }
        else:
            return False

    @staticmethod
    @db_session
    def get_regencies(prov):
        validateCode(prov)
        kode = prov + '___'
        wil = Wilayah_Indonesia.select(lambda w: raw_sql('kode like "' + kode + '"'))
        if len(wil) > 0:
            return {
                "jumlah": len(wil),
                "data": [{"id": w.kode, "nama": w.nama.title(), "tipe": "kabupaten"} for w in wil]
            }
        else:
            return False

    @staticmethod
    @db_session
    def get_districts(prov, kab):
        validateCode(prov)
        validateCode(kab)
        kode = prov + '.' + kab + '___'
        wil = Wilayah_Indonesia.select(lambda w: raw_sql('kode like "' + kode + '"'))
        if len(wil) > 0:
            return {
                "jumlah": len(wil),
                "data": [{"id": w.kode, "nama": w.nama.title(), "tipe": "kecamatan"} for w in wil]
            }
        else:
            return False

    @staticmethod
    @db_session
    def get_localities(prov, kab, kec):
        validateCode(prov)
        validateCode(kab)
        validateCode(kec)
        kode = prov + '.' + kab + '.' + kec + '_____'
        wil = Wilayah_Indonesia.select(lambda w: raw_sql('kode like "' + kode + '"'))
        if len(wil) > 0:
            return {
                "jumlah": len(wil),
                "data": [{"id": w.kode, "nama": w.nama.title(), "tipe": "kelurahan"} for w in wil]
            }
        else:
            return False

    @staticmethod
    @db_session
    def get_town(prov, kab, kec, kel):
        validateCode(prov)
        validateCode(kab)
        validateCode(kec)
        validateCode(kel, 4)
        kode = prov + '.' + kab + '.' + kec + '.' + kel
        wil = Wilayah_Indonesia.select(lambda w: raw_sql('kode like "' + kode + '"'))
        if len(wil) > 0:
            return {
                "jumlah": len(wil),
                "data": [{"id": w.kode, "nama": w.nama.title(), "tipe": "kelurahan"} for w in wil]
            }
        else:
            return False
