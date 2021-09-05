from django.db import models
from django.contrib.auth.models import User
#community name ,community leader, community details , community link ,user

class Contact(models.Model):
    community_name=models.CharField(max_length=50,null=False)
    leader=models.CharField(max_length=50)
    details=models.TextField()
    link=models.URLField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.link)

    class Meta:
        verbose_name_plural='Contact'

class Dummy(models.Model):
    goal=models.CharField(max_length=200)
    domain=models.CharField(max_length=200)
    interest=models.CharField(max_length=200)
    time=models.IntegerField(default=0)
    pricing=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.goal

    class Meta:
        verbose_name_plural='Dummy'

class Solution(models.Model):
    course_name=models.CharField(max_length=100)
    course_link=models.URLField(max_length=50)
    platform=models.CharField(max_length=20)
    slug=models.SlugField(max_length=35,null=False,blank=False,default='default/slug')

    def __str__(self):
        return self.course_name
    
    class Meta:
        verbose_name_plural='Solution'
