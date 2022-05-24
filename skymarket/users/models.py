from django.contrib.auth.models import AbstractUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _



class User(AbstractUser):
    USER_ROLE = "user"
    ADMIN_ROLE = "admin"
    ROLES = [(USER_ROLE, USER_ROLE), (ADMIN_ROLE, ADMIN_ROLE)]
    
    username = None

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=5, choices=ROLES)
    image = models.ImageField(upload_to='django_media/users/')
    
    USERNAME_FIELD = 'email' 

    REQUIRED_FIELDS = ['role'] 
    
    objects = UserManager()
    
