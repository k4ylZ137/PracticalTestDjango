from django.contrib import admin
from django.urls import path
from django.urls import include
from catsandstudents import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'catsandstudents'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
