from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import RegexValidator
USER_1=1
USER_2=2
USER_3=3
USER_ROLES=(
    (USER_1, 'Client'),
    (USER_2,'Business_account'),
    (USER_3,'Admin')
)

class MainUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class UserNew(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('user name'), max_length=50, unique=True,
                                 error_messages={'unique': _("A user with that username already exists."), })
    email = models.EmailField(_('email address'), unique=True,
                              error_messages={'unique': _("A user with that email already exists."), })
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    objects = MainUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class Profile(models.Model):
    user= models.OneToOneField(UserNew, on_delete=models.CASCADE,related_name='profile')
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+879999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True,null=True)
    role = models.SmallIntegerField(choices=USER_ROLES, default=USER_1)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = _('profile')


class Location(models.Model):
    profile=models.OneToOneField(Profile,on_delete=models.CASCADE)
    address_1 = models.CharField(_("address"), max_length=128,blank=True)
    city = models.CharField(_("city"), max_length=64, default="Almaty")
    country = models.CharField(_("country"), max_length=64, default="Kazakhstan")
    zip_code = models.CharField(_("zip code"), max_length=7, default="050000")