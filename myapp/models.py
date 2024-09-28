
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils import timezone

class CourtEvent(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} on {self.date} at {self.time}"

class Profile(models.Model):
    USER_ROLES = [
        ('litigant', 'Litigant'),
        ('advocate', 'Advocate'),
        ('staff', 'Court Staff'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=USER_ROLES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('litigant', 'Litigant'),
        ('advocate', 'Advocate'),
        ('staff', 'Court Staff'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    firm = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Change the related_name here
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Change the related_name here
        blank=True
    )

    def __str__(self):
        return f"{self.username} - {self.role}"

class Advocate(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bar_number = models.CharField(max_length=20,default=0)
    specialty = models.CharField(max_length=100,default=True)
    years_of_experience = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=15, blank=True, null=True,default='0000000')
    email = models.EmailField(unique=True,default='example@gmail.com')
    address = models.TextField(blank=True, null=True,default='address not provided')
    firm = models.CharField(max_length=100, blank=True, null=True)
    license_issued_date = models.DateField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Advocate {self.user.username} - {self.specialty}"

class Case(models.Model):
    CASE_STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('pending', 'Pending'),
    ]
    
    case_number = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200,default='law')
    description = models.TextField(blank=True, null=True)
    filing_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=CASE_STATUS_CHOICES, default='open')
    
    litigant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='litigant_cases',default=0)
    advocate = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='advocate_cases', blank=True, null=True)
    court_staff = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name='staff_cases', blank=True, null=True)

    def __str__(self):
        return f"Case {self.case_number} - {self.title}"

    class Meta:
        ordering = ['-filing_date']
