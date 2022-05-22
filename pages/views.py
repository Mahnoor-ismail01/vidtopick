from django.shortcuts import render
from srtgen.models import Srtgen
# Create your views here.
from icecream import ic
def home(request):
    objs = Srtgen.objects.filter(public=True)
    ic(objs)
    return render(request, 'newhome.html', {"home":True, "objs":objs})