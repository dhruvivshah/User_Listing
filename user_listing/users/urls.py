#urls to route the api but this is a sub url file wherein it can change the view of the file to either json or api
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('users/', UserViewSet.as_view({'get': 'list'}), name='user-list'),  # Adjust according to your viewset
]