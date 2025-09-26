from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, UserManager
from stella.models import create_id
from stella.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator
#from django.core.mail import send_mail
 
 
class UserManager(BaseUserManager):
 
    def _create_user(self, username, email, password=None):
        if not email: #nameも必須入力にしたい else?
            raise ValueError('メールアドレスを入力して下さい')
        user = self.model(
            username=username,
            email=self.normalize_email(email),            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username, email=None, password=None):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password)
 
    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

    #def create_superuser(self, username, email, password, **extra_fields):
        #extra_fields.setdefault('is_staff', True)
        #extra_fields.setdefault('is_superuser', True)

        #if extra_fields.get('is_staff') is not True:
            #raise ValueError('Superuser must have is_staff=True.')
        #if extra_fields.get('is_superuser') is not True:
            #raise ValueError('Superuser must have is_superuser=True.')

        #return self._create_user(username, email, password, **extra_fields)
 
 
class CustomUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(default=create_id, primary_key=True, max_length=22)
    username = models.CharField(max_length=50, unique=True, blank=False)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', ]
    bookmark = models.ManyToManyField(Article, verbose_name='お気に入り', blank=True)

    def __str__(self):
        return self.username
 
    def __str__(self):
        return self.email
 
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
 
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
 
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
 
 

 
 
# OneToOneFieldを同時に作成
@receiver(post_save, sender=User)
def create_onetoone(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])