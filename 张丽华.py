#homework1
import urllib.request
import urllib.parse

data = bytes(urllib.parse.urlencode({'wd':'学生'}),encoding='utf8')
print(data)
ur1 = 'http://www.baidu.com'
response = urllib.request.urlopen(ur1)
HTML = response.read().decode('utf8')
print(HTML)

#homework2
var router = new VueRouter({
    routes:[
        {path:'/',
        name:'home',
        component:Home
    },
    {path:'*',
    redirect:'/'
    },
    ]
})

