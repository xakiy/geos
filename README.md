# GEOS

Server REST API wilayah Indonesia menggunakan framework FastAPI dan Falcon.

Cakupan wilayah yang ditampilkan sampai pada level kelurahan atau desa yang
berupa kode gabungan/agregasi, yang setiap kode tingkatan wilayahnya dipisahkan
oleh tanda titik.

Database wilayah diambil dari proyek https://github.com/cahyadsn/wilayah besutan
saudara [Cahya DSN](https://github.com/cahyadsn)

## Install

Klon reponya dengan `$git clone https://github.com/xakiy/geos`.  
Anda bisa menjalankannya sebagai server lokal atau membuat docker image dari
masing-masing server.

### Membuat Docker Image
Anda bisa membuat container image dengan docker atau yang lebih ringan podman
dengan perintah:  
untuk Falcon  
`$docker build -t geos-falcon -f Falcon/Dockerfile .`  
untuk FastAPI  
`$docker build -t geos-fastapi -f FastAPI/Dockerfile .`  
lalu jalankan containernya dengan perintah:  
`$docker run -d -p 8000:8000 geos`


### Membuat Server Lokal
Siapkan virtualenv dan buat database `geo.db` dengan perintah  
`$python3 rebuild-db.py`  
Jalankan servernya, untuk FastAPI:  
`pip install -r FastAPI/requirements.txt`  
`$gunicorn FastAPI.asgi:app -c FastAPI/gunicorn.conf.py`  
untuk Falcon:  
`pip install -r Falcon/requirements.txt`  
`$gunicorn Falcon.wsgi:app -c Falcon/gunicorn.conf.py`

### Endpoint API
Kode suatu wilayah yang dihasilkan merupakan gabungan/agregasi dari kode wilayah
daerah itu sendiri dengan wilayah induknya yang dipisahkan oleh tanda titik.
Seperti kode kelurahan **31.75.02.100** yang bisa diurutkan sebagai **31**
untuk **DKI Jakarta**, **75** untuk **Kota Adm. Jakarta Timur**, **02** mewakili
kecamatan **Pulogadung** dan angka **100** untuk kelurahan **Rawamangun**.

Endpoint utama yaitu `http://localhost:8000/indonesia`
akan menampilkan data seluruh propinsi di Indonesia, untuk melihat kabupaten bisa
dengan mencantumkan kode propinsi kabupaten tersebut setelahnya yang dipisah `/`,
misal `http://localhost:8000/indonesia/11` akan menampikan semua kabupaten di
provinsi **Aceh**, begitu juga selanjutnya untuk menampilkan kecamatan dan
kelurahan di bawahnya.

### Memperbarui Data
Untuk membuat ulang `geo.db` berdasarkan data sql terbaru Anda bisa menjalankan
script `$python rebuid-db.py` yang sudah disediakan.

**Note**:
Sejak update database wilayah_2022.sql, format dump SQL yang dipakai telah diubah
tidak lagi spesifik MySQL format dump tetapi sudah menjadi format universal SQL dump.
Oleh karena itu, SQLite sudah bisa langsung menggunakan format dump tersebut dan
tidak membutuhkan konverter mysql2sqlite lagi.

---
### Referensi
Database Wilayah: https://github.com/cahyadsn/wilayah  
MySQL to SQLite3 converter: https://github.com/dumblob/mysql2sqlite  
Falcon Framework: https://github.com/falconry/falcon  
FastAPI Framework: https://github.com/tiangolo/fastapi  
