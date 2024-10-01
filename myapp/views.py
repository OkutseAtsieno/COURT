
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import CourtEvent, CustomUser, Advocate, Case
from .forms import AdvocateForm, UserRegistrationForm, ProfileForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


# Home and Base Views
def home(request):
    return render(request, 'Home.html')

def base_view(request):
    return render(request, 'base.html')

# Portfolio View
def portfolio(request):
    return render(request, 'portfolio.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'myapp/login.html')

# Court Calendar View
def court_calendar(request):
    events = CourtEvent.objects.all().order_by('date', 'time')
    return render(request, 'calendar/court_calendar.html', {'events': events})

# Team View
def team(request):
    users = CustomUser.objects.all()
    advocates = Advocate.objects.all()

    # Initialize the forms
    user_form = UserRegistrationForm()
    profile_form = ProfileForm()

    return render(request, 'team.html', {
        'users': users,
        'advocates': advocates,
        'user_form': user_form,
        'profile_form': profile_form
    })

# User Views
def custom_user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'custom_user_list.html', {'users': users})

def custom_user_detail(request, id):
    user = get_object_or_404(CustomUser, id=id)
    return render(request, 'custom_user_detail.html', {'user': user})

# Advocate Views
def advocate_list(request):
    advocates = Advocate.objects.all()
    return render(request, 'advocate_list.html', {'advocates': advocates})

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

# Advocate Login View
def advocate_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.role == 'admin':  # Ensure only advocates can log in
            login(request, user)
            return redirect('advocate_dashboard')
    return render(request, 'advocate_login.html')

# Advocate Dashboard View
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

# User Registration View
def register_user(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)  # Automatically log in the user
            return redirect('success_page')

    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()

    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})


def advocate_register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'advocate.html', {'error_message': "Passwords do not match."})

        try:
            user = CustomUser.objects.create_user(username=email, email=email, password=password)
            user.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')  
        except Exception as e:
            messages.error(request, "Error during registration: " + str(e))
            return render( 'advocate.html', {'error_message': str(e)})

    return redirect( 'login')  

# Client View
def client_view(request):
    return render(request, 'client.html')

# Clerk View
def clerk_view(request):
    return render(request, 'clerk.html')

# About View
def about(request):
    return render(request='about.html')



def advocate_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'advocate.html')

        try:
            User = get_user_model()
            user = User.objects.create_user(username=email, email=email, password=password)
            advocate = Advocate(user=user, email=email)
            advocate.save()

            messages.success(request, "Registration successful!")
            return redirect('success_page')

        except Exception as e:
            messages.error(request, f"Error during registration: {str(e)}")
            return render(request, 'advocate.html', {'error_message': str(e)})

    return render(request, 'advocate.html')

# Logout View
def user_logout(request):
    logout(request)
    return redirect('home')

def Advocate_login(request):
    if request.method=='POST':
        Fname=request.POST.get('Fname')
        Lname=request.POST.get('Lname')
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=Fname
        myuser.last_name=Lname
        myuser.save

        messages.success(request,"account created succesfully")
        return redirect('login')
    
   
    

   
        
        
        
        

    pass
