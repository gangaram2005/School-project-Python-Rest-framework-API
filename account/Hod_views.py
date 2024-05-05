from django.shortcuts import render,redirect,HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.parsers import FileUploadParser # images upload garna ko lagi ho 

#Add Course
class CourseListCreate(ListCreateAPIView):
    renderer_classes=[UserRenderer]
    queryset=Course.objects.all()
    serializer_class=CreateCourseSerializer   
class CourseDRD(RetrieveUpdateDestroyAPIView):
    queryset=Course.objects.all()
    serializer_class = CreateCourseSerializer
 
# Branch Api
# class BranchListCreate(ListCreateAPIView):
#     parser_classes = (FileUploadParser,)
#     renderer_classes=[UserRenderer]
#     queryset=Branch.objects.all()
#     serializer_class=BranchSerializer
# class BranchURD(RetrieveUpdateDestroyAPIView):
#     parser_classes = (FileUploadParser,)
#     renderer_classes=[UserRenderer]
#     queryset=Branch.objects.all()
#     serializer_class=BranchSerializer

class BranchApi(APIView):
    #renderer_classes=[UserRenderer]
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            stu=Branch.objects.get(id=id)
            serializer=BranchSerializer(stu)
            return Response(serializer.data)
        stu=Branch.objects.all()
        serializer=BranchSerializer(stu,many=True)
        return Response(serializer.data)
    
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        #data=request.data #bhayeko data sabai yesai ma parsed bhayera milxa
        serializer=BranchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data created successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk,format=None):
        id=pk
        stu=Branch.objects.get(pk=id)
        serializer=BranchSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Complete Data Updated"})
        return Response(serializer.errors)
    
    def patch(self,request,pk,format=None):
        id=pk
        stu=Branch.objects.get(pk=id)
        serializer=BranchSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Partial Data Updated"})
        return Response(serializer.errors)
    
    def delete(self,request,pk,format=None):
        id=pk
        stu=Branch.objects.get(pk=id)
        stu.delete()
        return Response({"msg":"Data Deleted"})
        
          
# Subject 
class SubjectApi(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            stu=Subject.objects.get(id=id)
            serializer=SubjectSerializer(stu)
            return Response(serializer.data)
        stu=Subject.objects.all()
        serializer=SubjectSerializer(stu,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        #data=request.data #bhayeko data sabai yesai ma parsed bhayera milxa
        serializer=SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data created successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk,format=None):
        id=pk
        stu=Subject.objects.get(pk=id)
        serializer=SubjectSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Complete Data Updated"})
        return Response(serializer.errors)
    
    def patch(self,request,pk,format=None):
        id=pk
        stu=Subject.objects.get(pk=id)
        serializer=SubjectSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Partial Data Updated"})
        return Response(serializer.errors)
    
    def delete(self,request,pk,format=None):
        id=pk
        stu=Subject.objects.get(pk=id)
        stu.delete()
        return Response({"msg":"Data Deleted"})
        