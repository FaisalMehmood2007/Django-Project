#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member

def testing(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'greeting': 1,
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
# Create your views here.
# def members(request):
#    template = loader.get_template('myfirst.html')
#    return HttpResponse(template.render())


def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


def master(request):
  template = loader.get_template('master.html')
  return HttpResponse(template.render())

# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'fruits': ['Apple', 'Banana', 'Cherry'],   
#   }
#   return HttpResponse(template.render(context, request))

# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'firstname': 'Faisal',
#   }
#   return HttpResponse(template.render(context, request))

# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'cars': [
#       {
#         'brand': 'Ford',
#         'model': 'Mustang',
#         'year': '1964',
#       },
#       {
#         'brand': 'Ford',
#         'model': 'Bronco',
#         'year': '1970',
#       },
#       {
#         'brand': 'Volvo',
#         'model': 'P1800',
#         'year': '1964',
#       }]
#     }
#   return HttpResponse(template.render(context, request)) 