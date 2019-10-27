# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
# class of Projects
class Projects(models.Model):
    title=models.CharField(max_length=30)
    image=models.ImageField(upload_to='projects/')
    description=models.TextField(max_length=320)
    link=models.URLField(max_length=60)
    design=models.IntegerField(default=0)
    usability=models.IntegerField(default=0)
    content=models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='projects')
    date=models.DateField(auto_now=True)
    image1=models.ImageField(upload_to='screenshot/',blank=True)
    image2=models.ImageField(upload_to='screenshot/',blank=True)
    
    
    class Meta:
        ordering=['-title']
    
    def __str__(self):
        self.title

    @classmethod
    def search_project(cls,word):
        searched=cls.objects.filter(name__icontains=word)
        return searched
    
class Profile(models.Model):
    profile_picture=models.ImageField(upload_to='profile/')
    bio=models.CharField(max_length=60)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.IntegerField()
    
    class Meta:
        ordering=['-profile_picture']
        
class Rates(models.Model):
    design=models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    usability=models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    content=models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    project=models.IntegerField(default=0)
    
class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField(max_length=200)
    pro_id=models.IntegerField(default=0)