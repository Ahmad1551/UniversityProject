# Generated by Django 4.0.6 on 2022-11-05 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_organization_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('edu', '0002_rename_is_verifies_bot_is_verified'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField(blank=True, default=1, help_text='Number of Unlocks, Number of Upvotes etc.', null=True)),
                ('duration', models.IntegerField(blank=True, default=1, help_text='Number of days, Number of weeks etc.', null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_popular', models.BooleanField(default=False)),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edu.bot')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(blank=True, default=1, help_text='Number of Unlocks, Number of Upvotes etc.', null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('paid_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edu.bot')),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.organization')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edu.plan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]