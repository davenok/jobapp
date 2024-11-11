from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
#from django.template import loader
from datetime import datetime #, time

# Create your views here.

job_title = [
    "First Job",
    "Second Job",
     "Third Job" ]

job_description = [
    "First Job Description",
    "Second Job Description",
     "Third Job Description" ]


class TempClass:
    x = 5

def hello(request):
    #template = loader.get_template('app/hello.html') #pushing templates into sub folder "namespacing"
    now = datetime.now()
    list = ["alpha","bravo","charlie","delta"]
    temp = TempClass()
    is_authenticated = True
    context = {"name":"David", 
               "age":56,
               "time":now.time(),
               "first_list": list,
               "temp_object": temp, 
               "is_authenticated": is_authenticated }
    #return HttpResponse(template.render(context, request))
    return render(request, "app/hello.html", context) # replaces commented lines above

def job_list(request):
    context = {"job_titles":job_title}
    return render(request, "app/index.html", context)

def job_detail(request, id):
    try:
        if id == 0:
            return redirect(reverse('jobs_home'))
        # return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
        # return HttpResponse(return_html)
        context = {"job_title":job_title[id], "job_description":job_description[id]}
        return render(request, "app/job_detail.html", context)
    except:
        return HttpResponseNotFound("Not found")