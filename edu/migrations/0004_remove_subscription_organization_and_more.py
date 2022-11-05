# Generated by Django 4.0.6 on 2022-11-05 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_organization_image'),
        ('edu', '0003_plan_subscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='organization',
        ),
        migrations.AlterField(
            model_name='plan',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.organization'),
        ),
    ]