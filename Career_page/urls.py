from django.urls import path

from . import views


urlpatterns = [
    path("", views.ListAPI, name="job-list"),
    path("job/<int:id>/", views.Job_Detail, name="job-detail"),

]