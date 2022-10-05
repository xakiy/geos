from urllib.request import urlretrieve
import os
import time
import subprocess

database_raw_url = 'https://raw.github.com/cahyadsn/wilayah/master/db/wilayah_2020.sql'
input_db = os.path.basename(database_raw_url)
output_db = 'geo.db'
mysql2sqlite = './bin/mysql2sqlite'
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
print(' - {}\t\t '.format(os.path.basename(mysql2sqlite)), end='')
if os.path.isfile(mysql2sqlite):
    print('ada')
else:
    print('tidak')
    ready = False

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
    subprocess.run('{} {} | {} {}'.format(mysql2sqlite, input_db, sqlite, output_db), shell=True)
except Exception:
    print('gagal!')
else:
    if os.path.isfile(output_db) and os.path.getsize(output_db) > 0:
        print('berhasil!')
    else:
        print('gagal!')
