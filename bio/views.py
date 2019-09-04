from django.shortcuts import render


def home(requests):
    return render(requests, 'bio/home.html')


def about(requests):
    return render(requests, 'bio/about.html')
