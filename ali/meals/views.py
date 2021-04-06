from django.shortcuts import render
from .models import Food

# Create your views here.

def index(request):

    dest1 = Food()
    dest1.name = 'Delecious Salad'
    dest1.desc = 'Loads Of Vitamins'
    dest1.img = '01.jpg'
    dest1.price = 20

    dest2 = Food()
    dest2.name = 'Pizza'
    dest2.desc = 'Tasty'
    dest2.img = '02.jpg'
    dest2.price = 25

    dest3 = Food()
    dest3.name = 'Momos'
    dest3.desc = 'Cispy'
    dest3.img = '03.jpg'
    dest3.price = 30

    dest4 = Food()
    dest4.name = 'Curry'
    dest4.desc = 'Tasty And Crispy'
    dest4.img = '04.jpg'
    dest4.price = 35

    dests = [dest1,dest2,dest3,dest4]
    return render(request, "index.html",{'dests':dests})