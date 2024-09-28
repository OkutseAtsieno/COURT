
from django.urls import path
from . import views
from django.views.generic import TemplateView 

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    path('base_view/', views.base_view, name='base'), 
    # Portfolio page
    path('folio/', views.portfolio, name='portfolio'),

    # Court calendar
    path('calendar/', views.court_calendar, name='court_calendar'),

    # Custom user management
    path('custom_user/', views.custom_user_list, name='custom_user_list'),  
    path('custom_user/<int:id>/', views.custom_user_detail, name='custom_user_detail'), 

    # Advocate management
    path('advocates/', views.advocate_list, name='advocate_list'),  
    path('advocates/<int:id>/', views.advocate_detail, name='advocate_detail'), 

    
    # Teams page with slider
    path('team/', views.team, name='team'),

    path('client/', views.client_view, name='client'),
    path('advocate/', views.advocate_view, name='advocate'),
    path('clerk/', views.clerk_view, name='clerk'),

    # User registration and login
    path('register/', views.register_user, name='register_user'),  
    path('success/', TemplateView.as_view(template_name='success.html'), name='success_page'),  

    # Logout
    path('logout/', views.user_logout, name='user_logout'),
]
