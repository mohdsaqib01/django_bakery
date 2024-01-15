from django.shortcuts import render
from inventory.models import Collection
def home(request):
    return render(request, 'home.html', context={'collections':Collection.objects.all()[:4]})

    #about func  about.html

    #contact func   
