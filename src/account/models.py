from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        # Если пользовательне вел email
        if not email:
            raise ValueError("Пользователь не вел email")
        if not username:
            raise ValueError("Пользователь не вел Username")
        
        # If all is ok, then 
        user = self.model(
            # the func normalize is write all verbs in lowercase, the func is only used in the class BaseUserManager
               email=self.normalize_email(email),
               username = username,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # Create super user for our site
    def create_superuser(self, email, username, password):
        user = self.create_user(
            # the func normalize is write all verbs in lowercase, the func is only used in the class BaseUserManager
               email=self.normalize_email(email),
               username = username,
               password=password,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email           = models.EmailField(name="email", max_length=60, unique=True)
    username        = models.CharField(max_length=30, unique=True)
    date_joined     = models.DateTimeField(name="date joined", auto_now_add=True)
    last_login      = models.DateTimeField(name="last login", auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    object = MyAccountManager()

    def __str__(self):
        return self.email
    
    # Эти функ необходоми если мы собираемся создовать новую пользователя
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True;

