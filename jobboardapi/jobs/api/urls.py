from django.urls import path
from jobs.api.views import JobOfferListApiCreateView, JobOfferDetailAPIView


urlpatterns = [
    path("jobs/", JobOfferListApiCreateView.as_view(), name="joboffer-list"),
    path("jobs/<int:pk>/", JobOfferDetailAPIView.as_view(), name="joboffer-detail"),
]
