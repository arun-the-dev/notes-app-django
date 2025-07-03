"""
URL configuration for notesappproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_control

from notesapp.views import UserCreateView,UserUpdateView
# Here we set login ,register ,logout viewssand urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("notesapp.urls")),
    path("login/", cache_control(no_cache=True, must_revalidate=True, no_store=True)(
            LoginView.as_view(template_name="auth/login.html")
        ),name="login"),
    path("logout/",LogoutView.as_view(next_page = "login"),name='logout'),
    path("register/",UserCreateView.as_view(),name="register"),
    path("account/update/",UserUpdateView.as_view(),name="user-update")

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
