from django.shortcuts import render,HttpResponse
from staff.models import hrdata
# Create your views here.
def index(request):
    if request.method=='POST':
        data=hrdata.objects.all()
        username=request.POST.get('un')
        password=request.POST.get('pw')
        for i in data:
            if i.username==username and i.password==password:
                return render(request,'index.html',{'data':data})
    else:
        return render(request,'index.html')
def hrlogin(request):
    if request.method=='POST':
        data=hrdata.objects.all()
        username=request.POST.get('un')
        password=request.POST.get('pw')
        sts=False
        for i in data:
            if i.username==username and i.password==password:
                sts=True
                return render(request,'hrlogin.html',{'data':data,'sts':sts})
            
    else:
        return render(request,'hrlogin.html')
def mock(request):
    