from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('membership/', views.MembershipView.as_view({
        'get': 'get',
        'post': 'post'

    })),
    path('membership/<str:pk>/', views.MembershipDetails.as_view({
        'get': 'get',
        'patch': 'patch',
        'delete': 'delete',
    })),
]

urlpatterns = format_suffix_patterns(urlpatterns)