from django.shortcuts import render

# Create your views here.
def index(request):
    contdict = {'info':'hello world','fig':100}
    return render(request,'basicapp/index.html',contdict)

def new(request):
    return render(request, 'basicapp/new.html')

def relative(request):
    return render(request, 'basicapp/relative.html')
