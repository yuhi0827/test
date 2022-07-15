from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('realestate', include('realestate.urls')),
    path('admin/', admin.site.urls),
]
