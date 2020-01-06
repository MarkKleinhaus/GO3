# Generated by Django 3.0 on 2020-01-05 23:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gig', '0004_auto_20200105_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gig',
            name='leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leader_gigs', to=settings.AUTH_USER_MODEL),
        ),
    ]