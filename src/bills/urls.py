from rest_framework.routers import DefaultRouter
from django.urls import path,re_path
from .views import BillDetailView, BillListView

urlpatterns = [
    path('bills/20', BillListView.as_view()),
    re_path(r'bills/20/(?P<bill_id>\w+)/$', BillDetailView.as_view()),
]