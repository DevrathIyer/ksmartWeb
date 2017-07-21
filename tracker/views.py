from django.shortcuts import render,redirect
import requests
import os
# Create your views here.
def home(request):
    return render(request, 'tracker/Home.html', {})

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
    id_token = request.POST.get('Cname')
    request.session['TokenID'] = id_token
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
            Pname = response.json()['name']
            return render(request, 'tracker/signedin.html', {})
    except:
        return redirect('home')