from django.shortcuts import render
import requests
import os
# Create your views here.
def home(request):
    return render(request, 'tracker/Home.html', {})

def viewuserdata(request):
    id_token = request.POST.get('TokenID')
    request.session['TokenID'] = id_token
    GoogleID = "867858739826-0j8s1vplsccuqcha9tng77pmrpc49mam.apps.googleusercontent.com"
    url = "https://www.googleapis.com/oauth2/v3/tokeninfo?id_token="+id_token
    response = requests.get(url)
    try:
        if (response.json()['iss'] in ('accounts.google.com', 'https://accounts.google.com')) and (response.json()['aud'] == GoogleID):
            #response['auth'] = os.environ['password']
            userid = response.json()['sub']
            post_data = {'auth': os.environ['password'], 'uid': userid}
            return render(request, 'tracker/Projects.html', {'Projects': ProjectList,'UserName':UserName})