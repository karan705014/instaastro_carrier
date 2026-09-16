from django.urls import path
from .views import (ListAPI,DetailAPI,AdminJobAPI,AdminJobDetailAPI,)
urlpatterns = [
    path("jobs/",ListAPI.as_view(),name="job-list"),
    path("jobs/<int:pk>/",DetailAPI.as_view(),name="job-detail"),
    path("admin/jobs/",AdminJobAPI.as_view(),name="admin-job-list"),
    path("admin/jobs/<int:pk>/",AdminJobDetailAPI.as_view(),name="admin-job-detail"),
]