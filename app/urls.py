from django.urls import path
from app import views 

urlpatterns = [
    path('Sponsor-list/', views.SponsorListAPIView.as_view()),
    path('Sponsor-create/', views.SponsorCreateAPIView.as_view()),
    path('Sponsor-update/<int:pk>/', views.SponsorUpdateAPIView.as_view()),
    path('Sponsor-destroy/<int:pk>/', views.SponsorDestroyAPIView.as_view()),
    path('Talaba-list/', views.TalabaListAPIView.as_view()),
    path('Talaba-list/<int:pk>/', views.TalabaDetailAPIView.as_view()),
    path('Talaba-create/', views.TalabaCreateAPIView.as_view()),
    path('Talaba-update/<int:pk>/', views.TalabaUpdateAPIView.as_view()),
    path('Talaba-destroy/<int:pk>/', views.TalabaDestroyAPIView.as_view()),
    path('SponsorStudent-list/', views.SponsorStudentListAPIView.as_view()),
    path('SponsorStudent-create/', views.SponsorStudentCreateAPIView.as_view()),
    path('SponsorStudent-update/<int:pk>/', views.SponsorStudentUpdateAPIView.as_view()),
    path('SponsorStudent-destroy/<int:pk>/', views.SponsorStudentDestroyAPIView.as_view()),
    path('University-create/', views.UniversityCreateAPIView.as_view()),
    path('amount-statictic/', views.StaticticAPIView.as_view()),
    path('amount-statictic-list/', views.StaticticAPIView.as_view()),
    path('SponsorStudents-list/', views.StudentSponsorlistAPIView.as_view()),
]