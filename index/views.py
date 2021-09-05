from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Contact,Dummy,Solution
from django.contrib import messages
import bs4 
import requests

def index(request):
    return render(request,'index/index.html')


@login_required
def learn(request):
    if request.method == 'POST':
        goal=request.POST.get('goal')
        domain=request.POST.get('domain')
        interest=request.POST.get('interest')
        time=request.POST.get('time')
        pricing=request.POST.get('pricing')
        user=request.user
        entryy=Dummy(goal=goal,domain=domain,interest=interest,time=time,pricing=pricing,user=user)
        entryy.save()
        return render(request,'index/solution.html')
    return render(request,'index/getstarted.html')


@login_required
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        leader=request.POST.get('leader')
        details=request.POST.get('details')
        link=request.POST.get('link')
        user=request.user
        print(details)
        entry=Contact(name=name,leader=leader,details=details,link=link,user=user)
        print(details)
        entry.save()
        messages.success(request,'Request Sent!')
        return render(request,'index/index.html')
    return render(request,'index/contact.html')

def communities(request):
    qset= Contact.objects.all()
    return render(request,'index/communities.html',{'qset':qset})



@login_required
def solution(request):
    qset2=Solution.objects.all()
    return render(request,'index/solution.html',{'qset2':qset2})

@login_required
def paginated_solution(request,slug):
    qset3=Solution.objects.filter(slug=slug)
    return render(request,'index/paginated.html',{'qset3':qset3})
