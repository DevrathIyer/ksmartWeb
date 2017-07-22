from django.shortcuts import render,redirect
from tracker.models import User,Goal,SubGoal
import requests
import os
# Create your views here.
def home(request):
    return render(request, 'tracker/Home.html', {})

def signup(request):
    return render(request, 'tracker/NewUser.html', {})

def viewuserdata(request):
    id_token = request.POST.get('TokenID')
    #request.session['TokenID'] = id_token
    GoogleID = "734656398511-bvq0eii3pavpasv7lj8359u6s6n41gvg.apps.googleusercontent.com"
    url = "https://www.googleapis.com/oauth2/v3/tokeninfo?id_token="+id_token
    response = requests.get(url)
    try:
        if (response.json()['iss'] in ('accounts.google.com', 'https://accounts.google.com')) and (response.json()['aud'] == GoogleID):
            #response['auth'] = os.environ['password']
            userid = response.json()['sub']
            return render(request, 'tracker/signedin.html', {})
    except:
        return redirect('Home')

def newuser(request):
    id_token = request.POST.get('TokenID')
    Phone = request.POST.get('PhoneNumber')
    Cname = request.POST.get('CName')
    City = request.POST.get('City')
    #request.session['TokenID'] = id_token
    GoogleID = "734656398511-bvq0eii3pavpasv7lj8359u6s6n41gvg.apps.googleusercontent.com"
    url = "https://www.googleapis.com/oauth2/v3/tokeninfo?id_token="+id_token
    response = requests.get(url)
    try:
        if (response.json()['iss'] in ('accounts.google.com', 'https://accounts.google.com')) and (response.json()['aud'] == GoogleID):
            #response['auth'] = os.environ['password']
            userid = response.json()['sub']
            if(response.json()['email_verified'] == "true"):
                email = response.json()['email']
            Pname = response.json()['name']
            PicURL = response.json()['picture']
            u = User(Pname = Pname ,Cname = Cname, City = City, UID = userid, Email = email, PicUrl = PicURL, PhoneNumber = Phone)
            return render(request, 'tracker/signedin.html', {})
    except:
        return redirect('home')