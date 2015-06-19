__author__ = 'wzf'

from poi_wrapper.tests.base import TestBase

class TestLocationProb(TestBase):
    def __init__(self):
        super(TestBase, self).__init__()
        self.headers = {"Content-type":"application/json"}

    def testLocationProb(self):
        '''
        params = {
            'dev_key' : 'wzf',
            'external_user' : 'jiusi',
            'user_trace' : [{'timestamp': 1427642632501L, 'location': {'latitude': 39.9874399, '__type': u'GeoPoint', 'longitude': 116.4383235}}]
            }
            '''

        params = {
            "sb":"a",
            "user_trace":[
            {
            "timestamp":1427642632501,
            "objectID":"adadfadfadsf",
            "location":{
            "latitude":39.9874399,
            "type":"GeoPoint",
            "longitude":116.4383235
            }
            },
            {
            "timestamp":1427642632501,
            "objectID":"adadfadfadsf",
            "location":{
            "latitude":39.9874399,
            "type":"GeoPoint",
            "longitude":116.4383235
            }
            },
            {
            "timestamp":1427642632501,
            "objectID":"adadfadfadsf",
            "location":{
            "latitude":39.9874399,
            "type":"GeoPoint",
            "longitude":116.4383235
            }
            },
            {
            "timestamp":1427642632501,
            "objectID":"adadfadfadsf",
            "location":{
            "latitude":39.9874399,
            "type":"GeoPoint",
            "longitude":116.4383235
            }
            },
            {
            "timestamp":1427642632501,
            "objectID":"adadfadfadsf",
            "location":{
            "latitude":39.9874399,
            "type":"GeoPoint",
            "longitude":116.4383235
            }
            },
            {
            "timestamp":1427642632501,
            "objectID":"adadfadfadsf",
            "location":{
            "latitude":39.9874399,
            "type":"GeoPoint",
            "longitude":116.4383235
            }
            },
            {
            "timestamp":1427642632501,
            "objectID":"adadfadfadsf",
            "location":{
            "latitude":39.9874399,
            "type":"GeoPoint",
            "longitude":116.4383235
            }
            },
            {
            "timestamp":1427642632501,
            "objectID":"adadfadfadsf",
            "location":{
            "latitude":39.9874399,
            "type":"GeoPoint",
            "longitude":116.4383235
            }
            },
            {
            "timestamp":1427642632501,
            "objectID":"adadfadfadsf",
            "location":{
            "latitude":39.9874399,
            "type":"GeoPoint",
            "longitude":116.4383235
            }
            },
            {
            "timestamp":1427642632501,
            "objectID":"adadfadfadsf",
            "location":{
            "latitude":39.9874399,
            "type":"GeoPoint",
            "longitude":116.4383235
            }
            },
            {
            "timestamp":1427642632501,
            "objectID":"adadfadfadsf",
            "location":{
            "latitude":39.9874399,
            "type":"GeoPoint",
            "longitude":116.4383235
            }
            },
            {
            "timestamp":1427642632501,
            "objectID":"adadfadfadsf",
            "location":{
            "latitude":39.9874399,
            "type":"GeoPoint",
            "longitude":116.4383235
            }
            },
            {
            "timestamp":1427642632501,
            "objectID":"adadfadfadsf",
            "location":{
            "latitude":39.9874399,
            "type":"GeoPoint",
            "longitude":116.4383235
            }
            },
            {
            "timestamp":1427642632501,
            "objectID":"adadfadfadsf",
            "location":{
            "latitude":39.9874399,
            "type":"GeoPoint",
            "longitude":116.4383235
            }
            },
            {
            "timestamp":1427642632501,
            "objectID":"adadfadfadsf",
            "location":{
            "latitude":39.9874399,
            "type":"GeoPoint",
            "longitude":116.4383235
            }
            },
            {
            "timestamp":1427642632501,
            "objectID":"adadfadfadsf",
            "location":{
            "latitude":39.9874399,
            "type":"GeoPoint",
            "longitude":116.4383235
            }
            },
            {
            "timestamp":1427642632501,
            "objectID":"adadfadfadsf",
            "location":{
            "latitude":39.9874399,
            "type":"GeoPoint",
            "longitude":116.4383235
            }
            },
            {
            "timestamp":1427642632501,
            "objectID":"adadfadfadsf",
            "location":{
            "latitude":39.9874399,
            "type":"GeoPoint",
            "longitude":116.4383235
            }
            },
            {
            "timestamp":1427642632501,
            "objectID":"adadfadfadsf",
            "location":{
            "latitude":39.9874399,
            "type":"GeoPoint",
            "longitude":116.4383235
            }
            },
            {
            "timestamp":1427642632501,
            "objectID":"adadfadfadsf",
            "location":{
            "latitude":39.9874399,
            "type":"GeoPoint",
            "longitude":116.4383235
            }
            },
            {
            "timestamp":1427642632501,
            "objectID":"adadfadfadsf",
            "location":{
            "latitude":39.9874399,
            "type":"GeoPoint",
            "longitude":116.4383235
            }
            },
            {
            "timestamp":1427642632501,
            "objectID":"adadfadfadsf",
            "location":{
            "latitude":39.9874399,
            "type":"GeoPoint",
            "longitude":116.4383235
            }
            },
            {
            "timestamp":1427642632501,
            "objectID":"adadfadfadsf",
            "location":{
            "latitude":39.9874399,
            "__type":"GeoPoint",
            "longitude":116.4383235
            }
            }

        ]
        }

        res = self.testBase(params, 'POST', '/senz/locationprob/', self.headers)

        print res

        #dic = json.loads(res)
        #print json.dumps(dic, encoding='UTF-8', ensure_ascii=False)

if __name__ == '__main__':
    test = TestLocationProb()
    test.testLocationProb()
