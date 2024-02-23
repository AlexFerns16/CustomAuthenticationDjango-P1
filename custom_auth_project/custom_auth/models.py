from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, username, usercode, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, usercode=usercode, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, usercode, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email=email, username=username, usercode=usercode, password=password, **extra_fields)


class CustomUser(AbstractBaseUser):
    
    age = models.PositiveIntegerField(blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=500, unique=True)
    usercode = models.IntegerField(unique=True, default=0)
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'usercode'
    REQUIRED_FIELDS = ['email', 'username']
    
    objects = CustomUserManager()
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    def __str__(self):
        return self.email
