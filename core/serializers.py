from rest_framework import serializers
from core.models import Userprofile,Deparment,Project,Document,Summary,ProjectSite

class UserprofileSerializers(serializers.ModelSerializer):
    Deparments=serializers.StringRelatedField(many=True)
    project=serializers.StringRelatedField(many=True)
    documents=serializers.StringRelatedField(many=True)
    class Meta:
        model=Userprofile
        fields= ['user','Email','phone','gender','Deparments','project','documents','files','date']



class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model= Deparment
        fields= '__all__'

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model= Project
        fields=['id','userprofile','department_field','projectsite','project_name','start_date','end_date','is_active']

class DocumentSerializers(serializers.ModelSerializer):
    class Meta:
        model= Document
        fields= ['userprofile','project_name','title','description','files','date']

class SummaryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = '__all__'

class ProjectSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectSite
        fields = ['id','user', 'proj_site_cordinates', 'area', 'way_from_home']


class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model=Summary
        fields=['monthly_total_projects','monthly_total_users','annual_total_projects','annual_total_users','created_at','updated_at']