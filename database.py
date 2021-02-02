from pony.orm import Database, PrimaryKey, Optional
from pathlib import Path


db = Database()


class Wilayah_Indonesia(db.Entity):
    kode = PrimaryKey(str)
    nama = Optional(str)


db.bind("sqlite", filename=str(Path("./geo.db").absolute()), create_db=False)
db.generate_mapping(create_tables=False)
