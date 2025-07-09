from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
STATUS_CHOICES = [
        ('waiting', 'Ожидает рассмотрения'),
        ('accepted', 'Принято'),
        ('ended successfully', 'закончилось успешно'),
        ('ended unsuccessfully', 'закончилось безуспешно'),
    ]


class Request(models.Model):
    '''Запросы на собеседование'''
    candidate = models.ForeignKey(User, on_delete=models.CASCADE, related_name='candidate_requests', verbose_name='Кандидат')
    hr = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='hr_requests', blank=True, verbose_name='HR менеджер')
    description = models.TextField('Описание запроса')
    status = models.CharField('Статус', choices=STATUS_CHOICES, default='waiting')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True, null=True)
    interview_time = models.DateTimeField('Время собеседования', null=True, blank=True)

    class Meta:
        verbose_name = 'Запрос на собеседование'
        verbose_name_plural = 'Запросы на собеседование'
        ordering = ['-created_at']

    def __str__(self):
        return f"Запрос #{self.id} от {self.candidate}"