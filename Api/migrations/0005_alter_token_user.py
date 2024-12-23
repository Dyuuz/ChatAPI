# Generated by Django 5.0.7 on 2024-12-20 04:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0004_rename_model_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alltokens', to=settings.AUTH_USER_MODEL),
        ),
    ]
