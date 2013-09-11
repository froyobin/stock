#encoding=utf-8
from hello.models import stockSnName
import urllib2
import sys
from django.http import HttpResponseRedirect
from django.http import HttpResponse
def addcode(request):
	codevalue=request.POST.get("codeadd",None)
	mychoice = request.POST.get("choice",None)
	html = "<html><body>It is now %s.</body></html>" % codevalue
	if int(mychoice) == 1:
		querystring='http://hq.sinajs.cn/list=sh'+codevalue
	else :
		querystring='http://hq.sinajs.cn/list=sz'+codevalue
	values =  urllib2.urlopen(querystring).read()
	if len(values)>30:
		#if int(mychoice) ==2:
		#	return HttpResponse(values)
   		arr = values.split(',')
		b=arr[0].index('"')
		name=arr[0][b+1:len(arr[0])]
		stockname = name.decode('gb18030').encode('utf-8')
		if int(mychoice) ==1:
			codevalue = "sh"+codevalue
		else:
			codevalue = "sz"+codevalue

		p1=stockSnName(values=codevalue,name="reserve");
		p1.save()
	#return HttpResponse(name)
    	return HttpResponseRedirect("/list/")
	
def delcode(request):
	codevalue=request.POST.get("codedel",None)
	try:
        	s1 = stockSnName.objects.get(values=codevalue)
	except:
   		return HttpResponseRedirect("/list/")
	s1.delete()
    	return HttpResponseRedirect("/list/")

def szaddcode(request):
	codevalue=request.POST.get("codeadd",None)
	html = "<html><body>It is now %s.</body></html>" % codevalue
	querystring='http://hq.sinajs.cn/list=sh'+codevalue
	values =  urllib2.urlopen(querystring).read()
	if(len(values)>30):
   		arr = values.split(',')
		b=arr[0].index('"')
		name=arr[0][b+1:len(arr[0])]
		stockname = name.decode('gb18030').encode('utf-8')
		codevalue = "sz"+codevalue
		p1=stockSnName(values=codevalue,name="reserve");
		p1.save()
	#return HttpResponse(name)
    	return HttpResponseRedirect("/list/")
