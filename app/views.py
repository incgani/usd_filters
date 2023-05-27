from django.shortcuts import render

# Create your views here.
def userdefined(request):
    d={'data':'The Name Is KhAn Name'}
    return render(request,'userdefined.html',d)
