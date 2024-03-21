from django.shortcuts import render
from catsandstudents.models import Cat, Student


def index(request):
    context_dict = {}
    context_dict = {'students': Student.objects.order_by('last_name')}
    return render(request, 'catsandstudents/index.html', context=context_dict)


def about(request):
    context_dict = {}
    context_dict = {'cats': Cat.objects.order_by('name_of_cat')}
    return render(request, 'catsandstudents/about.html', context=context_dict)
