from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import LawmakerView, LawmakerPushView, LawmakerSummaryView, CandidateView

urlpatterns = [
    path('lawmakers/20/', LawmakerView.as_view()),
    path('lawmakers/20/modify', LawmakerPushView.as_view()),
    path('lawmakers/summaries', LawmakerSummaryView.as_view()),
    path('lawmakers/21/candidate', CandidateView.as_view())
]