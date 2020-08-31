from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Ebook(models.Model):
    """Model definition for Ebook."""

    title = models.CharField(max_length=140)
    author = models.CharField(max_length=60)
    description = models.TextField()
    publication_date = models.DateField()

    class Meta:
        """Meta definition for Ebook."""

        verbose_name = "Ebook"
        verbose_name_plural = "Ebooks"

    def __str__(self):
        """Unicode representation of Ebook."""
        return self.title


class Review(models.Model):
    """Model definition for Review."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review_author = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(blank=True, null=True)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    ebook = models.ForeignKey(Ebook, on_delete=models.CASCADE, related_name="reviews")

    class Meta:
        """Meta definition for Review."""

        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        """Unicode representation of Review."""
        return f"{self.rating} | {self.review_author}"
