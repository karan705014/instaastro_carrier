from django.contrib import messages
from .models import Job
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .forms import JobApplicationForm



# for display all job
def ListAPI(request):
    data = Job.objects.all()    
    context = {
        'jobs': data  
    }
    return render(request, "homepage.html", context)


# for display search data
def Job_List(request):
    jobs = Job.objects.all()
    search = request.GET.get("q", "").strip()
    if search:
        words = search.split()
        query = Q()
        for word in words:
            query = query | (
                Q(role__icontains=word)
                | Q(department__icontains=word)
                | Q(location__icontains=word)
                | Q(skill_requirment__icontains=word)
            )
        jobs = jobs.filter(query).distinct()
    return render(request, "searchoutput.html",{"jobs": jobs})


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