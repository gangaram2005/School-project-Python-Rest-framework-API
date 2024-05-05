from django.contrib import admin
from django.urls import path,include
from account.views import *
from account.Hod_views import *
import os
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('profile/', UserProfileView.as_view(),name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(),name='changepassword'),
    path('send-reset-password-email/', SendResetPasswordEmailView.as_view(),name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(),name='reset-password'),
    
    path('classapi/', ClassApi.as_view(),name='addclass'),
    path('classapi/<int:pk>', ClassApi.as_view(),name='addclass'),
    
    path('shiftapi/',Shiftapi.as_view(),name='add_shift'),
    path('shiftapi/<int:pk>',Shiftapi.as_view(),name='view'),
    
    path('collegeapi/', CollegeApi.as_view()),
    path('collegeapi/<int:pk>', CollegeApi.as_view()),
    
    path('grouptime/',GroupApi.as_view()),
    path('grouptime/<int:pk>',GroupApi.as_view()),
    
    path('yearapi/',YearApi.as_view(),name='yearapi'),
    path('yearapi/<int:pk>',YearApi.as_view(),name='yearapi'),
    
    path('courseapi/', CourseListCreate.as_view()),
    path('courseapi/<int:pk>', CourseDRD.as_view()),
   
#    path('branchapi/', BranchListCreate.as_view()),
#    path('branchapi/<int:pk>', BranchURD.as_view()),

    path('branchapi/',BranchApi.as_view(),name='yearapi'),
    path('branchapi/<int:pk>',BranchApi.as_view(),name='yearapi'),

   path('subjectapi/', SubjectApi.as_view(),name='subject'),
   path('subjectapi/<int:pk>', SubjectApi.as_view(),name='subject'),
   
    

    
    
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)