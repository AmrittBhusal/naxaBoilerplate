from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import UserProfile
from rest_framework.decorators import api_view
from user.serializers import UserProfileSerializer


# Create your views here.
@api_view(['GET','POST','DELETE','PATCH','PUT'])
# @authentication_classes([SessionAuthentication])
# @permission_classes([IsAuthenticated])
def Userprofile_api(request):
    
    if request.method=='GET':
        date = request.query_params.get('date',None)
        if  date is not None:
            date_selected= UserProfile.objects.filter(date=date)
            serailizer=UserProfileSerializer(date_selected,many=True)
            return Response(serailizer.data)
        else:
            querysets=UserProfile.objects.all()
            serailizers=UserProfileSerializer(querysets,many=True)
            return Response(serailizers.data)
    
    if request.method=='POST':
        serializer=UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"sucessfully your data is posted"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='PUT':
        selected_row=UserProfile.objects.get(id=pk)
        serializer=UserProfileSerializer(selected_row,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'sucessfully your data is updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='PATCH':
        selected_row=UserProfile.objects.get(id=pk)
        serializer=UserProfileSerializer(selected_row,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data is patched sucessfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='DELETE':
        selected_row=UserProfile.objects.get(id=pk)
        selected_row.delete()
        return Response( {'msg':'selected row is deleted'}) 


