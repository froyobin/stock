#coding=utf-8
from django.db import models
class stockSnName(models.Model):
	values = models.CharField(max_length=50)
	name = models.CharField(max_length=50)

