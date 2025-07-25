# Generated by Django 5.2.4 on 2025-07-08 20:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'Профиль пользователя', 'verbose_name_plural': 'Профили пользователей'},
        ),
        migrations.AddField(
            model_name='users',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Аккаунт Django'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='description',
            field=models.TextField(blank=True, verbose_name='Характеристика'),
        ),
        migrations.AlterField(
            model_name='users',
            name='interview_count_passed',
            field=models.IntegerField(default=0, verbose_name='Количество пройденных собеседований'),
        ),
        migrations.AlterField(
            model_name='users',
            name='interview_count_taken',
            field=models.IntegerField(default=0, verbose_name='Проведённые собеседования'),
        ),
        migrations.AlterField(
            model_name='users',
            name='negative_results',
            field=models.IntegerField(default=0, verbose_name='Неудачные собеседования'),
        ),
        migrations.AlterField(
            model_name='users',
            name='positive_results',
            field=models.IntegerField(default=0, verbose_name='Успешные собеседования'),
        ),
        migrations.AlterField(
            model_name='users',
            name='type',
            field=models.CharField(choices=[('HR', 'сотрудник отдела кадров'), ('candidate', 'кандидат'), ('admin', 'администратор')], default='candidate', max_length=20, verbose_name='Тип пользователя'),
        ),
    ]
