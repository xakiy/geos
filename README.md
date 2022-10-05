# GEOS

Server API wilayah Indonesia menggunakan
framework FastAPI dan Falcon.

Cakupan wilayah yang ditampilkan sampai pada level kelurahan atau desa yang berupa kode gabungan/agregasi, yang setiap kode tingkatan wilayahnya dipisahkan oleh tanda titik.

Database wilayah diambil dari proyek https://github.com/cahyadsn/wilayah besutan saudara [Cahya DSN](https://github.com/cahyadsn)

---
## Install

Klon reponya dengan perintah `$git clone https://github.com/xakiy/geos`.
Anda bisa menjalankannya sebagai server lokal atau membuat docker image dari masing-masing server.

### Membuat Docker Image
Anda bisa membuat docker image dengan docker atau (yang lebih ringan) podman
dengan perintah
`$docker build -t geos .`
lalu jalankan containernya dengan perintah
`$docker run -d -p 8000:8000 geos`


### Membuat Server Lokal
Siapkan virtualenv, kemudian install requirement yang dibutuhkan dengan perintah `pip install -r requirements.txt` di folder framework yang diinginkan.
Jalankan servernya, untuk FastAPI gunakan uvicorn
`$uvicorn asgi:app --host 0.0.0.0 --port 8000`
untuk Falcon gunakan gunicorn
`$gunicorn wsgi:app --bind 0.0.0.0:8000 --log-file -`

### Endpoint API
Kode suatu wilayah yang dihasilkan merupakan gabungan/agregasi dari kode wilayah daerah itu sendiri dengan wilayah induknya yang dipisahkan oleh tanda titik. Seperti kode kelurahan **31.75.02.100** yang bisa diurutkan sebagai **31** untuk **DKI Jakarta**, **75** untuk **Kota Adm. Jakarta Timur**, **02** mewakili kecamatan **Pulogadung** dan angka **100** untuk kelurahan **Rawamangun**.

Endpoint utama yaitu `http://localhost:8000/indonesia`
akan menampilkan data seluruh propinsi di Indonesia, untuk melihat kabupaten bisa dengan mencantumkan kode propinsi kabupaten tersebut setelahnya yang dipisah `/`, misal
`http://localhost:8000/indonesia/11` akan menampikan semua kabupaten di provinsi **Aceh**, begitu juga selanjutnya untuk menampilkan kecamatan dan kelurahan di bawahnya.

### Memperbarui Data
Untuk membuat ulang `geo.db` berdasarkan data sql ~~terbaru~~ Anda bisa menjalankan script `$python rebuid-db.py` yang sudah disediakan.

**Note**: Karena ada perubahan gaya dump SQL antara yang lama dan yang terbaru, yakni dihilangkannya `backtick` yang mengapit kolom/field di database, `mysql2sqlite` selalu gagal memparse dump data yang terbaru, jadi untuk sementara masih menggunakan database `wilayah_2020.sql`.

---
### Referensi
Database Wilayah: https://github.com/cahyadsn/wilayah \
MySQL to SQLite3 converter: https://github.com/dumblob/mysql2sqlite \
Falcon Framework: https://github.com/falconry/falcon \
FastAPI Framework: https://github.com/tiangolo/fastapi
