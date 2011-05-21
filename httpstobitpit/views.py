import urllib

from httpstobitpit import app
from flask import Flask, render_template, make_response, request, abort 

# views
@app.route('/bitcoin/work')
def work():
    '''Formats a URL based on client_id and hash_rate, ignoring them if they
    have no value. Then returns the result of that URL as a JSON object.'''
    
    url = 'http://api.bitp.it/work?'
    
    client_id = request.args.get('client_id', '')
    hash_rate = request.args.get('hash_rate', '')
    params = [client_id, hash_rate]
    
    for param in params:
        url += param + '=' + params[params.index(param)] + '&';
    
    response = make_response(urllib.urlopen(url).read())
    response.content_type = 'application/json'
    return response

@app.route('/bitcoin/mine')
def mine():
    '''Returns an iframe whose source is based on `client_id`.'''
    
    client_id = request.args.get('client_id', '')
    
    return render_template(
            'iframe.html', 
            client_id=client_id,
            )
