from rest_framework import serializers
from .models import Projects,Profile

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id','title', 'description', 'link','user','date','image','design''usability','content','vote_submissions')
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','profile_picture', 'bio', 'phone','user')