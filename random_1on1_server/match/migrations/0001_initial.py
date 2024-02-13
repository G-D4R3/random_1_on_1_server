# Generated by Django 4.0 on 2024-02-13 05:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('start', models.DateField(help_text='usually monday')),
                ('end', models.DateField(help_text='usually friday')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('users', models.ManyToManyField(related_name='matches', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
