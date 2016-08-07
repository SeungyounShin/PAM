from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Post(models.Model):
    product = models.CharField('PRODUCT',max_length=50)
    description = models.TextField('DESCRIPTION')
    pub_date = models.DateTimeField(default = timezone.now)
    price = models.IntegerField()

    def __str__(self):
        return "%s : %s" %(self.product,self.price)


    
