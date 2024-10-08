from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "name": "Ethan",
        "age" : "20"
    }

    return render(request, 'home.html')