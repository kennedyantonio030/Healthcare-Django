from django.urls import path
from . import views

urlpatterns = [
    path('', views.hospitalView.as_view(), name='hospital'),
    path('doctor/', views.DoctorListView.as_view(), name='doctor_team'),

    path('contact/', views.ContactView.as_view(), name='contact'),
]