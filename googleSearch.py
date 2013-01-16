from settings import GAPIKEY, GCUSTOMSEARCHID
import urllib
import json
import httplib2

def shortenUrl(url):
    apiUrl = 'https://www.googleapis.com/urlshortener/v1/url?' \
             'key={0}'.format(GAPIKEY)

    headers = {'Content-Type': 'application/json'}
    data = {'longUrl': url}
    h = httplib2.Http()
    headers, response = h.request(apiUrl, 'POST', json.dumps(data), headers)
    result = json.loads(response)
    return result['id']

def googleSearch(searchTerm):
    query = urllib.urlencode({'q': searchTerm})
    apiUrl = 'https://www.googleapis.com/customsearch/v1?g1=dk&key={0}&' \
             'cx={1}&{2}'.format(GAPIKEY, GCUSTOMSEARCHID, query)

    h = httplib2.Http()
    response, content = h.request(apiUrl, 'GET')
    if(response['status'] != '200'):
        return 'API returned error code: {0}'.format(response['status'])
    else:
        results = json.loads(content)
        moreResults = 'https://www.google.com/#hl=da&{0}'.format(query)
        data = results['items']
        searchInfo = results['searchInformation']
        return '{0} - Total results: {1} ({2}s) - More results: {3}'.format(
            data[0]['link'], searchInfo['formattedTotalResults'],
            searchInfo['formattedSearchTime'], shortenUrl(moreResults)
        )
