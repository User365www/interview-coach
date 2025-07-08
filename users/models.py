from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICES = [
        ('HR', 'сотрудник отдела кадров'),
        ('candidate', 'кандидат'),
        ('admin', 'администратор'),
    ]


class Users(models.Model):
    """Профиль пользователя, связанный со стандартной моделью User"""
    name = models.CharField("Имя и фамилия", max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name="Аккаунт Django")
    type = models.CharField("Тип пользователя", max_length=20, choices=STATUS_CHOICES, default='candidate')
    description = models.TextField("Характеристика", blank=True)
    interview_count_passed = models.IntegerField("Количество пройденных собеседований", default=0)
    positive_results = models.IntegerField("Успешные собеседования", default=0)
    negative_results = models.IntegerField("Неудачные собеседования", default=0)
    interview_count_taken = models.IntegerField("Проведённые собеседования",default=0)

    def __str__(self):
        return f"{self.user.username} ({self.get_type_display()})"

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"