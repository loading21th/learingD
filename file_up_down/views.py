# coding:utf-8

from django.shortcuts import render 
from django.http import HttpResponse
from django.http import FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
#from django.http import StreamingHttpResponse
# Create your views here.

from .forms import courseware_form 
from .models import courseware_db 
import os 
import json

@csrf_exempt
def hlsroompage(request,schoolname,classname):
    print "no"
    if request.method == 'POST':
        file_obj = request.FILES.getlist('filename')[0]
        if file_obj:
            upload_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'uploadfile',schoolname,classname)
            if not os.path.exists(upload_path):
                os.makedirs(upload_path)
            with open(os.path.join(upload_path,file_obj.name), 'wb') as newfile:
                for chunk in file_obj.chunks():
                    newfile.write(chunk)
	    hlsdic = {'Courseware_name':file_obj.name}
	    response = JsonResponse(hlsdic, safe=False)
	    response["Access-Control-Allow-Origin"] = "*"
	    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
	    response["Access-Control-Max-Age"] = "1000"
	    response["Access-Control-Allow-Headers"] = "*"
	    return response
	    """
	    # return JsonResponse(hlsdic)
	    result = str(json.dumps(hlsdic))
	    mm = request.get('jsonpcallback')
	    print mm
	    ll = request.get('jsonpcallback')+'('+result+')'
	    print ll
	    return HttpResponse(ll) 
	    """   
        else:
            return HttpResponse(u'Error')
    else:
        hlsdic = {'schoolname':schoolname,'classname':classname,'num':3,'courseware':'up load your file','Courseware_name':''}
        return render(request,'index.html',hlsdic);


def download(request,schoolname,classname,filename):
    """
    def file_iterator(filename,chunk_size=512):
        basedir = "/home/loading_21th/test_file/"
        with open(basedir+filename) as f:
            while true:
                c = f.read(chunk_size)
                if c:
                    yield c
                else :
                    break 
    response = StreamingHttpResponse(file_iterator(filename))
    """
    print 'begin'
    fullpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'uploadfile',schoolname,classname,filename)
    ffile = open(fullpath)
    response = FileResponse(ffile)
    response['Content-Type'] = "application/octet-stream"
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename.encode('utf-8'))
    print 'ok'
    return response 

def add(request,schoolname,classname,a):
    sum = int(a)+2
    return render(request,'index.html',{'sum':sum})

