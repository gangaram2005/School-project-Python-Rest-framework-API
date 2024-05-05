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
# Create your views here.

# Generate Token manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    
# user creation view
class UserRegistrationView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializer=UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            token=get_tokens_for_user(user)
            #token=get_tokens_for_user(user)
            return Response({'token':token,'msg':'Registration Success'},status=status.HTTP_201_CREATED)
        #print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                
# User Login Api            
class UserLoginView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializer=UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            #user_type=User.user_type
            print(email)
            print(password)
            #print(user_type)
            user=authenticate(email=email,password=password)
            if user is not None:
                user_type=user.user_type
                print(user_type)
                #return Response({'msg':'Login Success with Hod Panel'},status=status.HTTP_200_OK)
                if user_type==1:
                    #return HttpResponse("This is Hod panel")
                    token=get_tokens_for_user(user)
                    return Response({'token':token,'msg':'Login Success with Hod Panel'},status=status.HTTP_200_OK)
                    #return redirect('hod_home') 
                elif user_type==2:
                    #return redirect('staff_home')
                    token=get_tokens_for_user(user)
                    return Response({'token':token,'msg':'Login Success with Staff Panel'},status=status.HTTP_200_OK)
                elif user_type==3:
                    #return redirect('student_home')
                    token=get_tokens_for_user(user)
                    return Response({'token':token,'msg':'Login Success with studnet panel'},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_fields_errors':['email or passwod is not valid']}},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                     
# user view profile views
class UserProfileView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]
    def get(self,request,format=None):
        serializer=UserProfileSerializer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK) 

# user change password
class UserChangePasswordView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]
    def post(self,request,format=None):
        serializer=UserChangePasswordSerializer(data=request.data,context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Changed Successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Reset password 
class SendResetPasswordEmailView(APIView):
    renderer_classes=[UserRenderer] 
    def post(self,request,format=None):
        
        serializer=SendResetPasswordEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Reset Link Send. Please Check your email'},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# user password reset form  view
class UserPasswordResetView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,uid,token,format=None):
        serializer=UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token}) 
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  
# Add Class view
class ClassApi(APIView):
    renderer_classes=[UserRenderer]
    #permission_classes=[IsAuthenticated]
    def post(self,request,format=None):
        serializer=CreateClassesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Class successfully created'},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
         
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            stu=AddClass.objects.get(id=id)
            serializer=CreateClassesSerializer(stu)
            return Response(serializer.data)
        stu=AddClass.objects.all()
        serializer=CreateClassesSerializer(stu,many=True)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        id=pk
        stu=AddClass.objects.get(pk=id)
        serializer=CreateClassesSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Complete Data Updated"})
        return Response(serializer.errors)
    
    def patch(self,request,pk,format=None):
        id=pk
        stu=AddClass.objects.get(pk=id)
        serializer=CreateClassesSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Partial Data Updated"})
        return Response(serializer.errors)
    
    def delete(self,request,pk,format=None):
        id=pk
        stu=AddClass.objects.get(pk=id)
        stu.delete()
        return Response({"msg":"Data Deleted"})

            
# Shift class view
class Shiftapi(APIView):
    renderer_classes=[UserRenderer]
    #permission_classes=[IsAuthenticated]
    def post(self,request,format=None):
        serializer=ShiftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Shift created successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            stu=Shift.objects.get(id=id)
            serializer=ShiftSerializer(stu)
            return Response(serializer.data)
        stu=Shift.objects.all()
        serializer=ShiftSerializer(stu,many=True)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        id=pk
        stu=Shift.objects.get(pk=id)
        serializer=ShiftSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Complete Data Updated"})
        return Response(serializer.errors)
    
    def patch(self,request,pk,format=None):
        id=pk
        stu=Shift.objects.get(pk=id)
        serializer=ShiftSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Partial Data Updated"})
        return Response(serializer.errors)
    
    def delete(self,request,pk,format=None):
        id=pk
        stu=Shift.objects.get(pk=id)
        stu.delete()
        return Response({"msg":"Data Deleted"})

        
               
# Add College view
class CollegeApi(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            stu=College.objects.get(id=id)
            serializer=CollegeSerializer(stu)
            return Response(serializer.data)
        stu=College.objects.all()
        serializer=CollegeSerializer(stu,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        #data=request.data #bhayeko data sabai yesai ma parsed bhayera milxa
        serializer=CollegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data created successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk,format=None):
        id=pk
        stu=College.objects.get(pk=id)
        serializer=CollegeSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Complete Data Updated"})
        return Response(serializer.errors)
    
    def patch(self,request,pk,format=None):
        id=pk
        stu=College.objects.get(pk=id)
        serializer=CollegeSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Partial Data Updated"})
        return Response(serializer.errors)
    
    def delete(self,request,pk,format=None):
        id=pk
        stu=College.objects.get(pk=id)
        stu.delete()
        return Response({"msg":"Data Deleted"})
        
    
# Add Group Time View
class GroupApi(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializer=CreateGroupTimeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Group Time add Successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            grt=Grouptime.objects.get(id=id)
            serializer=CreateGroupTimeSerializer(grt)
            return Response(serializer.data)
        grt=Grouptime.objects.all()
        serializer=CreateGroupTimeSerializer(grt,many=True)
        return Response(serializer.data)
    
    def put(self,request,pk=None,format=None):
        id=pk
        grt=Grouptime.objects.get(id=id)
        serializer=CreateGroupTimeSerializer(grt,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Complete Data Updated"})
        return Response(serializer.errors)
        
    
    def delete(self,request,pk=None,format=None):
        id=pk
        grt=Grouptime.objects.get(id=id)
        grt.delete()
        return Response({"msg":"Data Deleted"})
        
            
# year add view
class YearApi(APIView):
    # get method 
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            stu=Year.objects.get(id=id)
            serializer=CreateYearSerializer(stu)
            return Response(serializer.data)
        stu=Year.objects.all()
        serializer=CreateYearSerializer(stu,many=True)
        return Response(serializer.data)
    # post method
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializer=CreateYearSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Year has been saved successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    #Put Method
    def put(self,request,pk,format=None):
        id=pk
        stu=Year.objects.get(pk=id)
        serializer=CreateYearSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Complete Data Updated"})
        return Response(serializer.errors)
    # patch 
    renderer_classes=[UserRenderer]
    def patch(self,request,pk,format=None):
        id=pk
        stu=Year.objects.get(pk=id)
        serializer=CreateYearSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Partial Data Updated"})
        return Response(serializer.errors)
    # Delete method
    def delete(self,request,pk,format=None):
        id=pk
        stu=Year.objects.get(pk=id)
        stu.delete()
        return Response({"msg":"Data Deleted"})       
        

        
        
        
            
        