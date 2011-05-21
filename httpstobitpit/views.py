import urllib

from httpstobitpit import app
from flask import Flask, render_template, make_response, request, abort 

@app.route('/bitcoin/work')
def work():
    '''Formats a URL using `client_id` and `hash_rate` as args, ignoring them 
    if they have no value. Then fetches the formated URL, reads the result, and
    formats that as a reponse. Reponse content_type is set to JSON. Finally we
    return the response.
    '''
    
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
    '''Renders an iframe for use with bitp.it.js.'''
    
    return render_template('iframe.html')
