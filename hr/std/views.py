from django.shortcuts import render,HttpResponse
from django.contrib import messages
from std.models import Details,Credentials
# Create your views here.
def index(request):
    return HttpResponse('This is students home page')
def register(request):
    if request.method=='POST':
        name=request.POST.get('nme')
        pno=request.POST.get('pno')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        pw=request.POST.get('pw')
        cpw=request.POST.get('cpw')
        uns=Credentials.objects.all()
        x=True
        for i in uns:
            if i.username==pno:
                x=False
        if x==True:
            if pw==cpw:
                details=Details(name=name,pno=pno,email=email,gender=gender,dob=dob,mock='')
                details.save()
                credentials=Credentials(username=pno,password=pw)
                credentials.save()
                return render(request,'login.html')
            else:
                return HttpResponse('Password dosent matched')
        else:
            return HttpResponse('Phone number already exist')
    return render(request,'register.html')
def login(request):
    if request.method=='POST':
        data=Credentials.objects.all()
        details=Details.objects.all()
        un=request.POST.get('un')
        pw=request.POST.get('pw')
        user=''
        unv=False
        pwv=False
        for j in details:
            if un==j.pno:
                user=j
        for i in data:
            if i.username==un:
                if i.password==pw:
                    unv=True
                    pwv=True
        if unv==True:
            if pwv==True:
                messages.info(request,'Logged in Successfull')
                return render(request,'login.html',{'user':user})
            else:
                messages.info(request,'invalid Password')
                return render(request,'login.html')
        else:
            messages.info(request,'Invalid username')
            return render(request,'login.html')
    else:
        return render(request,'login.html')
    
    
        