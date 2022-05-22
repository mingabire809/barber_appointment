from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('payment/', views.PaymentView.as_view({
        'get': 'get',
        'post': 'post'

    })),
    path('payment/<str:pk>/', views.PaymentDetails.as_view({
        'get': 'get',
        'patch': 'patch',
        'delete': 'delete',
    })),
]

urlpatterns = format_suffix_patterns(urlpatterns)
