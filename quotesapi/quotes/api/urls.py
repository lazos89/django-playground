from django.urls import path
from quotes.api.views import QuoteDetailAPIView, QuoteListAPIView

urlpatterns = [
    path("quotes/", QuoteListAPIView.as_view(), name="quote-list"),
    path("quotes/<int:pk>/", QuoteDetailAPIView.as_view(), name="quote-detail"),
]

