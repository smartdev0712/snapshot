from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from api.models import *
import json
from django.views import generic, View
import requests

# Create your views here.
def index(request):
    return redirect('/mountains/')

class searchImage(View):
    template_name = 'index.html'
    
    def get(self, request, *args, **kwargs):
        print("loading...")
        apiKey = '636e1481b4f3c446d26b8eb6ebfe7127'
        query = self.kwargs.get('image')
        url = f'https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key={apiKey}&tags={query}&per_page=24&format=json&nojsoncallback=1'
        response = requests.get(url=url)
        images = response.json()['photos']['photo']
        img_url = []
        for image in images:
            farm = image['farm']
            server = image['server']
            id = image['id']
            secret = image['secret']
            title = image['title']
            img_url.append(f'https://farm{farm}.staticflickr.com/{server}/{id}_{secret}_m.jpg')
        context = {
            'searchData': self.kwargs['image'],
            'images': img_url,
        }
        
        return render(request, self.template_name, context)

def search(request):
    searchData = request.POST['search']
    print(searchData)
    return redirect(f'/{searchData}')