from django.shortcuts import render

# Create your views here.
def index(request):
        return render(request,'cities/home.html')
        
def datetime(request):
        if request.POST['cities']=='Delhi':
                return render(request,'cities/date & time.html',{'post':'Delhi'})
        
        elif request.POST['cities']=='Gurgaon':
                return render(request,'cities/date & time.html',{'post':'Gurgaon'})
                
        elif request.POST['cities']=='Bangalore':
                return render(request,'cities/date & time.html',{'post':'Bangalore'})
                
        else:
                return render(request,'cities/home.html')

def arrdep(request):
        return render(request,'cities/arr-dep.html')
        
