# Generated by Django 2.2.7 on 2019-12-10 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tableros', '0003_auto_20191210_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabled',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tabled',
            name='dueno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dueno', to=settings.AUTH_USER_MODEL),
        ),
    ]
