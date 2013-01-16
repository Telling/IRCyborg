import urllib
import json
import httplib2
import HTMLParser

def imdbSearch(title):
    query = urllib.urlencode({'q': title})
    apiUrl = 'http://www.imdb.com/xml/find?json=1&nr=1&tt=on&{0}'.format(query)
    h = httplib2.Http()
    response, content = h.request(apiUrl, 'GET')
    results = json.loads(content)
    if(response['status'] != '200'):
        return 'API returned error code: {0}'.format(response['status'])
    elif(response['content-length'] == '0'):
        return 'There was a problem with your query.'
    elif('title_popular' not in results):
        return 'I found no popular match for your query.'
    else:
        popResult = results['title_popular'][0]
        imdbUrl = 'http://www.imdb.com/title/{0}/'.format(popResult['id'])
        popTitle = HTMLParser.HTMLParser().unescape(popResult['title'])
        return 'The most popular result is {0} from {1}: {2}'.format(
            popTitle, popResult['title_description'][0:4], imdbUrl
        )
