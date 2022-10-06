from urllib.request import urlretrieve
import os
import time
import subprocess


"""
Note:
Sejak update database wilayah_2022.sql, format dump SQL yang dipakai telah diubah tidak
lagi spesifik MySQL format dump, tetapi sudah menjadi format universal SQL dump.
Oleh karena itu, SQLite sudah bisa langsung menggunakan format dump tersebut dan
sudah tidak membutuhkan konverter mysql2sqlite lagi.

Tetapi untuk dokumentasi, saya akan tetap menyertakan kode konverternya.
"""

# database_raw_url = 'https://raw.github.com/cahyadsn/wilayah/master/db/wilayah_2020.sql'
database_raw_url = 'https://raw.github.com/cahyadsn/wilayah/master/db/wilayah.sql'
input_db = os.path.basename(database_raw_url)
output_db = 'geo.db'
# mysql2sqlite = './bin/mysql2sqlite'
sqlite = 'sqlite3'
ready = True

# Get the latest database file
print('Mengunduh database di {} ... '.format(database_raw_url), end='')
try:
    urlretrieve(database_raw_url, input_db)
    time.sleep(1)
except Exception:
    print('gagal!')
    print('Pastikan koneksi internetmu lancar jaya!')
else:
    print('berhasil!')

# Checking required files
print('Memeriksa berkas-berkas yang dibutuhkan:')
# print(' - {}\t\t '.format(os.path.basename(mysql2sqlite)), end='')
# if os.path.isfile(mysql2sqlite):
#     print('ada')
# else:
#     print('tidak')
#     ready = False

print(' - {}\t\t '.format(input_db), end='')
if os.path.isfile(input_db):
    print('ada')
else:
    print('tidak')
    ready = False

print(' - {}\t\t '.format(os.path.basename(sqlite)), end='')
if os.path.isfile(subprocess.getoutput('which '+sqlite)):
    print('ada')
else:
    print('tidak')
    print('Pastikan Anda sudah menginstall {} di system Anda.'.format(os.path.basename(sqlite)))
    ready = False

if not ready:
    raise SystemExit('Tidak bisa memproses, ada berkas yang dibutuhkan tidak tersedia!')

try:
    os.remove(output_db)
except Exception:
    pass

print('Memkonversi database ke sqlite format ... ', end='')
try:
    # subprocess.run('{} {} | {} {}'.format(mysql2sqlite, input_db, sqlite, output_db), shell=True)
    subprocess.run('cat {} | {} {}'.format(input_db, sqlite, output_db), shell=True)
except Exception:
    print('gagal!')
else:
    if os.path.isfile(output_db) and os.path.getsize(output_db) > 0:
        print('berhasil!')
    else:
        print('gagal!')

# Fungsi untuk menambahkan backtick di dump SQL
def quote_field(input_file, output_file):
    i = open(input_file, 'r')
    o = open(output_file,'w')
    line = i.readline()
    while line:
        line = re.sub(" wilayah",' "wilayah"', line)
        line = re.sub(" kode ",' "kode" ', line)
        line = re.sub(" nama ",' "nama" ', line)
        line = re.sub("kode, nama", '"kode", "nama"', line)
        o.write(line)
        line = i.readline()
    i.close()
    o.close()
