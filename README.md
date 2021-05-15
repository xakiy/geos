# GEOS

Simple Regions of Indonesia API using FastAPI and Falcon Framework,
both on their own branch.

---
## Install

Clone the repo, `$git clone https://github.com/xakiy/geos`.
Either you can build docker from it or run it from your local server.

### Docker build
You can build docker image using docker or podman
`$docker build -t geos .`
And run the container
`$docker run -d -p 8000:8000 geos`

### Local Server Setup
Create your virtualenv.
Install the dependancy packages `pip install -r requirements.txt`
Fire up your server, you can use uvicorn
`$uvicorn asgi:app --host 0.0.0.0 --port 8000`
or gunicorn
`$gunicorn wsgi:app --bind 0.0.0.0:8000 --log-file -`

### Accessing the API
The API endpoint is served in `http://localhost:8000/indonesia`
subsequent regions is accessible as numeric sub-path, first sub-path for
province, second for regencies, and the third for districts.

### Rebuilding the Database
To rebuild the `geo.db` based on newest version of the database source you can
invoke command like `mysql2sqlite wilayah_2020.sql | sqlite3 geo.db` with 
an assumption that you already have the required resources and tools installed,
such as `mysql2sqlite` and `sqlite3`.

---
### Resources
Database source: https://github.com/cahyadsn/wilayah
MySQL to SQLite3 converter: https://github.com/dumblob/mysql2sqlite
