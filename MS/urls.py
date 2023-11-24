from django.contrib import admin
from django.urls import path, re_path, include


admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('ComplaintMS.urls')),  # Use 're_path' instead of 'url'
]
