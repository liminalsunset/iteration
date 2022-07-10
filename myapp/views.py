from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
  context = {"name": "Pupcake"}
  template = loader.get_template("app/home.html")
  return HttpResponse(template.render(context))