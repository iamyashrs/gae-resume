from django.db import models


# Django Model for Storing Kudos
class Kudos(models.Model):
    count = models.IntegerField(default=1)
    made_on = models.DateTimeField(auto_now_add=True)


# Function to add a kudo
def add_kudos():
    default_kwargs = {
        'count': '1'
    }
    Kudos.objects.create(**default_kwargs)


# Get the Number of Kudos
def get_kudos():
    return Kudos.objects.all().count()
