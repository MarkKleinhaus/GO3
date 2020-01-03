# Generated by Django 3.0 on 2019-12-30 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('band', '0006_auto_20191227_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('order', models.IntegerField(default=0)),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='band.Band')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]