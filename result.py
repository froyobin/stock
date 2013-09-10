#encoding=utf-8
import urllib2
import sys
from django.http import HttpResponseRedirect
from django.http import HttpResponse
def addcode(request):
	codevalue=request.POST.get("codeadd",None)
	html = "<html><body>It is now %s.</body></html>" % codevalue
	values =  urllib2.urlopen('http://hq.sinajs.cn/list=sh601006').read()
   	arr = values.split(',')
	b=arr[0].index('"')
	name=arr[0][b+1:len(arr[0])]
	name = name.decode('gb18030').encode('utf-8')
	return HttpResponse(name)
    	#return HttpResponseRedirect("/list/")
	
