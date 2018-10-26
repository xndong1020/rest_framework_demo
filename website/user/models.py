from django.utils import timezone
from django.db import models, transaction
from django.contrib.auth.models import AbstractUser, UserManager


class CustomizedUserManager(UserManager):
    pass
    # def create_user(self, username, password, email=None, first_name=None, last_name=None, is_staff=None,
    #                 is_superuser=None, is_active=True, **extra_fields):
    #     if not username:
    #         raise ValueError("The given username must be set")
    #
    #     email = self.normalize_email(email)
    #     with transaction.atomic():
    #         username = self.model.normalize_username(username)
    #         user = self.model(
    #             username=username, first_name=first_name, last_name=last_name, email=email, **extra_fields
    #         )
    #         user.set_password(password)  # save password in encrypted format
    #         user.save(using=self._db)
    #         return user


class User(AbstractUser):
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomizedUserManager()
