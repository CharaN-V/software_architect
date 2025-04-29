from django.urls import path
from . import views

urlpatterns=[
        path('hello/',views.index,name='index'),
        path('api/',views.api_view,name='api'),
        ]
