import urllib

from httpstobitpit import app
from flask import Flask, make_response, request, abort 

API_URL = 'http://api.bitp.it/work?'

# views
@app.route('/work')
def index():
    '''Wrapper for bitp.it API'''
    
    client_id = request.args.get('client_id', '')
    hash_rate = request.args.get('hash_rate', '')
    assert client_id and hash_rate or abort(400)
    
    params = \
            'client_id={0}'.format(client_id) \
            + '&' + \
            'hash_rate={0}'.format(hash_rate)
    url = API_URL + params
    
    response = make_response(urllib.urlopen(url).read())
    response.content_type = 'application/json'
    return response
