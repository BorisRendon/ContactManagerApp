import request
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import urllib.request

#prueba fase 6

#POST
url = 'http://demo7862839.mockable.io/contacts?gid=100 '
post_fields = {}
request = Request(url,urlencode(post_fields).encode())
json = urlopen(request).read().decode()
print(json)
#GET


params = {"name": "arg1",
          "lastname": "arg2",
          "Phone": "arg3"
}
querystring = urllib.parse.urlencode(params)
url = url + "?" + querystring
with urllib.request.urlopen("http://demo7862839.mockable.io/contacts?gid=100") as response:
    response_txt = response.read()
    print(response_txt)
