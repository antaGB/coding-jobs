from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_job, name='add_job'),
    path('<int:job_id>/', views.job_detail, name='job_detail'),
    # Add other URL patterns here
]