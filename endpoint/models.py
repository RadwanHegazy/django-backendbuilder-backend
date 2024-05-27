from django.db import models
from users.models import Tenant
from uuid import uuid4
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

class Endpoint (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    json = models.JSONField()
    tenant = models.ForeignKey(Tenant, related_name='endpotin_tenant',on_delete=models.CASCADE)
    name = models.CharField(max_length=225)

    def __str__(self) : 
        return self.name

@receiver(post_save, sender=Endpoint)
def slugify_name (created, instance:Endpoint, **other) : 
    if created :
        new_name = slugify(instance.name)
        instance.name = new_name
        instance.save()