from django.contrib import admin

from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):

    # Job list page
    list_display = (
        "role",
        "department",
        "location",
        "job_type",
        "work_mode",
        "min_salary",
        "max_salary",
        "status",
        "job_post_date",
        "end_apply_date",
    )

    # Filters on the right side
    list_filter = (
        "status",
        "job_type",
        "work_mode",
        "department",
    )

    # Admin search
    search_fields = (
        "role",
        "department",
        "location",
    )

    # Latest jobs first
    ordering = ("-job_post_date",)

    # Jobs per page
    list_per_page = 25

    # Add/Edit job form
    fieldsets = (
        (
            "Job Details",
            {
                "fields": (
                    "role",
                    "summary",
                    "department",
                    "job_type",
                    "work_mode",
                    "status",
                ),
            },
        ),
        (
            "Requirements",
            {
                "fields": (
                    "description",
                    "edu_requirment",
                    "skill_requirment",
                    "min_exp",
                    "max_exp",
                    "vacancies",
                ),
            },
        ),
        (
            "Location & Salary",
            {
                "fields": (
                    "location",
                    "min_salary",
                    "max_salary",
                ),
            },
        ),
        (
            "Application Dates",
            {
                "fields": (
                    "end_apply_date",
                ),
            },
        ),
    )