from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """Ayuda a django a trabajar con nuestro usuario customizado"""


    def create_user(self, email, name, password=None):
        """Crea un nuevo usuario en el perfil"""
        if not email:
            raise ValueError('Los usuarios deben tener una correo electrónico')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, name, password):
        """Crea y guarda un nuevo superusuario con los detalles dados"""
        user = self.create_user(email,name, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represent un perfil de usuario dentro del sistema"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Usado para obtener el nombre completo"""

        return self.name

    def get_short_name(self):
        """Usado para obtener el nombre del usuario"""

        return self.name

    def __str__(self):
        """Django utiliza esto cuando necesita convertir un objeto en una cadena"""
        return self.email
