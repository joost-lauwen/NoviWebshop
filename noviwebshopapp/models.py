from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    role = models.CharField(max_length=25)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username

class Painting(models.Model):
    name = models.CharField(max_length=264)
    date_added = models.DateField(default=datetime.datetime.now())

    def __str__(self):
        return self.name
    
class Webpage(models.Model):
    Painting = models.ForeignKey(Painting, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name
    
class AccesRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.datetime.now())

    def __str__(self):
        return str(self.date)
