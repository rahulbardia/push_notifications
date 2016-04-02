from django.db import models

# Create your models here.
class Person(models.Model):
	subscriber_id = models.CharField(max_length=30)
	browser_name = models.CharField(max_length=30)
	browser_engine = models.CharField(max_length=30)
	device = models.CharField(max_length=30)


class notification(models.Model):
	notification_title = models.CharField(max_length=200)
	notification_url = models.URLField(max_length=200)
	notification_message = models.CharField(max_length=200)
	notification_tag = models.IntegerField()
	subscriber_id = models.CharField(max_length=30)



