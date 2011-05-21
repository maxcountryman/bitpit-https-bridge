import urllib

# Flask and friends :)
from flask import Flask, Response, request, abort 

app = Flask(__name__)
app.config.from_pyfile('app.cfg')

API_URL = 'http://api.bitp.it/work?'

# views
@app.route('/work')
def index():
    '''Wrapper for bitp.it API'''
    
    client_id = request.args.get('client_id', '')
    hash_rate = request.args.get('hash_rate', '')
    assert client_id and hash_rate
    
    params = \
            'client_id={0}'.format(client_id) \
            + '&' + \
            'hash_rate={0}'.format(hash_rate)
    url = API_URL + params
    
    print(url)
    response = urllib.urlopen(url).read()
    Response.content_type = 'application/json'
    return Response(response)

if __name__ == '__main__':
    app.run()
