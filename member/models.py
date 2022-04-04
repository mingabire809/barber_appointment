from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.

class MemberManager(BaseUserManager):
    def create_user(self, full_name, email, username, phone_number, password, **other_fields):
        if not full_name:
            raise ValueError("Your name is required!!")
        if not email:
            raise ValueError("Please add your email address!")
        if not username:
            raise ValueError("Input your username!")
        if not phone_number:
            raise ValueError("Member must have a phone number!")
        if not password:
            raise ValueError("Member must have a password!")

        user = self.model(
            full_name=full_name,
            email=self.normalize_email(email),
            username=username,
            phone_number=phone_number,
          #  profile_picture=profile_picture,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, phone_number, username, full_name):

        user = self.create_user(
            email=self.normalize_email(email=email),
            password=password,
            username=username,
            full_name=full_name,
            phone_number=phone_number,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class Member(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    full_name = models.CharField(unique=True, max_length=50, null=False)
    profile_picture = models.ImageField(upload_to='Member', verbose_name='Profile Picture')
    username = models.CharField(max_length=50, null=False, unique=True)
    phone_number = models.BigIntegerField(unique=True, null=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_barber = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'full_name', 'phone_number']

    objects = MemberManager()

    def __str__(self):
        return f'{self.full_name} with username: {self.username} and email: {self.email} has phone number {self.phone_number},{self.profile_picture}, {self.id}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


#@receiver(post_save, sender=settings.AUTH_USER_MODEL)
#def create_auth_token(sender, instance=None, created=False, **kwargs):
#    if created:
#        Token.objects.create(user=instance)
