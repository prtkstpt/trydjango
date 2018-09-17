from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print('>>>', request, request.user)
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact Page</h1>")
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    # return HttpResponse("<h1>About Page</h1>")
    my_context = {
        "my_name": "ppppp",
        "my_age": 25,
        "my_list": [111, 222, 333]
    }
    return render(request, "about.html", my_context)
