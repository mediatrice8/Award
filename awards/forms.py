from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Projects,Comments
class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(max_length=40)
    # last_name = forms.CharField(max_length=40)

    class Meta:
        model = User
        exclude = []
        fields = ['username','email','password1','password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # exclude = ['user']
        fields = ['profile_picture','bio','phone']

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        # exclude = ['user']
        fields = ['title','link','image']


class CommentsForm(forms.ModelForm):
    class Meta:
        model=Comments
        exclude=[]
        fields=['comment']


class RateForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['design','usability','content']


# rating_choices = [
#     (1, '1'),
#     (2, '2'),
#     (3, '3'),
#     (4, '4'),
#     (5, '5'),
#     (6, '6'),
#     (7, '7'),
#     (8, '8'),
#     (9, '9'),
#     (10, '10'),
# ]

# class Votes(forms.Form):
#     design = forms.CharField(label='Design level', widget=forms.RadioSelect(choices=rating_choices))

#     usability = forms.CharField(label='Usability level', widget=forms.RadioSelect(choices=rating_choices))

#     creativity  = forms.CharField(label='Creativity level', widget=forms.RadioSelect(choices=rating_choices))

#     content = forms.CharField(label='Content level', widget=forms.RadioSelect(choices=rating_choices))