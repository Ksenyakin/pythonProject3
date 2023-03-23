# myproject/urls.py

from django.urls import path
from myapp.views import member_list

urlpatterns = [
    path('members/', member_list, name='member_list'),
]