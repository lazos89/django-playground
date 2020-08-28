from django.db import models


class JobOffer(models.Model):
    """Model definition for JobOffer."""

    company_name = models.CharField(max_length=60)
    company_email = models.EmailField()
    job_title = models.CharField(max_length=60)
    job_description = models.TextField()
    salary = models.PositiveIntegerField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True)
    avaliable = models.BooleanField(default=True)

    class Meta:
        """Meta definition for JobOffer."""

        verbose_name = "JobOffer"
        verbose_name_plural = "JobOffers"

    def __str__(self):
        """Unicode representation of JobOffer."""
        return f"{self.job_title} | {self.company_name}"


# Create your models here.
