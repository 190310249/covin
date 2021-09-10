from django.http import HttpResponse, response
from django.shortcuts import render, redirect
import requests
import json
from django.conf import settings


def oauth2(request):
    url = f'https://login.salesforce.com/services/oauth2/authorize?client_id={settings.CLIENT_ID}&response_type=code&redirect_uri={settings.REDIRECT_URI}'
    return redirect(url)


def oauth2_success(request):
    code = request.GET['code']
    data = {
        'client_id': settings.CLIENT_ID,
        'client_secret': settings.CLIENT_SECRET
    }
    params = {
        'Content-type': 'application/x-www-form-urlencoded',
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': settings.REDIRECT_URI,
    }
    response = requests.post('https://login.salesforce.com/services/oauth2/token', params=params, data=data)
    res = json.loads(response.text)
    access_token = res['access_token']
    return render(request, 'core/success.html', {'access_token': access_token})
