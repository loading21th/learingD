# coding:utf-8

from django.shortcuts import render 
from django.http import HttpResponse
from django.http import FileResponse
#from django.http import StreamingHttpResponse
# Create your views here.

from .forms import courseware_form 
from .models import courseware_db 


def upload(request):
    if request.method == 'POST':
        Courseware_Form = courseware_form(request.POST,request.FILES)
        if Courseware_Form.is_valid():
            Courseware_Db  = courseware_db()
            Courseware_Db.content = Courseware_Form.cleaned_data['content']
            Courseware_Db.save()
            return render(request,'index.html',{'coursewareform':Courseware_Form,'courseware_name':Courseware_Db.content.name.split('/',1)[1]})
           # return render(request,'index.html',{'sum':50})
        else:
            return HttpResponse(u"Error")
    else:
        form = courseware_form()
        return render(request,'index.html',{'coursewareform':form,'sum':23,'courseware_name':''})


def download(request,filename):
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
    basedir = "/home/loading_21th/test_file/uploadfile/"
    ffile = open(basedir+filename)
    response = FileResponse(ffile)
    response['Content-Type'] = "application/octet-stream"
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename.encode('utf-8'))

    return response 

def add(request,a):
    sum = int(a)+2
    return render(request,'index.html',{'sum':sum})
