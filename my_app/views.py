from django.shortcuts import render
from . import models
import requests
from bs4 import BeautifulSoup

BASE_TGDD_URL = 'https://www.thegioididong.com/tim-kiem?key={}'


# Create your views here.
def home(request):
    return render(request, 'base.html')


def index(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    final_url = BASE_TGDD_URL.format(search)
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_listing = soup.find_all('li', {'class': 'cat42'})
    for post in post_listing:
        post_title = post.find('h3').text
        print(post_title)
    stuff_for_frontend = {
        'search': search
    }
    return render(request, 'my_app/index.html', stuff_for_frontend)
