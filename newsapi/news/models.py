from django.db import models


class Journalist(models.Model):
    """Model definition for Journalist."""

    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    biography = models.TextField(blank=True)

    class Meta:
        """Meta definition for Journalist."""

        verbose_name = "Journalist"
        verbose_name_plural = "Journalists"

    def __str__(self):
        """Unicode representation of Journalist."""
        return f"{self.first_name} {self.last_name}"


class Article(models.Model):
    author = models.ForeignKey(
        Journalist, on_delete=models.CASCADE, related_name="articles"
    )
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    body = models.TextField()
    location = models.CharField(max_length=120)
    publication_date = models.DateField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} {self.title}"
