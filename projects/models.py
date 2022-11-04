from django.db import models

from config.mixins import TimeStampedModel


class Organization(TimeStampedModel):
    name = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, null=True, blank=True)
    about_link = models.URLField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
