# app/urls.py
from django.urls import path
from .views import SectionListCreateView, SectionDetailView, StudentListCreateView, StudentDetailView

urlpatterns = [
    path('sections/', SectionListCreateView.as_view(), name='section-list-create'),
    path('sections/<int:pk>/', SectionDetailView.as_view(), name='section-detail'),

    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
]
