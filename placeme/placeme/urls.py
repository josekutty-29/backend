"""
URL configuration for placeme project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include  # <-- include must be imported here
from main.views import signup,login_view,student_dashboard, tutor_dashboard,admin_dashboard,logout_view,student_register
from django.shortcuts import redirect 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')), 
    path('signup/', signup, name='signup'),
    path('', lambda request: redirect('signup/')),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('student_register/', student_register, name='student_register'),
    path('student_dashboard/', student_dashboard, name='student_dashboard'),
    path('tutor_dashboard/', tutor_dashboard, name='tutor_dashboard'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
  #  path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    # Optionally, set home to redirect to dashboard
    path('', login_view, name='home'),
    
]
