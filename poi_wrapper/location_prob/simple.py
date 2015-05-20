# -*- coidng:utf-8 -*-
__author__ = 'wuzhifan'

import time
import datetime

from abc import *

from poi_wrapper.exceptions import *

DEFAULT_POI_MAPPING= {
    'dining' : [
        'chinese_restaurant', 'japan_korea_restaurant', 'western_restaurant', 'bbq', 'chafing_dish', 'seafood', 'vegetarian_diet', 'muslim', 'buffet', 'dessert', 'cooler', 'snack_bar',
    ],
    'shopping' : [
        'comprehensive_market', 'convenience_store', 'supermarket', 'digital_store', 'pet_market', 'furniture_store', 'farmers_market', 'commodity_market', 'flea_market', 'sports_store', 'clothing_store', 'video_store', 'glass_store', 'mother_store', 'jewelry_store', 'cosmetics_store', 'gift_store', 'photography_store', 'pawnshop', 'antique_store', 'bike_store', 'cigarette_store', 'stationer',
    ],
    'life_service' : [
        'travel_agency', 'ticket_agent', 'post_office', 'telecom_offices', 'newstand', 'water_supply_office', 'electricity_office', 'photographic_studio', 'laundry', 'talent_market', 'lottery_station', 'housekeeping', 'intermediary', 'pet_service', 'salvage_station', 'welfare_house', 'barbershop',
    ],
    'entertainment' : [
        'bath_sauna', 'ktv', 'bar', 'coffee', 'night_club', 'cinema', 'odeum', 'resort', 'outdoor', 'game_room', 'internet_bar',
    ],
    'auto_related' : [
        'gas_station', 'parking_plot', 'auto_sale', 'auto_repair', 'motorcycle', 'car_maintenance', 'car_wash',
    ],
    'healthcare' : [
        'hospital', 'clinic', 'emergency_center', 'drugstore',
    ],
    'hotel' : [
        'motel', 'hotel', 'economy_hotel', 'guest_house', 'hostel',
    ],
    'scenic_spot' : [
    ],
    'exhibition' : [
        'museum', 'exhibition_hall', 'science_museum', 'library', 'gallery', 'convention_center',
    ],
    'education' : [
        'university', 'high_school', 'primary_school', 'kinder_garten', 'training_institutions', 'technical_school', 'adult_education',
    ],
    'finance' : [
        'bank', 'atm', 'insurance_company', 'security_company',
    ],
    'infrastructure' : [
        'traffic', 'public_utilities', 'toll_station', 'other_infrastructure',
    ],
    'estate' : [
        'residence', 'business_building'
    ],
}

def get_poi_mapping():
    ''' get poi mapping.

    this may be refactored to get mapping dynamic
    '''
    return DEFAULT_POI_MAPPING


class LocationProbability(object):
    '''Abstract location probability class.

    '''
    __metaclass__ = ABCMeta

    @abstractmethod
    def compute(self, trace, places=None):

        raise NotImplemented(functionName='compute')

SIMPLE_TIME_PROBABILITY = {
    'midnight' : {
        'hour_range' : [0, 1, 2, 3, 4, 5],
        'probability' : {'dining': {'weekday' : 0.005, 'rest_day' : 0.01},
                        'shopping': 0.001,
                        'life_service': 0.001,
                        'entertainment': {'weekday' : 0.005, 'rest_day' : 0.01},
                        'auto_related': 0.001,
                        'healthcare': 0.001,
                         'hotel': {'weekday' : 0.02, 'rest_day' : 0.03},
                         'scenic_spot': 0.001,
                         'exhibition' : 0.001,
                         'education': 0.001,
                         'finance': 0.001,
                         'infrastructure' : 0.005,
                         'estate' : 0.07},
    },
    'morning' : {
        'hour_range' : [6, 7, 8, 9, 10, 11],
        'probability' : {'dining': {'weekday' : 0.001, 'rest_day' : 0.02},
                        'shopping': {'weekday' : 0.001, 'rest_day' : 0.02},
                        'life_service': {'weekday' : 0.001, 'rest_day' : 0.02},
                        'entertainment': {'weekday' : 0.001, 'rest_day' : 0.02},
                        'auto_related': 0.001,
                        'healthcare': {'weekday' : 0.001, 'rest_day' : 0.01},
                         'hotel': {'weekday' : 0.001, 'rest_day' : 0.01},
                         'scenic_spot': {'weekday' : 0.001, 'rest_day' : 0.02},
                         'exhibition' : {'weekday' : 0.001, 'rest_day' : 0.01},
                         'education': {'weekday' : 0.03, 'rest_day' : 0.005},
                         'finance': 0.001,
                         'infrastructure' : 0.001,
                         'estate' : {'weekday' : 0.07, 'rest_day' : 0.03},},
    },
    'noon' : {
        'hour_range' : [12, 13,],
        'probability' : {'dining': 0.05,
                        'shopping': {'weekday' : 0.001, 'rest_day' : 0.01},
                        'life_service': {'weekday' : 0.001, 'rest_day' : 0.01},
                        'entertainment': {'weekday' : 0.001, 'rest_day' : 0.01},
                        'auto_related': 0.001,
                        'healthcare': 0.001,
                         'hotel': {'weekday' : 0.001, 'rest_day' : 0.01},
                         'scenic_spot': {'weekday' : 0.001, 'rest_day' : 0.01},
                         'exhibition' : {'weekday' : 0.001, 'rest_day' : 0.01},
                         'education': {'weekday' : 0.03, 'rest_day' : 0.005},
                         'finance': 0.001,
                         'infrastructure' : 0.001,
                         'estate' : 0.02,},
    },
    'afternoon' : {
        'hour_range' : [14, 15, 16, 17],
        'probability' : {'dining': 0.01,
                        'shopping': {'weekday' : 0.001, 'rest_day' : 0.04},
                        'life_service': {'weekday' : 0.001, 'rest_day' : 0.02},
                        'entertainment': {'weekday' : 0.001, 'rest_day' : 0.04},
                        'auto_related': 0.001,
                        'healthcare': {'weekday' : 0.001, 'rest_day' : 0.01},
                         'hotel': {'weekday' : 0.001, 'rest_day' : 0.005},
                         'scenic_spot': {'weekday' : 0.001, 'rest_day' : 0.02},
                         'exhibition' : {'weekday' : 0.001, 'rest_day' : 0.01},
                         'education': {'weekday' : 0.03, 'rest_day' : 0.005},
                         'finance': 0.001,
                         'infrastructure' : 0.001,
                         'estate' : {'weekday' : 0.07, 'rest_day' : 0.04},},
    },
    'super_time' : {
        'hour_range' : [18, 19, ],
        'probability' : {'dining': 0.05,
                        'shopping': {'weekday' : 0.001, 'rest_day' : 0.01},
                        'life_service': {'weekday' : 0.001, 'rest_day' : 0.01},
                        'entertainment': {'weekday' : 0.001, 'rest_day' : 0.01},
                        'auto_related': 0.001,
                        'healthcare': {'weekday' : 0.001, 'rest_day' : 0.01},
                         'hotel': {'weekday' : 0.001, 'rest_day' : 0.005},
                         'scenic_spot': {'weekday' : 0.001, 'rest_day' : 0.005},
                         'exhibition' : 0.001,
                         'education': {'weekday' : 0.03, 'rest_day' : 0.005},
                         'finance': 0.001,
                         'infrastructure' : 0.001,
                         'estate' : 0.03,},
    },
    'night' : {
        'hour_range' : [20, 21, 22, 23],
        'probability' : {'dining': 0.01,
                        'shopping': {'weekday' : 0.01, 'rest_day' : 0.03},
                        'life_service': {'weekday' : 0.001, 'rest_day' : 0.01},
                        'entertainment': {'weekday' : 0.001, 'rest_day' : 0.03},
                        'auto_related': 0.001,
                        'healthcare': {'weekday' : 0.001, 'rest_day' : 0.01},
                         'hotel': {'weekday' : 0.001, 'rest_day' : 0.03},
                         'scenic_spot': 0.001,
                         'exhibition' : 0.001,
                         'education': {'weekday' : 0.03, 'rest_day' : 0.005},
                         'finance': 0.001,
                         'infrastructure' : 0.001,
                         'estate' : 0.06,},
    },

}

class SimpleLocationProbability(LocationProbability):

    def __init__(self):
        self.poi_type_mapping = get_poi_mapping()

    def _get_mapping_type(self, poi_l2_type):
            '''get top level mapping type
            '''
            if poi_l2_type is None:
                return None

            for t_name in self.poi_type_mapping:
                if poi_l2_type in self.poi_type_mapping[t_name] or poi_l2_type == t_name:
                    return t_name

    def _prob_from_time(self, poi):
        timestamp = poi.get('timestamp', None)

        if not timestamp:
            return

        date_t = datetime.datetime.fromtimestamp(timestamp / 1000)
        weekday = date_t.weekday()

        time_hour = time.localtime(timestamp / 1000).tm_hour

        for p in poi['pois']:
            poi_l2_type = poi['type'].get('mapping_type', None)
            mapping_l1_type = self._get_mapping_type(poi_l2_type)

            for time_range in SIMPLE_TIME_PROBABILITY:
                if time_hour in SIMPLE_TIME_PROBABILITY[time_range]['hour_range']:
                    whole_prob = SIMPLE_TIME_PROBABILITY[time_range]['probability']

            if mapping_l1_type and mapping_l1_type in whole_prob:
                if isinstance(whole_prob[mapping_l1_type], dict):
                    if weekday in [0, 6]:
                        probablity = whole_prob[mapping_l1_type]['rest_day']
                    else:
                        probablity = whole_prob[mapping_l1_type]['weekday']
                else:
                    probablity = whole_prob[mapping_l1_type]

                #print poi['poi_probability']

                #print mapping_type

                #if

                poi['poi_probability'][mapping_l1_type][poi_l2_type] += probablity

    def _prob_from_poi_quantity(self, poi):
        statistics = {}
        sum = 0

        for p in poi['pois']:
            mapping_type = self._get_mapping_type(p)
            statistics[mapping_type] = statistics[mapping_type] + 1 if statistics[mapping_type] else 1
            sum += 1

        for t in statistics:
            poi['poi_probability'][t] += float(statistics[t]) / sum * 0.1

    def _prob_from_poi_distance(self, poi):
        for p in poi['pois']:
            #geopoint locate inside poi if distance is 0
            probability = 1.0 / p['_distance'] if p['_distance'] > 0 else 1.0

            poi_l2_type = poi['type'].get('mapping_type', None)
            mapping_l1_type = self._get_mapping_type(poi_l2_type)

            print 'type %s' % mapping_l1_type
            print 'dis prob %s ' % probability

            if mapping_l1_type is not None:
                poi['poi_probability'][mapping_l1_type][poi_l2_type] += probability
            else:
                poi['poi_probability']['unknown']['sum_probability'] += probability


    def _home_office_prob(self, poi, places=None):
        if places is None:
            return




    def compute(self, trace, places=None):

        base_prob = {}

        for p in DEFAULT_POI_MAPPING:
            base_prob[p] = {}
            base_prob[p]['sum_probability'] = 0.0001
            for p_l2 in DEFAULT_POI_MAPPING[p]:
                base_prob[p][p_l2] = 0.0001

        for p in ['home', 'office', 'unknown']:
            base_prob[p]['sum_probability'] = 0.0001

        for t in trace:
            pois = t.get('pois', None)

            if not pois:
                continue

            #t['poi_probability'] = {}
            #for p in DEFAULT_POI_MAPPING:
            #   t['poi_probability'][p] = 0.0001

            #t['poi_probability']['unknown'] = 0.0001

            t['poi_probability'] = dict(base_prob)
            self._prob_from_time(t)
            #self._prob_from_poi_quantity(t)
            self._prob_from_poi_distance(t)
            self._home_office_prob(t, places)

        return trace
