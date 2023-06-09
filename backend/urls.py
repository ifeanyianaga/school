from django.contrib import admin
from django.urls import path
from .views import homepage,loginpage,signup,tutoring,about,contact,dashboard,admin_dashboard,terms
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',homepage,name='home'),
    path('login/',loginpage,name='login'),
    path('signup/',signup,name='signup'),
    path('tutoring/',tutoring,name='tutoring'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('dashboard/',dashboard,name='dashboard'),
    path('admin_dashboard/',admin_dashboard,name='admin_dashboard'),
    path('terms/',terms,name='terms'),
    path('admin/', admin.site.urls),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
