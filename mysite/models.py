from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

from django.db import models
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
# Create your models here.

class Post(models.Model):
    seller = models.ForeignKey('auth.User')
    product = models.CharField('PRODUCT',max_length=50)
    description = models.TextField('DESCRIPTION')
    pub_date = models.DateTimeField(default = timezone.now)
    price = models.IntegerField()
    
    def approved_comments(self):
        return self.comments.filter(approved_comment = True)

    def __str__(self):
        return "%s : %s" %(self.product,self.price)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    schoolid = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(99999)])
    phone_number = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(99999999999)])    

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    post = models.ForeignKey('mysite.Post',related_name = 'comments')
    author = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    approved_comment = models.BooleanField(default = False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

