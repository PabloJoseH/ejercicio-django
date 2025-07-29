from django.db import models
from django.conf import settings
from django_countries.fields import CountryField
from django.urls import reverse

class Cheese(models.Model):
    name        = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    country     = CountryField(blank_label="selecciona país", blank=True)
    added_by    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Firmness(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified"
        SOFT = "soft", "Soft"
        SEMI_SOFT = "semi-soft", "Semi-Soft"
        SEMI_HARD = "semi-hard", "Semi-Hard"
        HARD = "hard", "Hard"

    firmness = models.CharField("Firmness", max_length=20, choices=Firmness.choices, default=Firmness.UNSPECIFIED)


    def __str__(self):
        return f"{self.name} ({self.country.name if self.country else '–'})"
    
    def get_absolute_url(self):
        return reverse("cheese_detail", kwargs={"pk": self.pk})

