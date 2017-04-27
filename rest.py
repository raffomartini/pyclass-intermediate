'''
A REST API for docfinder
'''

from libs import bottle
import docfinder,json,subprocess

@bottle.route('/')
def index():
    return 'Welcome to Docfinder'

# http://localhost:8080/docfinder/v1/search?q=zip,barry
@bottle.get('/docfinder/v1/search')
def search():
    # this is used to get the query, as we are doing comma separated, then we need to unseparate
    keywords = filter(None, bottle.request.query.get('q', '').split(','))
    # .get() is a best
    # using filter to remove the empty string (was creating bugs on docfinder)
    result = docfinder.search(*keywords)
    bottle.response.content_type = 'application/json'
    return json.dumps(result)

# http://localhost:8080/docfinder/v1/document/pep-3000
@bottle.get('/docfinder/v1/document/<uri>')
def select(uri):
    data = {'uri': uri}
    try:
        text = docfinder.get_document(uri)
    except docfinder.UnknownURI:
        data['status'] = 'error'
        data['content'] = 'UnknownURI'
    else:
        data['status'] = 'OK'
        data['content'] = text
    bottle.response.content_type = 'application/json'
    return json.dumps(data, indent=2)

# http://localhost:8080/docfinder/v1/document/pep-3000
@bottle.post('/docfinder/v1/document/<uri>')
def intert(uri):
    text = bottle.request.POST.get('text', '')
    data = {'uri': uri, 'text':text}
    try:
        docfinder.add_document(uri, text)
    except docfinder.DuplicateURI:
        data['status'] = 'error'
        data['error'] = 'DuplicateURI'
    else:
        data['status'] = 'OK'
    bottle.response.content_type = 'application/json'
    return json.dumps(data, indent=2)

# This adds the capability tosend commands
@bottle.get('/cmd/v1/<command>')
def execute(command):
    argv = command.split()
    try:
        output = subprocess.check_output(argv)
    except Exception as e:
        data = {'status': 'error',
                'error': str(e)}
    else:
        data = {'status': 'OK',
                'output': output}
    return json.dumps(data, indent=2)


if __name__ == '__main__':
    bottle.run(host='localhost', port=8080)