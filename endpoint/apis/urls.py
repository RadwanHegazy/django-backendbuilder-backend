from .views import get, create
from django.urls import path

urlpatterns = [
    path('get/user/<str:tenant>/<str:url_route>',get.user_endpoint.as_view()),
    path('get/user/all/',get.user_all_endpoints.as_view()),
    path('create/',create.create_endpoint.as_view()),
]