from django.http import HttpResponse
from django.template import loader
from .models import Members

def members(request):
  # fetching data from the database
  mymembers = Members.objects.all().values()
  # loads the template
  template = loader.get_template('all_members.html')
  # pass data
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


def details(request, id):
  mymember = Members.objects.get(id = id)
  template = loader.get_template('details.html')
  context = {
    'mymembers': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('test.html')
  # mydata = Members.objects.all().values()
  mydata = Members.objects.filter(firstname__startswith = 'A' )
  context = {
    'mydata': mydata,
  }

  return HttpResponse(template.render(context, request))