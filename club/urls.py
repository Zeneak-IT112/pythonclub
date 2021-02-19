from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resources/', views.resources, name='resources'),
    path('meeting_list/', views.meetings, name='meetings'),
    path('meeting/<int:id>/', views.meeting_details, name='meeting-details'),
    path('newMeeting/', views.newMeeting, name='newmeeting'),
    path('newResource/', views.newResource, name='newresource')
]