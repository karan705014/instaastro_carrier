from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
#new coments are added
=======
#sthese are URl end points
>>>>>>> e1ac666 (add some comments)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("InstaAstro.urls")),
    path("", include("Career_page.urls")),
]
