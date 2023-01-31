from django.urls import path 
from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('friends/<str:pk>',views.detail,name="detail"),
    path('sent_msg/<str:pk>',views.sentMessages,name='sent_msg')
]