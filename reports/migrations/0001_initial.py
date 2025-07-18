# Generated by Django 5.2.4 on 2025-07-10 13:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание конфликта')),
                ('status', models.CharField(choices=[('waiting', 'Ожидает рассмотрения'), ('done', 'Обработано')], default='waiting', verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reports_done', to=settings.AUTH_USER_MODEL, verbose_name='Репортируемый')),
                ('user_reported', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='reports_received', to=settings.AUTH_USER_MODEL, verbose_name='Репортируемый')),
                ('user_reporting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports_made', to=settings.AUTH_USER_MODEL, verbose_name='Репортящий')),
            ],
            options={
                'verbose_name': 'Репорт на нарушениe',
                'verbose_name_plural': 'Репорты на нарушения',
                'ordering': ['-created_at'],
            },
        ),
    ]
