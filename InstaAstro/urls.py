from django.contrib import admin
from django.urls import path, include
#new coments are added
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Career_page.urls")),
]
