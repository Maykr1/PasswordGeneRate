from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "name": "Ethan",
        "age" : "20"
    }

    return render(request, 'PasswordGeneRateApp/home.html', context)

def generator(request):
    context = {
        "name": "Bob"
    }

    return render(request, 'PasswordGeneRateApp/generator.html', context)

def insultor(request):
    context = {
        "name": "Jeff"
    }

    return render(request, 'PasswordGeneRateApp/insultor.html', context)
#update each time a new html is made