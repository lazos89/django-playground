from rest_framework import serializers

from ebooks.models import Ebook, Review


class ReviewSerializer(serializers.ModelSerializer):
    """Model definition for ReviewSerializer."""

    review_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        """Meta definition for ReviewSerializer."""

        model = Review
        exclude = ("ebook",)
        # fields = "__all__"


class EbookSerializer(serializers.ModelSerializer):
    """Model definition for ReviewSerializer."""

    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        """Meta definition for ReviewSerializer."""

        model = Ebook
        fields = "__all__"
