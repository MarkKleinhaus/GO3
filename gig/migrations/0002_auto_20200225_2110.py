# Generated by Django 3.0.3 on 2020-02-26 02:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gig', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gig',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contact_gigs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gig',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_gigs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gig',
            name='leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leader_gigs', to=settings.AUTH_USER_MODEL),
        ),
    ]
