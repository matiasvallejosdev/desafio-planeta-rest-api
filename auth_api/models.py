from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Email must be provided')
        email_normalized = self.normalize_email(email)
        user = self.model(email=email_normalized.lower(), **kwargs)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    instance_name = models.CharField(max_length=255)
    count_auth = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['instance_name']

    def get_full_name(self):
        return str(self.instance_name)

    def __str__(self):
        return self.email
