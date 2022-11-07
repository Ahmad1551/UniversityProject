import datetime

from django.db import models

from config.mixins import TimeStampedModel


class Bot(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='bot_images')
    is_active = models.BooleanField(default=True)
    is_online = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Plan(TimeStampedModel):
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    organization = models.ForeignKey('projects.Organization', on_delete=models.CASCADE, blank=True, null=True)

    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1, help_text='Number of Unlocks, Number of Upvotes etc.', blank=True, null=True)
    duration = models.IntegerField(default=1, help_text='Number of months i.e 1', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Subscription(TimeStampedModel):
    user = models.ForeignKey('core.User', on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    quantity = models.IntegerField(default=1, help_text='Number of Unlocks, Number of Upvotes etc.', blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_active = models.BooleanField(default=False)

    @property
    def is_expired(self):
        if self.end_date and self.end_date > datetime.date.today():
            return True
        return False

    @property
    def time_left(self):
        if self.end_date:
            return str(self.end_date - datetime.date.today()).split(',')[0]
        return None

    @property
    def duration_progress(self):
        progress = (self.end_date - datetime.date.today()).days * 100 / 30
        if progress < 0:
            if self.is_expired:
                return {'progress': 100, 'class': 'bg-success'}
            else:
                return {'progress': 100, 'class': 'bg-danger'}
        elif progress > 100:
            return {'progress': 0, 'class': 'bg-success'}
        elif progress < 30:
            return {'progress': 100 - progress, 'class': 'bg-danger'}
        elif progress < 60:
            return {'progress': 100 - progress, 'class': 'bg-success'}
        elif progress < 85:
            return {'progress': 100 - progress, 'class': 'bg-success'}
        elif progress < 100:
            return {'progress': 100 - progress, 'class': 'bg-success'}
        else:
            return {'progress': 0, 'class': 'bg-success'}

    def __str__(self):
        return self.plan.name
