import urllib

from httpstobitpit import app
from flask import Flask, render_template, make_response, request, abort 

# views
@app.route('/bitcoin/work')
def index():
    '''Wrapper for bitp.it API'''
    
    url = 'http://api.bitp.it/work?'
    
    client_id = request.args.get('client_id', '')
    hash_rate = request.args.get('hash_rate', '')
    params = [client_id, hash_rate]
    #assert client_id and hash_rate or abort(400)
    
    for param in params:
        url += param + '=' + params[params.index(param)] + '&';
    
    response = make_response(urllib.urlopen(url).read())
    response.content_type = 'application/json'
    return response

@app.route('/bitcoin/static/mine')
def bitpit():
    client_id = request.args.get('client_id', '')
    hash_rate = request.args.get('hash_rate', '')
    
    print(client_id)
    return render_template(
            'bitpit.html', 
            client_id=client_id,
            hash_rate=hash_rate
            )
