from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from rest_framework.authtoken.models import Token

# ---------------------
# Token Authentication
# ---------------------
def token_login(request):
    context = {}

    if request.method == "POST":

        # Get the username and password from the form
        username = request.POST.get("username")
        password = request.POST.get("password")

        # verify credentials
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Create a token for the user
            token, created = Token.objects.get_or_create(user=user)

            # To pass to the template
            context = {
                "username": username,
                "token": token.key,
                "message": f"Success! Logged in succesfully as {username}",
            }
        else:
            context = {"error": "Invalid credentials"}

    return render(request, "token_login.html", context)


def token_register(request):
    context = {}

    if request.method == "POST":

        # Create form instance with submitted data
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Create a token for the new user
            token = Token.objects.create(user=user)
            context = {
                "username": user.username,
                "token": token.key,
                "message": "Success! User created",
            }
        else:
            context = {"form": form}

    else:
        form = UserCreationForm()
        context = {"form": form}

    return render(request, "token_register.html", context)


# ---------------------
# Session Authentication
# ---------------------
def session_login(request):
    context = {}

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Django's session login
            context = {"message": f"Success! Logged in as {username}"}
        else:
            context = {"error": "Invalid credentials"}

    return render(request, "session_login.html", context)


def session_register(request):
    context = {}

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # Creates a new User object in the database
            login(request, user)
            context = {
                "message": f"Registration succesful! Logged in as {user.username}"
            }
        else:
            context = {"form": form}

    else:
        form = UserCreationForm()
        context = {"form": form}

    return render(request, "session_register.html", context)
