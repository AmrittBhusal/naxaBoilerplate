from django.contrib import admin
from .models import Userprofile,Deparment,Project,Document,Summary,ProjectSite
import csv
from django.http import HttpResponse


@admin.register(Userprofile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display= ('user','Email','phone','gender','files','date','location')
    list_filter = ('user',)


def download_csv(self,request,queryset):
    meta = Deparment
    field_names = ('department_name','description','department_number','department_open')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; exported_data.csv'.format(meta)
    writer = csv.writer(response)
    writer.writerow(field_names)
    for obj in queryset:
        row = writer.writerow([getattr(obj, field) for field in field_names])
    return response
download_csv.short_description = "Download as csv"

class DepartmentAdmin(admin.ModelAdmin):
    list_display=('department_name','description','department_number','department_open')
    list_filter=('department_name','department_number')
    actions=[download_csv]

   

class ProjectAdmin(admin.ModelAdmin):
    list_display=('id','project_name','department_field','start_date','end_date','is_active','userprofile')
    list_filter=('userprofile',)
    
class DocumentAdmin(admin.ModelAdmin):
    list_display=('project_name','title','description','files','date')
    list_filter=('title',)

class ProjectSiteAdmin(admin.ModelAdmin):
    list_display=('proj_site_cordinates','area','way_from_home',)

class SummaryAdmin(admin.ModelAdmin):
    list_display=('monthly_total_projects','monthly_total_users','annual_total_projects','annual_total_users','created_at','updated_at')

# Register your models here.
# admin.site.register(Userprofile, UserProfileAdmin)
admin.site.register(Deparment, DepartmentAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Summary,SummaryAdmin)
admin.site.register(ProjectSite,ProjectSiteAdmin)