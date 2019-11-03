# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

class ProfileTest(TestCase):
    def setUp(self):
        self.new_user=User(username='hono',email='hoza@gmail.com')
        self.new_user.save()
        self.new_profile=Profile(user=self.new_user,phone="536382210",bio='developer')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_data(self):
        self.assertTrue(self.new_profile.bio,"developer")
        self.assertTrue(self.new_profile.user,self.new_user)

    def test_save(self):
        self.new_profile.save()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_delete(self):
        profile = Profile.objects.filter(id=1)
        profile.delete()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)==0)


    def test_edit_profile(self):
        self.new_profile.save()
        self.update_profile = Profile.objects.filter(bio='developer').update(bio = 'web designer')
        self.updated_profile = Profile.objects.get(bio='web designer')
        self.assertTrue(self.updated_profile.bio,'web designer')
        
        
class projectsTest(TestCase):
    def setUp(self):
        self.user=User(username='hono',email='hoza@gmail.com')
        self.user.save()
        self.new_profile=Profile(user=self.user,phone="536382210",bio='developer')
        self.new_profile.save()
        self.new_project = Projects(user=self.user,link="https://ig20.herokuapp.com/")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_project,Projects))

    def test_data(self):
        self.assertTrue(self.new_project.link,"https://news-8-app.herokuapp.com/")

    def test_save(self):
        self.new_project.save()
        projects = Projects.objects.all()
        self.assertTrue(len(projects)>0)

    def test_delete(self):
        project = Projects.objects.filter(id=1)
        project.delete()
        projects = Projects.objects.all()
        self.assertTrue(len(projects)==0)

    def test_update_project(self):
        self.new_project.save()
        self.update_project = Projects.objects.filter(link='https://ig20.herokuapp.com/').update(link = 'https://news-8-app.herokuapp.com/')
        self.updated_project = Projects.objects.get(link='https://news-8-app.herokuapp.com/')
        self.assertTrue(self.updated_post.link,'https://news-8-app.herokuapp.com/')

class CommentTest(TestCase):
    def setUp(self):
        self.new_user=User(username='hono',email='hoza@gmail.com')
        self.new_user.save()
        self.new_profile=Profile(user=self.new_user,phone="536382210",bio='developer')
        self.new_profile.save()
        self.new_project = Projects(user=self.new_user,link='https://www.google.com')
        self.new_project.save()
        self.comment=Comments(user=self.new_user,project=self.new_project,comment='nice one')

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comments))

    def test_data(self):
        self.assertTrue(self.comment.comment,"nice one")

    def test_comments(self):
        self.comment.save()
        comment=Comments.objects.all()
        self.assertTrue(len(comment)>0)