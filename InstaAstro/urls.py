from django.contrib import admin
from django.urls import path, include
#sthese are URl end points
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Career_page.urls")),
]
