__author__ = 'wzf'

import json
import httplib
import logging

from poi_wrapper.exceptions import *


LOG = logging.getLogger(__name__)

POI_HOST = "120.27.30.239:9222"

TEST_HOST = "127.0.0.1:8088"

class SimpleHttpClient(object):
    def __init__(self):
        pass

    def request(self, params, method, url, headers):
        self.conn = httplib.HTTPConnection(POI_HOST)
        self.conn.request(method, url,
                          json.JSONEncoder().encode(params),
                          headers)

        print "json.JSONEncoder().encode(params)   ", \
                              json.JSONEncoder().encode(params)


        respon = self.conn.getresponse()

        if respon.status >= 400:
            LOG.error('request %s error : %s' %(url, respon.reason))
            raise SenzExcption(msg='request %s error : %s' %(url, respon.reason))

        data = respon.read()
        self.conn.close()
        return data

    def _post(self, url, **kwargs):
        for p in kwargs.keys():
            if kwargs[p] is None:
                del kwargs[p]

        params = kwargs

        headers = {}

        return self.request(params, 'POST', url, headers)

POI_PARSE_URL = '/senz/pois/'

POI_PLACES_URL = '/senz/places/'

class Pois(SimpleHttpClient):
    def _get_url(self):
        return POI_PARSE_URL

    def post(self, locations, poi_type=None):
        res = self._post(self._get_url(), locations=locations, poi_type=poi_type)

        return json.loads(res)['results']['parse_poi']

class Places(SimpleHttpClient):
    def _get_url(self):
        return POI_PLACES_URL

    def post(self, user_trace, dev_key, external_user):
        res = self._post(self._get_url(), user_trace=user_trace, dev_key=dev_key, external_user=external_user)

        return json.loads(res)['results']['place_recognition']

class PoiClient(object):
    def __init__(self):
        self.pois = Pois()
        self.places = Places()

def get_client():
    return PoiClient()

if __name__ == '__main__':
    c = SimpleHttpClient()
    params = {
            'dev_key' : 'wzf',
            'external_user' : 'jiusi',
            'user_trace' : [{'timestamp': 1427642632501L, 'location': {'latitude': 39.9874399, '__type': u'GeoPoint', 'longitude': 116.4383235}}]
            }
    print c._post(POI_PLACES_URL, **params)