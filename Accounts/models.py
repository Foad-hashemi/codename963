import timez as timez
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import datetime


class UserManager(BaseUserManager):
    def create_user(self, email, fullname, password=None, ):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            fullname=fullname,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, fullname, password=None):
        user = self.create_user(
            email,
            password=password,
            fullname=fullname,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    fullname = models.CharField(max_length=255, default=None)
    date_of_birth = models.DateField(default=datetime.datetime.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['fullname']

    def __str__(self):
        return self.fullname

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin



