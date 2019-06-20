url = 'http://www.baidu.com'
proxy_handle = {
     'http':'http://183.51.190.51'
}
proxy = urllib.request.ProxyHandler(proxy_handle)
opener = urllib.request.build_opener(proxy)
response = opener.open(url)
print(response.status)
for url in urls:
    if response.status ==200:
        print(更换)

 
