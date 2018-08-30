from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.


class Profile(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    about = models.TextField(max_length=255)
    image = ImageField()

    def __str__(self):
        return '{}'.format(self.username)

    class Meta:
        verbose_name_plural = 'Profile'


class Projects(models.Model):
    username = models.ForeignKey(Profile)
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = ImageField()
    github_link = models.CharField(max_length=100, blank=True, null=True)
    live_link = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.username)

    class Meta:
        verbose_name_plural = 'Projects'


class Skills(models.Model):
    username = models.ForeignKey(Profile)
    skill = models.CharField(blank=True, null=True, max_length=255)

    def __str__(self):
        return '{}'.format(self.username)

    class Meta:
        verbose_name_plural = 'Skills'


class Education(models.Model):
    username = models.ForeignKey(Profile)
    institution = models.CharField(blank=True, null=True, max_length=255)

    def __str__(self):
        return '{}'.format(self.username)

    class Meta:
        verbose_name_plural = 'Education'


class Contacts(models.Model):
    username = models.ForeignKey(Profile)
    email = models.EmailField()
    github = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.username)

    class Meta:
        verbose_name_plural = 'Contacts'


