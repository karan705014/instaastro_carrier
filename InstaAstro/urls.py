from django.contrib import admin
from django.urls import path, include
#new coments are added
#sthese are URl end points
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Career_page.urls")),
]
