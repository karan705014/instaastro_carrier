from django.contrib import admin
from .models import Job
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display=("role","summary","department","description",
                  "vacancies","location" ,"min_exp","max_exp",
                  "edu_requirment","skill_requirment","min_salary" ,
                  "max_salary","job_type","work_mode" ,"job_post_date",
                  "end_apply_date" ,"status")