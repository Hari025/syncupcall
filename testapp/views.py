from django.shortcuts import render
from testapp.models import Truecomp
import datetime
# Create your views here.
def homeview(request):
    return render(request,'testapp/index.html')
def homeview1(request):
    truecomp=Truecomp.objects.all().order_by('-id')[0:4]
    date=datetime.datetime.now()
    return render(request,'testapp/submit.html',{'truecomp':truecomp,'date':date})

def createpost(request):
        if request.method == 'POST':
            if request.POST.get('TC') and request.POST.get('title') and request.POST.get('date') and request.POST.get('content') and request.POST.get('attendees') :
                post=Truecomp()
                post.TC=request.POST.get('TC')
                post.title= request.POST.get('title')
                post.date= request.POST.get('date')
                post.content= request.POST.get('content')
                post.attendees= request.POST.get('attendees')
                post.save()

                return render(request, 'testapp/index.html')
        else:
                return render(request,'testapp/truecomp.html')
def createpost1(request):
        if request.method == 'POST':
            if request.POST.get('TC') and request.POST.get('title') and request.POST.get('date') and request.POST.get('content') and request.POST.get('attendees') :
                post=Truecomp()
                post.TC=request.POST.get('TC')
                post.title= request.POST.get('title')
                post.date= request.POST.get('date')
                post.content= request.POST.get('content')
                post.attendees= request.POST.get('attendees')
                post.save()

                return render(request, 'testapp/index.html')
        else:
                return render(request,'testapp/smart.html')
def createpost2(request):
        if request.method == 'POST':
            if  request.POST.get('TC')and request.POST.get('title') and request.POST.get('date') and request.POST.get('content') and request.POST.get('attendees') :
                post=Truecomp()
                post.TC=request.POST.get('TC')
                post.title= request.POST.get('title')
                post.date= request.POST.get('date')
                post.content= request.POST.get('content')
                post.attendees= request.POST.get('attendees')
                post.save()

                return render(request, 'testapp/index.html')
        else:
                return render(request,'testapp/PDB.html')
def createpost3(request):
        if request.method == 'POST':
            if request.POST.get('TC') and request.POST.get('title') and request.POST.get('date') and request.POST.get('content') and request.POST.get('attendees') :
                post=Truecomp()
                post.TC=request.POST.get('TC')
                post.title= request.POST.get('title')
                post.date= request.POST.get('date')
                post.content= request.POST.get('content')
                post.attendees= request.POST.get('attendees')
                post.save()

                return render(request, 'testapp/index.html')
        else:
                return render(request,'testapp/Dms.html')

