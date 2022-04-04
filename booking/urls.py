from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.BookingListView.as_view({'get': 'get',
                                                    'post': 'post',

                                                    })),
    path('booking/<str:pk>/', views.BookingDetails.as_view({'get': 'retrieve',
                                                            'patch': 'update',
                                                            'delete': 'destroy'}))

]
