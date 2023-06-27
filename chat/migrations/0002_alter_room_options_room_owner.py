# Generated by Django 4.1.9 on 2023-06-20 09:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-pk']},
        ),
        migrations.AddField(
            model_name='room',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='owned_room_set', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
