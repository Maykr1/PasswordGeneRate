from django.shortcuts import render
from .forms import InsultForm
from .models import Password, Insult
import random
import string

password_criteria = ["4 characters", "1 uppercase letter", "1 lowercase letter", "1 number", "1 special character (!, @, $, etc.)"]

# Create your views here.
def home(request):
    context = {
        "name": "Home"
    }

    return render(request, 'PasswordGeneRateApp/home.html', context)

def generator(request):
    characters = string.ascii_letters + string.digits + string.punctuation

    random_string = ""

    while True:
        random_string = ''.join(random.choice(characters) for _ in range(random.randint(4, 16)))
        
        # Check if the string meets the requirements
        if (any(c.isupper() for c in random_string) and
            any(c.islower() for c in random_string) and
            any(c.isdigit() for c in random_string) and
            any(c in string.punctuation for c in random_string)):
                break
    context = {
        "criteria": password_criteria,
        "password": random_string
    }

    return render(request, 'PasswordGeneRateApp/generator.html', context)

def insultor(request):
    insult = None
    if request.method == 'POST':
        form = InsultForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if Password.objects.filter(password = password).exists():
                insult = random.choice(Insult.objects.all()).insult
            else:
                insult = "Good password!"
    else:
        form = InsultForm()
    return render(request, 'PasswordGeneRateApp/insultor.html', {'form': form, 'insult': insult})

def privacy(request):
    return render(request, "PasswordGeneRateApp/privacy.html")
#update each time a new html is made