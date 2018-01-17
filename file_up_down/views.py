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
    if request.method == 'POST':
        upload_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'uploadfile',schoolname,classname)
        if not os.path.exists(upload_path):
            os.makedirs(upload_path)
        if request.FILES:
            file_obj = request.FILES.getlist('filename')[0]
            with open(os.path.join(upload_path,file_obj.name), 'wb') as newfile:
                for chunk in file_obj.chunks():
                    newfile.write(chunk)
        hlsdic = {'Courseware_name':os.listdir(upload_path)}
        response = JsonResponse(hlsdic, safe=False)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
    else:
        hlsdic = {'schoolname':schoolname,'classname':classname,'sum':3}
        return render(request,'index.html',hlsdic);


def download(request,schoolname,classname,filename):
    fullpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'uploadfile',schoolname,classname,filename)
    ffile = open(fullpath,'rb')
    response = FileResponse(ffile)
    print(filename)
    response['Content-Type'] = "application/octet-stream"
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename)
    return response 

def add(request,schoolname,classname,a):
    sum = int(a)+2
    return render(request,'index.html',{'sum':sum})

