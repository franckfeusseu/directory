import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
"""
Mailinglist class to contains the different mailing list create by authorised 
authors. 
"""
class MailingList(models.Model):
    name = models.CharField(max_length=140, verbose_name=_('mailinglist name'))
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

"""
Subscriber class that contains all the subscribers for a particular 
mailing list.
"""
class Subscriber(models.Model):
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    mailinglist = models.ForeignKey(MailingList, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['email', 'mailinglist', ]

"""
class Message to track all the messages send from mailing list
"""
class Message(models.Model):  
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mailinglist = models.ForeignKey(to=MailingList, on_delete=models.CASCADE)
    subject = models.CharField(max_length=140)
    body = models.TextField()
    date_create = models.DateTimeField(
        verbose_name=_('created'), auto_now_add=True, editable=False
    )  

