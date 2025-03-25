#the urls to route the api 

from django.contrib import admin
from django.urls import path, include
from users.views import home
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('',home,name='home'),
    path('', RedirectView.as_view(url='/api/', permanent=False)),  # Redirect root to /api/
]