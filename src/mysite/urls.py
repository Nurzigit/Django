"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path


from pages.views import (
    IndexHome,
    about_screen_view,
    AddPage,
    ShowPost,
)
from account.views import (
    registration_view,
    logout_view,
    login_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexHome.as_view(), name="home"),
    path('about/', about_screen_view, name="about"),
    path('addpage/', AddPage.as_view(), name="addpage"),
    path('post/', ShowPost.as_view(), name="post"),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
]
handler500 = 'pages.views.error500'
hander404 = 'pages.views.error_404'
handler403 = 'pages.views.error_403'
handler400 = 'pages.views.error_400'
