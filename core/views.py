from django.shortcuts import render
from rest_framework import status
from core.models import Userprofile,Project,Document,Deparment,ProjectSite,Summary  
from core.serializers import UserprofileSerializers,DepartmentSerializers,ProjectSerializers,DocumentSerializers,ProjectSiteSerializer,SummarySerializer
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
import geopandas as gpd
import os
import zipfile
import tempfile
from shapely.geometry import Point, LineString, Polygon
from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from core.tasks import add,update_summary_everynight, calling_fake_project_data
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def user(request):
    return render(request,'user.html')

# funcation based apiview of Userprofile

@api_view(['GET','POST','DELETE','PATCH','PUT'])
@authentication_classes([SessionAuthentication])
# @permission_classes([IsAuthenticated])
def Userprofile_api(request):
    
    if request.method=='GET':
        date = request.query_params.get('date',None)
        if  date is not None:
            date_selected= Userprofile.objects.filter(date=date)
            serailizer=UserprofileSerializers(date_selected,many=True)
            return Response(serailizer.data)
        else:
            querysets=Userprofile.objects.all()
            serailizers=UserprofileSerializers(querysets,many=True)
            return Response(serailizers.data)
    
    if request.method=='POST':
        serializer=UserprofileSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"sucessfully your data is posted"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='PUT':
        selected_row=Userprofile.objects.get(id=pk)
        serializer=UserprofileSerializers(selected_row,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'sucessfully your data is updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='PATCH':
        selected_row=Userprofile.objects.get(id=pk)
        serializer=UserprofileSerializers(selected_row,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data is patched sucessfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='DELETE':
        selected_row=Userprofile.objects.get(id=pk)
        selected_row.delete()
        return Response( {'msg':'selected row is deleted'}) 
    
# class based apiview of department

class   Department_api(APIView):
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self, request, pk=None, format=None):
        userprofile = request.query_params.get("userprofile", None)
        if userprofile is not None:
            selected_row=Deparment.objects.get(userprofile_id=userprofile)
            serializer=DepartmentSerializers(selected_row)
            return Response(serializer.data)
        else:
            querysets=Deparment.objects.all()
            serailizers=DepartmentSerializers(querysets,many=True)
            return Response(serailizers.data)
       

    def post(self,request,pk=None,format=None):
        serializer=DepartmentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"sucessfully your data is posted"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

    def put(self,request,pk=None,format=None):
        selected_row=Deparment.objects.get(id=pk)
        serializer=DepartmentSerializers(selected_row,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'sucessfully your data is updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

    def patch(self,request,pk=None, format=None):
        selected_row=Deparment.objects.get(id=pk)
        serializer=DepartmentSerializers(selected_row,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data is patched sucessfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    

    def delete(self,request,pk=None, format=None):
        selected_row=Deparment.objects.get(id=pk)
        selected_row.delete()
        return Response( {'msg':'selected row is deleted'}) 

    
#  apiview of project

class project_api(APIView):

    def get(self, request, pk=None, format=None):
        if pk is not None:
            try:
                selected_row=Project.objects.get(id=pk)
                serializer=ProjectSerializers(selected_row)
                return Response(serializer.data)
            except Project.DoesNotExist:
                return Response({"message": "Project not found"}, status=404)
         
        querysets=Project.objects.all()
        serailizers=ProjectSerializers(querysets,many=True)
        return Response(serailizers.data)
    
    def post(self,request,pk=None,format=None):
        serializer=ProjectSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"sucessfully your data is posted"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

    def put(self,request,pk=None,format=None):
        selected_row=Project.objects.get(id=pk)
        serializer=ProjectSerializers(selected_row,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'sucessfully your data is updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

    def patch(self,request,pk=None, format=None):
        selected_row=Project.objects.get(id=pk)
        serializer=ProjectSerializers(selected_row,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data is patched sucessfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    

    def delete(self,request,pk=None, format=None):
        selected_row=Project.objects.get(id=pk)
        selected_row.delete()
        return Response( {'msg':'selected row is deleted'}) 
    
    

    
    
# apiview of Document
class document_api(APIView):

    def get(self, request, pk=None, format=None):
        date=request.query_params.get('date',None)
        if date is not None:
            selected_row=Document.objects.filter(date=date)
            serializer=DocumentSerializers(selected_row, many=True)
            return Response(serializer.data)
        else:
            querysets=Document.objects.all()
            serailizers=DocumentSerializers(querysets,many=True)
            return Response(serailizers.data)
    
    def post(self,request,pk=None,format=None):
        fil
        serializer=DocumentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"sucessfully your data is posted"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

    def put(self,request,pk=None,format=None):
        selected_row=Document.objects.get(id=pk)
        serializer=DocumentSerializers(selected_row,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'sucessfully your data is updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

    def patch(self,request,pk=None, format=None):
        selected_row=Document.objects.get(id=pk)
        serializer=DocumentSerializers(selected_row,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data is patched sucessfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    

    def delete(self,request,pk=None, format=None):
        selected_row=Document.objects.get(id=pk)
        selected_row.delete()
        return Response( {'msg':'selected row is deleted'}) 


    
class Projectsite_api(APIView):

    def get(self,request):
        querysets=ProjectSite.objects.all()
        serailizer=ProjectSiteSerializer(querysets,many=True)

        return Response(serailizer.data)

    def post(self, request, format=None):
        serializer=ProjectSiteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"sucessfully your data is posted"},status=status.HTTP_201_CREATED)
        return Response(serailizer.errors,status=status.HTTP_404_NOT_FOUND)


class Downloadfile(APIView):
    def get(self, request, project_id):
        crs = "EPSG:4326" 
        try:
            project = get_object_or_404(Project, id=project_id)         
        except Project.DoesNotExist:
            return Response({"message": "Project not found"}, status=404)
        # project_sites = project.projectsite_set.all()
        # print("--------------------", project_fields)
        # print(project_sites,"++++++++++++=")


        project_sites = ProjectSite.objects.filter(project=project)
        print("====================", project_sites)
        point_geometries = []
        line_geometries = []
        polygon_geometries = []
        attributes = []

        # for attrs in project:

        attrs={
            'project_name':project.project_name,
            'start_date':project.start_date,
            'end_date':project.end_date,
            'coordinate':project.projectsite.proj_site_cordinates,
        }

        print("-----------------", attrs)

        for site in project_sites:
            if site.proj_site_cordinates:
                point = Point(site.proj_site_cordinates.x, site.proj_site_cordinates.y)
                point_geometries.append(point)
                attributes.append(attrs)
                
            if site.way_from_home:
                line = LineString(site.way_from_home.coords)
                line_geometries.append(line)
                attributes.append(attrs)

            if site.area:
                polygon = Polygon(site.area.coords[0])
                polygon_geometries.append(polygon)
                attributes.append(attrs)

        point_gdf = gpd.GeoDataFrame(attributes,geometry=point_geometries, crs=crs)
        print(point_gdf,'+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==')
        linestring_gdf = gpd.GeoDataFrame(attributes,geometry=line_geometries,crs=crs)
        polygon_gdf = gpd.GeoDataFrame(attributes,geometry=polygon_geometries,crs=crs)

        with tempfile.TemporaryDirectory() as temp_dir:
            point_path = os.path.join(temp_dir, 'point_shapefile.shp')
            if not point_gdf.empty:
                point_gdf.to_file(point_path)

            line_path = os.path.join(temp_dir, 'line_shapefile.shp')
            linestring_gdf.to_file(line_path)

            polygon_path = os.path.join(temp_dir, 'polygon_shapefile.shp')
            polygon_gdf.to_file(polygon_path)

            zip_path = os.path.join(temp_dir, 'exported_data.zip')
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for shapefile_path in [point_path, line_path, polygon_path]:
                    for file_extension in ['.shp', '.shx', '.dbf']:
                        file_path = shapefile_path.replace('.shp', file_extension)
                        if os.path.exists(file_path):
                            zip_file.write(file_path, os.path.basename(file_path))

            with open(zip_path, 'rb') as zip_data:
                response = HttpResponse(zip_data, content_type='application/zip')
                response['Content-Disposition'] = f'attachment; filename="exported_data_{project_id}.zip"'
                return response
        return Response({"error": "No data to export."}, status=204)

class Summary_api(APIView):
    def get(self,request):
        querysets=Summary.objects.all()
        serailizer=SummarySerializer(querysets, many=True)
        return Response(serailizer.data)



@api_view(['GET'])
def Celerytask(request):
    # result=calling_fake_project_data.delay()
    result = project.objects.all()
    serailizer=ProjectSerializers(result,  many=True)
    return Response(serailizer.data)

    
        

       
        






