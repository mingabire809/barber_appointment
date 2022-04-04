from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'member'

urlpatterns = [
    path('signup/', csrf_exempt(views.RegisterMemberView.as_view())),
    path('<username>/', views.MemberView.as_view({'get': 'retrieve',
                                                  'patch': 'update',
                                                  'delete': 'destroy'})),

]
