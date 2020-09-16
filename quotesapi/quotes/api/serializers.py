from rest_framework import serializers
from quotes.models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    """Model definition for QuoteSerilizer."""

    class Meta:
        model = Quote
        fields = "__all__"

