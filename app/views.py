from django.shortcuts import render
from .models import RawData, Results, PharmacyData

# Create your views here.
def home(request):
    obj=RawData.objects.values('Specialization').distinct()
    cname=request.POST.get('spec')
    data=cname
    obj1=RawData.objects.values('Consultant').filter(Specialization=cname).distinct()
    #dname=request.POST.get('doc')
    #obj2=res.objects.values('Efficiency').filter(consultant=dname).distinct()
    dname=request.POST.get('doc')
    obj2=Results.objects.all().filter(Consultant=dname)
    #cat=request.POST.get('spec')
    
    return render(request,'home.html',{'obj':obj, 'obj1':obj1, 'obj2':obj2,'doctor':dname,'speciliz':cname,'data':data})


def doctor(request):
    dname=request.POST.get('search')
    obj1=Results.objects.values().filter(Consultant=dname)
    return render (request,'doctor.html',{'dname':dname,'obj1':obj1})


def statistics(request):
    obj=RawData.objects.values('Specialization').distinct()
    cname=request.POST.get('spec')
    char=cname
    obj1=Results.objects.all().filter(Specialization=char).order_by('-Efficiency')[:5] # For descending;


    return render (request, 'statistics.html',{'obj':obj,'speciliz':cname, 'obj1':obj1,'cname':cname})



def pharmacy(request):
    obj=PharmacyData.objects.values('Specialization').distinct()
    cname=request.POST.get('spec')
    obj1=PharmacyData.objects.all().filter(Specialization=cname)

    return render (request, 'pharmacy.html',{'obj':obj, 'obj1':obj1,'cname':cname,'speciliz':cname})