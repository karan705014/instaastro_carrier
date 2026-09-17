from django.db import models
class Job(models.Model):
    class JobType(models.TextChoices):
        FULL_TIME = "FULL_TIME", "Full Time"
        PART_TIME = "PART_TIME", "Part Time"
        INTERNSHIP = "INTERNSHIP", "Internship"

    class WorkMode(models.TextChoices):
        ONSITE = "ONSITE", "On-site"
        REMOTE = "REMOTE", "Remote"
        HYBRID = "HYBRID", "Hybrid"
   #Status Choices for Job Status
    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        CLOSED = "CLOSED", "Closed"
        DRAFT = "DRAFT", "Draft"
        EXPIRED = "EXPIRED", "Expired"
    class Department_Type(models.TextChoices):
        ASTROLOGY = "astrology", "Astrology"
        CUSTOMER_SUPPORT = "customer_support", "Customer Support"
        SALES = "sales", "Sales"
        MARKETING = "marketing", "Marketing"
        CONTENT = "content", "Content & Social Media"
        TECHNOLOGY = "technology", "Technology"
        PRODUCT = "product", "Product"
        HUMAN_RESOURCES = "hr", "Human Resources"
        FINANCE = "finance", "Finance"
        LEGAL = "legal", "Legal"
        BUSINESS_DEVELOPMENT = "business_development", "Business Development"

    role = models.CharField(max_length=100)
    summary = models.CharField(max_length=255)
    department = models.CharField(max_length=20,choices=Department_Type.choices,default=Department_Type.ASTROLOGY)
    description = models.TextField()
    vacancies = models.PositiveIntegerField(default=1)
    location = models.CharField(max_length=100,default='Noida Sec 59 ,Uttar Pradesh')
    min_exp = models.PositiveIntegerField(default=0)
    max_exp = models.PositiveIntegerField(default=0)
    edu_requirment = models.TextField()
    skill_requirment = models.TextField()
    min_salary = models.CharField(max_length=50, blank=True, null=True)
    max_salary = models.CharField(max_length=50, blank=True, null=True)
    job_type = models.CharField(max_length=20,choices=JobType.choices,default=JobType.FULL_TIME)
    work_mode = models.CharField(max_length=20,choices=WorkMode.choices,default=WorkMode.ONSITE)
    job_post_date = models.DateTimeField(auto_now_add=True)
    end_apply_date = models.DateTimeField()
    status = models.CharField(max_length=20,choices=Status.choices,default=Status.ACTIVE)


    def __str__(self):
        return self.role