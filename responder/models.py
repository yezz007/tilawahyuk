from django.db import models
from django.contrib.postgres.fields import JSONField

class Organization(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=128, blank=False)
	register_token = models.CharField(max_length=8, blank=False) #used for adding users
	group_count = models.IntegerField(default=0)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return self.name

class Group(models.Model):
	group_id = models.CharField(max_length=256)
	register_date = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=32, blank=False)
	organization = models.ForeignKey('Organization')
	user_count = models.IntegerField(default=0)

	class Meta:
		ordering = ('register_date',)

	def __str__(self):
		return self.name

class User(models.Model):
	user_id = models.CharField(max_length=256)
	register_date = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=32, blank=False)
	group = models.ForeignKey('Group')
	tilawah_count = models.IntegerField(default=0)
	tilawah_miss = models.IntegerField(default=0)
	tilawah_day = JSONField()

	class Meta:
		ordering = ('register_date',)

	def __str__(self):
		return self.name