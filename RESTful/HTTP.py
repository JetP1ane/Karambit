from urllib import request, parse
import json


class APIController():

    def __init__(self, BASE):
        self.BASE = BASE

    def http_request(self, url_ext, data):

        try:
            send_data = parse.urlencode(data).encode()
            print("\n=> Connecting to: " + self.BASE + url_ext)  # Show url that we're connecting to

            if data:    # If data exists, include it in request
                req = request.Request(self.BASE + url_ext, data)
            else:
                req = request.Request(self.BASE + url_ext)

            resp = request.urlopen(req)
            return resp.read()

        except Exception as e:
            print(e)

            return False
