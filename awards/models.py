# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
# class of Projects
class Projects(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField(max_length=320)
    link=models.URLField(max_length=60)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='projects')
    date=models.DateField(auto_now=True)
    image=models.ImageField(upload_to='image/',blank=True)
    design = models.IntegerField(choices=list(zip(range(0,11), range(0,11))), default=0)
    usability = models.IntegerField(choices=list(zip(range(0,11), range(0,11))), default=0)
    content = models.IntegerField(choices=list(zip(range(0,11), range(0,11))), default=0)
    vote_submissions = models.IntegerField(default=0)
    
    
    
    class Meta:
        ordering=['-title']
    
    def __str__(self):
        self.title

    @classmethod
    def search_project(cls,search_item):
        searched=cls.objects.filter(title__icontains=search_item)
        return searched
    
    @classmethod
    def get_all_projects(cls):
       projects=cls.objects.all().prefetch_related('comment_set')
       return projects
    
