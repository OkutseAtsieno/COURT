
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from .models import CourtEvent, CustomUser, Advocate, Case
from .forms import AdvocateForm,UserRegistrationForm,ProfileForm
from django.db import models

# Home view
def home(request):
    return render(request, 'home.html')

def base_view(request):
    return render(request, 'base.html')

# Portfolio view
def portfolio(request):
    return render(request, 'portfolio.html')

# Court calendar view
def court_calendar(request):
    events = CourtEvent.objects.all().order_by('date', 'time')
    return render(request, 'calendar/court_calendar.html', {'events': events})


def team(request):
    users = CustomUser.objects.all()
    advocates = Advocate.objects.all()

    # Initialize the forms
    user_form = UserRegistrationForm()
    profile_form = ProfileForm()

    # Pass the forms to the template context
    return render(request, 'team.html', {
        'users': users,
        'advocates': advocates,
        'user_form': user_form,
        'profile_form': profile_form
    })


# List all users
def custom_user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'custom_user_list.html', {'users': users})

# Detail view for a single user
def custom_user_detail(request, id):
    user = get_object_or_404(CustomUser, id=id)
    return render(request, 'custom_user_detail.html', {'user': user})

# List all advocates
def advocate_list(request):
    advocates = Advocate.objects.all()
    return render(request, 'advocate_list.html', {'advocates': advocates})

# Detail view for a single advocate
def advocate_detail(request, id):
    advocate = get_object_or_404(Advocate, id=id)
    cases = Case.objects.filter(advocate=advocate)
    
    if request.method == 'POST':
        advocate_form = AdvocateForm(request.POST, instance=advocate)
        if advocate_form.is_valid():
            advocate_form.save()
            return redirect('advocate_detail', id=advocate.id)
    else:
        advocate_form = AdvocateForm(instance=advocate)
    
    context = {
        'advocate': advocate,
        'cases': cases,
        'advocate_form': advocate_form,
    }
    
    return render(request, 'advocate_detail.html', context)





# Advocate login view
def advocate_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.role == 'admin':  # Ensure only advocates can log in
            login(request, user)
            return redirect('advocate_dashboard')
    return render(request, 'advocate_login.html')

# Advocate dashboard view
def advocate_dashboard(request):
    if not request.user.is_authenticated or request.user.role != 'admin':
        return redirect('home')
    
    advocate = get_object_or_404(Advocate, user=request.user)
    cases = Case.objects.filter(advocate=advocate)
    
    context = {
        'advocate': advocate,
        'cases': cases,
        'case_count': cases.count(),
    }
    return render(request, 'advocate_dashboard.html', context)

def register_user(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # Automatically log in the user after registration
            login(request, user)

            return redirect('success_page')  # Redirect to a success page or dashboard

    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()

    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})

def client_view(request):
    return render(request, 'client.html')

def advocate_view(request):
    return render(request, 'advocate.html')

def clerk_view(request):
    return render(request, 'clerk.html')



# Logout view
def user_logout(request):
    logout(request)
    return redirect('home')
