from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
]
