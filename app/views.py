from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.

job_title = [
    "First Job",
    "Second Job",
     "Third Job" ]

job_description = [
    "First Job Description",
    "Second Job Description",
     "Third Job Description" ]




def job_list(request):
    return_html = "<ul>"
    for title in job_title:
        id = job_title.index(title)
        detail_url = reverse('jobs_detail', args = (id,))
        return_html += f"<li><a href='{detail_url}'>{title}</a></li>"
    return_html += "</ul>"
    return HttpResponse(return_html)

def job_detail(request, id):
    try:
        if id == 0:
            return redirect(reverse('jobs_home'))
        return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
        return HttpResponse(return_html)
    except:
        return HttpResponseNotFound("Not found")