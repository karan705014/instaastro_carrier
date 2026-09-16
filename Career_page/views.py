from rest_framework.views import APIView
from .models import Job
from .serializers import JobSerializer
from rest_framework.response import Response
def filter_jobs(queryset, request, allow_status=False):
    search = request.query_params.get("search")
    location = request.query_params.get("location")
    department = request.query_params.get("department")
    job_type = request.query_params.get("job_type")
    work_mode = request.query_params.get("work_mode")
    if search:
        queryset = queryset.filter(role__icontains=search)
    if location:
        queryset = queryset.filter(location__icontains=location)
    if department:
        queryset = queryset.filter(department=department)
    if job_type:
        queryset = queryset.filter(job_type=job_type)
    if work_mode:
        queryset = queryset.filter(w_mode=work_mode)
    if allow_status:
        status = request.query_params.get("status")
        if status:
            queryset = queryset.filter(status=status)
    return queryset
class ListAPI(APIView):
    def get(self, request):
        jobs = Job.objects.filter(status=Job.Status.ACTIVE)
        jobs = filter_jobs(jobs,request)
        serializer = JobSerializer(jobs,many=True)
        return Response(serializer.data)
class DetailAPI(APIView):
    def get(self, request, pk):
        try:
            job=Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            return Response({"error":"Job Not Found"},status=404)
        serializer = JobSerializer(job)
        return Response(serializer.data)
class AdminJobAPI(APIView):
    def get(self, request):
        jobs = Job.objects.all()
        jobs = filter_jobs(jobs,request,allow_status=True)
        serializer = JobSerializer(jobs,many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
class AdminJobDetailAPI(APIView):
    def get(self, request, pk):
        try:
            job = Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            return Response({"error": "Job Not Found"},status=404)
        serializer = JobSerializer(job)
        return Response(serializer.data)
    def put(self, request, pk):
        try:
            job = Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            return Response({"error": "Job Not Found"},status=404)
        serializer = JobSerializer(job,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
    def delete(self, request, pk):
        try:
            job = Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            return Response({"error": "Job Not Found"},status=404)
        job.delete()
        return Response({"message": "Job deleted successfully"},status=204)