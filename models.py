from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.forms import ModelForm

class Sport(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=200)
    sport = models.ForeignKey(Sport)

    def __unicode__(self):
        return self.name

class Fixture(models.Model):
    team = models.ForeignKey(Team)
    time = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.CharField(max_length=200)

    def __unicode__(self):
        return self.team

class Subscription(models.Model):
    mobile = models.CharField(max_length=15, blank=True, null=True)
    pushover = models.CharField(max_length=30, blank=True, null=True)
    user = models.ForeignKey(User)
    team = models.ForeignKey(Team)
    # Email gotten from user account

    def __unicode__(self):
        return self.user.username
        
class SubscriptionForm(ModelForm):
    class Meta:
        model = Subscription
