from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


# class BaseModel(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)

#     class Meta:
#         abstract = True

class User(AbstractUser):
    pass


class Lead(models.Model):
    # SOURCE_CHOICES = (
    #     # (firstval, secondval) -> First value is saved in DB, second val is to show options
    #     ('YT', 'YouTube'),
    #     ('GOOGLE', 'Google')
    #     ('UDEMY', 'Udemy')

    # )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=50)
    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files=models.FileField(blank=True,null=True)

    def __str__(self):
        return f" {self.first_name} {self.last_name}"


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    #  NOTE: Firstname & lastname will be from user

    def __str__(self):
        return self.user.username
