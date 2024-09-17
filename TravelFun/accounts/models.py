from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, full_name, email, password=None):
        if not email:
            raise ValueError('用戶必須擁有電子郵件地址')
        user = self.model(
            username=username,
            full_name=full_name,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, full_name, email, password=None):
        user = self.create_user(
            username=username,
            full_name=full_name,
            email=email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Member(AbstractBaseUser):
    USER_LEVELS = (
        ('admin', 'Administrator'),
        ('editor', 'Editor'),
        ('user', 'User'),
    )

    username = models.CharField(max_length=150, unique=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    level = models.CharField(max_length=10, choices=USER_LEVELS, default='user')
    date_joined = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name', 'email']

    def __str__(self):
        return self.username