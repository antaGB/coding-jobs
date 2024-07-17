from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('application/<int:application_id>', views.view_application, name='application'),
]