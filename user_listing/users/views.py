#view page of the localhost:8000 
from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from django.http import HttpResponse
from .serializers import UserSerializer
from rest_framework.pagination import PageNumberPagination

class UserPagination(PageNumberPagination):      #function to paginate the data fetched
    page_size = 10                             #displays the data according to the page_size
#there are 10 users picked from randomuser.me and due to this pagination process one can see the data only in pieces ie.5 on each page but in api 
#on react also it shows only the first 5 data.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination

def home(request):                #view of the localhost in the desired way through html
    return HttpResponse(
        """
        <h1>Welcome to the User Listing API!</h1>
        <p>Click <a href="/api/users/">here</a> to view the list of users.</p>
        """
    )