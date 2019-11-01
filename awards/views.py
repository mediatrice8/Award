# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import SignUpForm,ProfileForm,ProjectsForm,CommentsForm,RateForm
from .models import Profile,Projects,Comments
from django.http import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Projects,Profile
from .serializer import ProjectsSerializer,ProfileSerializer


# Create your views here.
def signup(request):
    form = SignUpForm
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user=authenticate(username=username,email=email,password=password)
            user.save()
            profile=Profile(user=user)
            profile.save()
            login(request,user)
            return redirect('/')
    return render(request,'registration/login.html',{"form":form})

def index(request):
    try:
        projects=Projects.objects.all()
    except Exception as e:
        raise  Http404()
    return render(request,'index.html',{"projects":projects})

def projects(request):
        current_user = request.user
        if request.method == 'POST':
                form = ProjectsForm(request.POST,request.FILES)
                if form.is_valid():
                        project = form.save(commit=False)
                        project.user = request.user
                        project.save()
                return redirect('index')

        else:
                form=ProjectsForm()
        return render(request,'project.html',{'form':form})
        

@login_required(login_url='/account/login/')
def search(request):

    if 'title' in request.GET or request.GET['title']:
        search_item = request.GET.get('title')
        searched_projects = Projects.search_project(search_item)
      
        message = f"{search_item}"
        return render(request, 'search.html',{"message":message,"projects": searched_projects})
    else:
        message = "You haven't searched for any user"
        return render(request, 'search.html',{"message":message})
    
@login_required(login_url='/account/login/')
def profile(request,user_id):
        current_user=request.user.username
        if request.method == 'POST':
                form = ProfileForm(request.POST, request.FILES)
                if form.is_valid():
                        profile = form.save(commit=False)
                        profile.user = current_user
                        profile.save()
                        return redirect('index')
        else:
                form = ProfileForm()
        user = User.objects.all()
        image = Projects.objects.filter(user__username=current_user)
        profile = Profile.objects.filter(user__username = current_user)
        return render(request,"profile/profile.html",{"user":user,"image":image,"profile":profile})
        
def update_profile(request):
        current_user=request.user
        if request.method =='POST':
                if Profile.objects.filter(user_id=current_user).exists():
                        form = ProfileForm(request.POST,request.FILES,instance=Profile.objects.get(user_id = current_user))
                else:
                        form=ProfileForm(request.POST,request.FILES)
                if form.is_valid():
                        profile=form.save(commit=False)
                        profile.user=current_user
                        profile.save()
                        return redirect('profile',current_user.id)
        else:
                if Profile.objects.filter(user_id = current_user).exists():
                        form=ProfileForm(instance =Profile.objects.get(user_id=current_user))
                else:
                        form=ProfileForm()
        return render(request,'profile/profiles.html',{"form":form}) 



               
def comment(request,project_id):
    current_user=request.user
    if request.method == 'POST':
        proj= Projects.objects.get(id=project_id)
        form=CommentsForm(request.POST, request.FILES)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.user = current_user
            comment.project=proj
            comment.save()
            return redirect('index')
    else:
        form=CommentsForm()   
    return render(request,'reviews.html',{"form":form,"project_id":project_id})

@login_required(login_url='/accounts/login/')
def rate(request,user_id):
       rate = Projects.objects.filter(id=user_id).first()
       average_score = round(((rate.design + rate.usability + rate.content)/3),2)
       if request.method == 'POST':
           rate_form = RateForm(request.POST)
           if rate_form.is_valid():
               rate.vote_submissions+=1
               if rate.design == 0:
                   rate.design = int(request.POST['design'])
               else:
                   rate.design = (rate.design + int(request.POST['design']))/2
               if rate.usability == 0:
                   rate.usability = int(request.POST['usability'])
               else:
                   rate.usability = (rate.usability + int(request.POST['usability']))/2
               if rate.content == 0:
                   rate.content = int(request.POST['content'])
               else:
                   rate.content = (rate.content + int(request.POST['usability']))/2
               rate.save()
               return redirect('index')
       else:
           rate_form = RateForm()
           return render(request,'rate.html',{"rate_form":rate_form,"rate":rate,"average_score":average_score})
       
class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)
    
class ProjectsList(APIView):
    def get(self,request,format=None):
        all_projects=Projects.objects.all()
        serializers=ProjectsSerializer(all_projects,many=True)
        return Response(serializers.data)