from django.shortcuts import render


def home(requests):
    return render(requests, 'home.html', {'title': 'Home'})


def about(requests):
    return render(requests, 'about.html', {'title': 'about'})
