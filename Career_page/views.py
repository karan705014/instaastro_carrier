from pstats import Stats

from django.contrib import messages
from .models import Job
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .forms import JobApplicationForm



# for display all job and also the search data 
def ListAPI(request):
    data = Job.objects.filter(status=Job.Status.ACTIVE).order_by("-job_post_date")
    search = request.GET.get("q", "").strip()
    # Get department filter
    department = request.GET.get("department", "").strip()

    if search:
        words = search.split()

        # AND between words
        for word in words:
            data = data.filter(
                Q(role__icontains=word)
                | Q(summary__icontains=word)
                | Q(description__icontains=word)
                | Q(skill_requirment__icontains=word)
            )

    if department:
            data = data.filter(department=department)

    paginator = Paginator(data, 6) # 6 jobs per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number) 
    context = {
        "jobs": page_obj,
        "page_obj": page_obj,
        "search": search,
        "department": department,
        "departments": Job.Department_Type.choices,
    }
    return render(request, "homepage.html", context)


#for details data of job
def Job_Detail(request, id):
    job = get_object_or_404(Job, id=id)
    return render(request, "jobdetail.html", {"job": job})
 
def Job_Apply(request, id):
    job = get_object_or_404(Job, id=id)

    if request.method == "POST":
        form = JobApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()

            messages.success(
                request,
                "Your application has been submitted successfully!"
            )

            return redirect("job_detail", id=job.id)

    else:
        form = JobApplicationForm()

    return render(request, "jobapply.html", {
        "job": job,
        "form": form
    })