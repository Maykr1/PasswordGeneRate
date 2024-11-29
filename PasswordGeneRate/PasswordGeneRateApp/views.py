from django.shortcuts import render
from .forms import InsultForm
from .models import Password, Insult
import random
import string
import re
import sys
try:
    import Levenshtein
except ImportError as e:
    print(f"Import error (probably Levenshtein): {e}")

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
    
def check_pw_db(password: str, threshold=0.9) -> bool:
    """
    Checks if given *password* is (nearly) equal to any in the Password database.
    """
    # Levenshtein is used to compare similarity of two strings, or here two passwords.
    if not "Levenshtein" in sys.modules:
        return Password.objects.filter(password = password).exists()
    
    passwords = Password.objects.values_list("password", flat=True).distinct()
    match = False

    for check_pw in passwords.iterator():
        ratio = Levenshtein.ratio(password, check_pw)
        if ratio >= threshold:
            match = True
            break
    
    return match

def insultor(request):
    insult = None
    if request.method == 'POST':
        form = InsultForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']

            if len(password) < 4:
                insult = "Password is too short!"
            elif " " in password:
                insult = "No spaces please!"
            elif check_pw_db(password):
                insult = random.choice(Insult.objects.all()).insult
            elif not bool(re.search(r'[A-Z]', password)):
                insult = "Needs to have at least one uppercase letter"
            elif not bool(re.search(r'[a-z]', password)):
                insult = "Needs to have at least one lowercase letter"
            elif not bool(re.search(r'\d', password)):
                insult  = "Needs to have at least one number"
            elif not bool(re.search(f'[{re.escape(string.punctuation)}]', password)):
                insult = "Needs to have at least one special character"
            else:
                insult = "Good password!"
    else:
        form = InsultForm()
    return render(request, 'PasswordGeneRateApp/insultor.html', {'form': form, 'insult': insult})

def privacy(request):
    return render(request, "PasswordGeneRateApp/privacy.html")
#update each time a new html is made