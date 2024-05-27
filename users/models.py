from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager
from uuid import uuid4
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify

class Manager (BaseUserManager) : 
    def create_user (self,email,password,**fields) : 
        email = self.normalize_email(email)
        user = self.model(**fields)
        user.email = email
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,**fields) :
        fields['is_staff'] = True 
        fields['is_superuser'] = True 
        return self.create_user(**fields)
    

class User (AbstractUser) :
    objects = Manager() 
    first_name = None
    last_name = None
    id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    username = None
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=225, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('full_name',)

    def __str__(self) -> str : 
        return self.full_name
    
    
class Tenant (models.Model) : 
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=225)
    user = models.ForeignKey(User,related_name='user_tenant',on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
@receiver(post_save, sender=User)
def create_user_tenant (created, instance:User, **kwargs):
    if created:
        tenant = Tenant(name=slugify(instance.full_name),user=instance)
        tenant.save()