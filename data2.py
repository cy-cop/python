#homework
import http.cookiejar,urllib.request
 headers = {
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
}
 cookie = http.cookiejar.MozillaCookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
url = 'http://www.baidu.com'
 request = urllib.request.Request(url,headers=headers)
 response = opener.open(request)

 for item in cookie:
    print(item.name,item.value)


 #保存cookie，保存到本地
 filename = 'Joker.txt'
 cookie.save(filename=filename,ignore_discard=True,ignore_expires=True)

cookie = http.cookiejar.MozillaCookieJar()
cookie.load('Joker.txt')
 print(cookie)

#homework2

url = 'http://www.baidu.com'
proxy_handle = {
    'http':'http://120.27.210.60','http://113.120.33.10'
}
proxy = urllib.request.Proxyhandler(proxy_handle)
opener = urllib.request.build_opener(proxy)
response = opener.open(url)
print(response.status)
for url in urls:
    if response.status == 200:
        print(更换代理)