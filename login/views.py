from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth.decorators import login_required

#registration
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from login.forms import SignUpForm


# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating
@login_required(login_url="login/")
def home(request):
    template="dash.html"
    u = request.user
    context={
        'u':u,
        }
    
    return render(request,template,context)
	
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
