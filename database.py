from pony.orm import Database, PrimaryKey, Optional
from pathlib import Path


db = Database()


class Wilayah(db.Entity):
    kode = PrimaryKey(str)
    nama = Optional(str)

db_file = Path(__file__).absolute().parent / 'geo.db'
db.bind("sqlite", filename=str(db_file.absolute()), create_db=False)
db.generate_mapping(create_tables=False)
