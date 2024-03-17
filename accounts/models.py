from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from . managers import UserManager


class User(AbstractBaseUser):
    phone_number = models.CharField(
        max_length=11, unique=True,
        verbose_name='شماره تلفن ',

        )
    email = models.EmailField(
        max_length=250, unique=True,
        verbose_name='ایمیل '
    )
    full_name = models.CharField(max_length=100, verbose_name='نام ')
    avatar = models.ImageField(upload_to='avatars/Y%M%D', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'full_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin




