#coding=utf-8
from django.shortcuts import render_to_response
from hello.models import stockSnName
import urllib2


def index(request):
    s1 = stockSnName.objects.all()
    address = []
    if True:
	for stock in s1:
	   sn = stock.values
	   querystring='http://hq.sinajs.cn/list='+sn
	   #querystring='http://hq.sinajs.cn/list=sh601001'
	   revalues =  urllib2.urlopen(querystring).read()
	   arr = revalues.split(',')
	   b=arr[0].index('"')
	   name=arr[0][b+1:len(arr[0])]
	   stockname = name.decode('gb18030').encode('utf-8')
	   numbers=str(int(arr[8])/100)
	   money = str(float(arr[9])/10000)
	   tmpdic=dict(id=sn,name=stockname,v3=arr[1],v4=arr[2], \
			   v5=arr[3],v6=arr[4],v7=arr[5],v8=arr[6],v9=arr[7], \
			   v10=numbers,v11=money)
	   address.append(tmpdic)
        return render_to_response('list.html', {'stock': address,'time':arr[-2]})
    else :
        return render_to_response('list.html', {'stock': address})

