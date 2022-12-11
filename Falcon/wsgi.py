from falcon import App, HTTPBadRequest, HTTPNotFound
import regions


# implemented in Falcon Framework
app = application = App()

# strip any trailing slash in request params
app.req_options.strip_url_path_trailing_slash = True


class Indonesia():
    def on_get(self, req, resp):
        data = regions.Indonesia.get_provinces()
        if data:
            resp.media = data
        else:
            raise HTTPNotFound()


class Provinsi():
    def on_get(self, req, resp, prov):
        try:
            data = regions.Indonesia.get_regencies(prov)
            if data:
                resp.media = data
            else:
                raise HTTPNotFound()
        except TypeError:
            raise HTTPBadRequest()


class Kabupaten():
    def on_get(self, req, resp, prov, kab):
        try:
            data = regions.Indonesia.get_districts(prov, kab)
            if data:
                resp.media = data
            else:
                raise HTTPNotFound()
        except TypeError:
            raise HTTPBadRequest()


class Kecamatan():
    def on_get(self, req, resp, prov, kab, kec):
        try:
            data = regions.Indonesia.get_localities(prov, kab, kec)
            if data:
                resp.media = data
            else:
                raise HTTPNotFound()
        except TypeError:
            raise HTTPBadRequest()


class Kelurahan():
    def on_get(self, req, resp, prov, kab, kec, kel):
        try:
            data = regions.Indonesia.get_town(prov, kab, kec, kel)
            if data:
                resp.media = data
            else:
                raise HTTPNotFound()
        except TypeError:
            raise HTTPBadRequest()


app.add_route('/indonesia', Indonesia())
app.add_route('/indonesia/{prov}', Provinsi())
app.add_route('/indonesia/{prov}/{kab}', Kabupaten())
app.add_route('/indonesia/{prov}/{kab}/{kec}', Kecamatan())
app.add_route('/indonesia/{prov}/{kab}/{kec}/{kel}', Kelurahan())
