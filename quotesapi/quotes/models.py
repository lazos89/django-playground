from django.db import models


class Quote(models.Model):
    """Model definition for Quote."""

    quote_author = models.CharField(max_length=50)
    quote_body = models.TextField()
    context = models.CharField(max_length=240, blank=True)
    source = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Unicode representation of Quote."""
        return self.quote_author
