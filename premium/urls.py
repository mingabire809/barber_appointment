from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('premium/', views.PremiumView.as_view({
        'get': 'get',
        'post': 'post'

    })),
    path('premium/<str:pk>/', views.PremiumDetails.as_view({
        'get': 'get',
        'patch': 'patch',
        'delete': 'delete',
    })),
]

urlpatterns = format_suffix_patterns(urlpatterns)
