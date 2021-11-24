# Generated by Django 3.0.3 on 2020-04-02 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='like', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
