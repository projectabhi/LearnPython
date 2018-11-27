from urllib import request, parse

#Base URL being accessed
url = 'http://httpbin.org/get'

#Dictionary of query parameters (if any)
parms = {
    'name1' : 'value1',
    'name2' : 'value2',
}

# Encode the query strings
querystring = parse.urlencode(parms)

# Make a get request and get the response
u = request.urlopen(url+'?'+querystring)
resp = u.read()

print(resp)