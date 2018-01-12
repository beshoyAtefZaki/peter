from django.shortcuts import render
from .forms import Itemform
# Create your views here.
def home(request):
    if request.method == 'POST':
        form =Itemform(request.POST,request.FILES)
        #if form.is_valid():
        form.save()
        print("saved")
        return render(request,"home.html")
    else :
       form =Itemform()

       return render (request ,"home.html" , {'form':form })
