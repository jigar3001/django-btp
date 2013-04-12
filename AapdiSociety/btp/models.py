from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Gossip(models.Model):
		location=models.CharField(primary_key=True,max_length=100)
		type=models.CharField(max_length=100)

class Services(models.Model):
		service_name=models.CharField(primary_key=True,max_length=100)
		type=models.CharField(max_length=100)

class Data(models.Model):
		service_name=models.ForeignKey(Services)
		sp_name=models.ForeignKey(User)
		ratings=models.FloatField()
		
class User_Provides(models.Model):
	username=models.ForeignKey(User)
	service_name=models.ForeignKey(Services)

class User_Wishes(models.Model):
	username=models.ForeignKey(User)
	service_name=models.ForeignKey(Services)

class Ratings(models.Model):
	sp_name=models.ForeignKey(User)
	service_name=models.ForeignKey(Services)

class EnterAndReadGossip(models.Model):
	username=models.ForeignKey(User)
	location=models.ForeignKey(Gossip)