from django.shortcuts import render

password_criteria = ["4 characters", "1 uppercase letter", "1 lowercase letter", "1 number", "1 special character (!, @, $, etc.)"]

# Create your views here.
def home(request):
    context = {
        "name": "Home"
    }

    return render(request, 'PasswordGeneRateApp/home.html', context)

def generator(request):
    context = {
        "name": "Generator",
        "criteria": password_criteria
    }

    return render(request, 'PasswordGeneRateApp/generator.html', context)

def insultor(request):
    context = {
        "name": "Insultor"
    }

    return render(request, 'PasswordGeneRateApp/insultor.html', context)

def privacy(request):
    return render(request, "PasswordGeneRateApp/privacy.html")
#update each time a new html is made