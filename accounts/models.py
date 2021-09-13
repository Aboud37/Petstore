from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class AccountUserManager(BaseUserManager):

    def create_user(self, email,gouvernerat,  password=None):
        if not email:
            raise ValueError("L'utilisateur doit avoir une adresse mail")
        if not gouvernerat:
            raise ValueError("L'utilisateur doit parvenir d'une gouvernerat")

        user = self.model(
        email = self.normalize_email(email),
        gouvernerat = gouvernerat
        )
        user.set_password(password)
        user.is_staff = True
        user.save(using= self._db)
        return user

    def create_superuser(self, email,gouvernerat,  password):

        user = self.create_user(
        email = self.normalize_email(email),
        gouvernerat = gouvernerat,
        password = password
        )

        user.is_admin= True
        user.is_staff = True
        user.save(using= self._db)
        return user

class Account(AbstractBaseUser, PermissionsMixin ):
    grvt_list= (('Tunis', 'Tunis'), ('Béja','Béja'),('Ariana','Ariana') )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    gouvernerat = models.CharField(max_length=60, choices=grvt_list)

    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=datetime.now(), blank=True, null=True)
    last_login = models.DateTimeField(default=datetime.now(), blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['gouvernerat']

    objects = AccountUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj= None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Profile(models.Model):
    user= models.OneToOneField(Account, on_delete=models.CASCADE)

    @receiver(post_save, sender=Account)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=Account)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


