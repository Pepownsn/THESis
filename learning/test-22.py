# # urllib Module (internet)
# import urllib2
# x = urllib2.urlopen('http://www.google.com')
# print x.read()


import urllib
import urllib2
url = 'https://www.google.com'
values = {'q' : 'python'}
data = urllib.urlencode(values)
# data = data.encode('utf-8')
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page

## PYTHON3
# data = urllib.parse.urlencode(values)
# data = data.encode('utf-8') # data should be bytes
# req = urllib.request.Request(url, data)
# response = urllib.request.urlopen(req)
# the_page = response.read()
# print(the_page)
#
# try:
#     url = 'https://www.google.com/search?q=python'
#     # now, with the below headers, we defined ourselves as a simpleton who is
#     # still using internet explorer.
#     headers = {}
#     headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
#     req = urllib2.Request(url, headers = headers)
#     resp = urllib2.urlopen(req)
#     respData = resp.read()
#
#     saveFile = open('withHeaders.txt','w')
#     saveFile.write(str(respData))
#     saveFile.close()
# except Exception as e:
#     print(str(e))
