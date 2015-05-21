# -*- coidng:utf-8 -*-
__author__ = 'wuzhifan'

from poi_wrapper.exceptions import *
from poi_wrapper.clients import poi_python_client

from .simple import SimpleLocationProbability

class LocationProbabilityCompute(object):

    def __init__(self):
        self._computer = SimpleLocationProbability()

    @property
    def _client(self):
        return poi_python_client.get_client()

    def compute_probability(self, user_trace, dev_key=None, external_user=None):
        if dev_key and external_user:
            places = self._client.places.post(user_trace, dev_key, external_user)
        else:
            places = None

        pois = self._client.pois.post(user_trace)

        self._computer.compute(pois, places)

        return pois