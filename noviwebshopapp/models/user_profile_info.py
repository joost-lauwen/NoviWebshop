from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    role_choices = [
                    ('teacher', 'Leraar'),
                    ('student', 'Student')
                    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    role = models.CharField(max_length=25, choices=role_choices)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
    