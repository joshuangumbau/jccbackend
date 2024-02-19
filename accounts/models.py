from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
import uuid

from .managers import UserManager

class AccountModel(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    client_code = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    other_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True, unique=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    user_type = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=128, verbose_name='password')
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_client = models.BooleanField(default=False)
    is_archive = models.BooleanField(default=False)
    jwt_secret = models.UUIDField(default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        return self.email

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.email

    def __str__(self):
        """
        Human redeable string representation of a user.
        """
        return self.email

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='account_groups'  # You can choose any related_name that suits your project
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='account_permissions'  # You can choose any related_name that suits your project
    )
