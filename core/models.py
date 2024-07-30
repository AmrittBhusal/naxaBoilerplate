from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from .managers import Projectmanagers
from django.contrib.gis.db import models 
from user.models import UserProfile
# Create your models here.


class Userprofile(models.Model):
    gender_choice= (
        ('male','male'),
        ('female','female')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    Email = models.EmailField(null=True)
    phone = models.CharField(max_length=20, null=True)
    gender = models.CharField(choices=gender_choice, max_length=10, null=True)
    files = models.FileField(upload_to='userprofiles/',null=True)
    date = models.DateField( null=True)
    location= models.PointField(blank=True, null=True)
    # userprofile= models.Manager()

    def __str__(self):  
        return f'{self.user.username}'


class Deparment(models.Model):
    userprofile= models.ForeignKey(Userprofile, on_delete=models.CASCADE,related_name='Deparments' ,blank=True, null=True)
    user_userprofile= models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='departments',blank=True,null=True)
    department_name= models.CharField(max_length=50)
    description  = models.TextField(null=True, blank=True)
    department_number= models.IntegerField(null=True)
    department_open =models.BooleanField(default=True)

    # department = models.Manager()

    def __str__(self):
        return self.department_name


class ProjectSite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True) 
    proj_site_cordinates= models.PointField()
    area= models.PolygonField()
    way_from_home=models.LineStringField()


class Project(models.Model):
    userprofile        = models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name='project',blank=True,default=True)
    department_field = models.ForeignKey(Deparment, on_delete=models.CASCADE, related_name='projects')
    user_userprofile= models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='projects',blank=True,null=True)
    projectsite=models.ForeignKey(ProjectSite, on_delete=models.CASCADE, related_name='project', blank=True,null=True)
    project_name = models.CharField(max_length=50)
    start_date   = models.DateTimeField(default=timezone.now)
    end_date     = models.DateField(null=True)
    is_active    = models.BooleanField(default=True)
    # project = Projectmanagers()# custommanager
    # project_obj   = models.Manager() 
    def __str__(self):
        return self.project_name

class Document(models.Model):
    userprofile        = models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name='documents', blank=True, null=True)
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='documents')
    user_userprofile= models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='documents',blank=True,null=True)
    title        = models.CharField( max_length=50)
    description  = models.TextField()
    files =  models.FileField(upload_to='document/',null=True)
    date = models.DateField( null=True)
    # document= models.Manager()

    def __str__(self):
        return self.title
    

class Summary(models.Model):
    monthly_total_projects = models.PositiveBigIntegerField(null=True, blank=True)
    monthly_total_users = models.PositiveBigIntegerField(null=True, blank=True)
    annual_total_projects = models.PositiveBigIntegerField(null=True, blank=True)
    annual_total_users = models.PositiveBigIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   

