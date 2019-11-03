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
        
        
