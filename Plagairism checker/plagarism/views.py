from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from datetime import datetime
from django.urls import reverse
from plagarism.models import User
from pandas import Series
from passlib.hash import pbkdf2_sha256
# Create your views here.

def CheckPlag(request):
    content = request.POST['mname'].split(" ")
    copy = request.POST['cname'].split(" ")
    same = ""
    #print(copy)
    #print(content)
    content = Series(content)
    copy = Series(copy)
    for i in content:
        s = copy[copy == i]
        try:
            #print(type(s.iloc[0]))
            same += " "+s.iloc[0]
        except IndexError:
            pass
    if(same == ""):
        same = "none"

    return HttpResponse("COMMON CONTENTS :\n"+same)



def Register(request):
    return render(request , 'plagarism/register.html')

def Login(request):
    return render(request,"plagarism/login.html")

def RegisterUser(request):
    username = request.POST['username']
    password = request.POST['userpassword']

    password = pbkdf2_sha256.encrypt(password , rounds = 12000 , salt_size=32)

    s = User(username = username,password = password)
    s.save()
    if s.id:
        return HttpResponseRedirect(reverse('Login'))
    else:
        return HttpResponse("error")

def Check(request):
    if(request .session.has_key('username')):
        del request.session['username']
        return render(request,'plagarism/check.html')
    else:
        return HttpResponseRedirect(reverse('Login'))

def AuthenticateUser(request):
    username = request.POST['username']
    password = request.POST['userpassword']



    #if 'username' not in request.session:
    #    return HttpResponseRedirect(reverse('Register'))

    l = User.objects.filter(username = username)
    passw = l[0].password
    print(password)
    print(passw)
    print(pbkdf2_sha256.verify(password,passw))

    if (pbkdf2_sha256.verify(password , passw)):
        request .session['username'] = username
        return HttpResponseRedirect(reverse('Check'))
    else:
        return HttpResponseRedirect(reverse('Register'))
