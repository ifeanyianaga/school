from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    template_name ='base.html'
    return render(request,template_name)


def loginpage(request):
    template_name ="login.html"
    return render(request,template_name)




def signup(request):
    template_name ="signup.html"
    return render(request,template_name)


def tutoring(request):
    template_name ="tutoring.html"
    return render(request,template_name)



def about(request):
    template_name="about.html"
    return render(request,template_name)


def contact(request):
    template_name="contact.html"
    return render(request,template_name)

    
def dashboard(request):
    template_name="dashboard.html"
    return render(request,template_name)

def admin_dashboard(request):
    template_name="dashboard-admin.html"
    return render(request,template_name)

def terms(request):
    template_name="terms.html"
    return render(request,template_name)


