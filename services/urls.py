from django.urls import path
from . import views

#app_name = 'services'

urlpatterns = [
    path('haircut/', views.HaircutView.as_view()),
    path('haircut/<str:pk>/', views.HairCutDetails.as_view()),
    path('extra_services/', views.ExtraServiceView.as_view()),
    path('extra_services/<str:pk>/', views.ExtraServiceDetails.as_view()),


]
