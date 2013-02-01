 # coding=utf-8
from settings import WAPIKEY
from googleSearch import shortenUrl
import urllib
import json
import httplib2


# Get the best result based on city using wunderground autocomplete
def getBestResult(city):
    query = urllib.urlencode({'query': city})
    apiUrl = 'http://autocomplete.wunderground.com/aq?{0}'.format(query)
    h = httplib2.Http()
    response, content = h.request(apiUrl, 'GET')
    results = json.loads(unicode(content, errors='replace'))
    if response['status'] != '200':
        return 'API returned error code {0}'.format(response['status'])
    elif results['RESULTS'] == []:
        return 'empty'
    else:
        return results['RESULTS'][0]['l']


def weatherLookup(city):
    query = getBestResult(city)
    apiUrl = 'http://api.wunderground.com/api/{0}/conditions{1}.json'.format(
        WAPIKEY, query
    )
    h = httplib2.Http()
    header = {'Accept-Encoding': 'Identity'}
    response, content = h.request(apiUrl, 'GET', headers=header)
    if response['status'] != '200':
        return 'API returned error code {0}'.format(response['status'])
    elif query == 'empty':
        return 'There was a problem with your query.'
    else:
        data = json.loads(content)
        results = data['current_observation']
        return "It's {0} at {1}C which feels like {2}C - More: {3}".format(
            results['weather'], results['temp_c'], results['feelslike_c'],
            shortenUrl(results['ob_url'])
        )
