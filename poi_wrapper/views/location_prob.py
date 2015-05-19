# -*- encoding=utf-8 -*-
__author__ = 'wuzhifan'


import logging
import json

from django.views.decorators.csrf import csrf_exempt

from poi_wrapper.views.base import django_view

from poi_wrapper.location_prob.base import LocationProbabilityCompute
from poi_wrapper.exceptions import *
LOG = logging.getLogger(__name__)

@csrf_exempt
@django_view('POST')
def location_prob(request):

    print 'pre location prob'

    body_context = json.loads(request.body)

    user_trace = body_context.get('user_trace')
    if not user_trace:
        raise BadRequest(msg='Missing user trace.')

    dev_key = body_context.get('dev_key')
    external_user = body_context.get('external_user')

    computer = LocationProbabilityCompute()
    res = computer.compute_probability(user_trace, dev_key, external_user)

    return res