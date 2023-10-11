from django.db import models
from django.utils import timezone
# Create your models here.
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    dated = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/', default='images/default.jpg')


    def __str__(self):
        return self.title
    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)