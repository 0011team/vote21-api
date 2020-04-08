from rest_framework.routers import DefaultRouter
from django.urls import path
# from rest_framework_nested.routers import NestedSimpleRouter

from .views import DistrictView, AdressView

urlpatterns = [
    path('districts/', DistrictView.as_view()),
    path('address/', AdressView.as_view()),
]



