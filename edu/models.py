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
    duration = models.IntegerField(default=1, help_text='Number of days, Number of weeks etc.', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Subscription(TimeStampedModel):
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    user = models.ForeignKey('core.User', on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    quantity = models.IntegerField(default=1, help_text='Number of Unlocks, Number of Upvotes etc.', blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.bot} - {self.organization}'


class Assignment(TimeStampedModel):
    user = models.ForeignKey('core.User', on_delete=models.CASCADE)

    name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='assignment_images')
    price = models.PositiveIntegerField(default=0, blank=True, null=True)
    upload_file = models.FileField(upload_to='ask_assignments', null=True, blank=True)
    question_text = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name




