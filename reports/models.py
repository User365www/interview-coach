from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
STATUS_CHOICES = [
        ('waiting', 'Ожидает рассмотрения'),
        ('done', 'Обработано'),
    ]


class Report(models.Model):
    '''Репорты на нарушения'''
    user_reporting = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports_made', verbose_name='Репортящий')
    user_reported = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='reports_received', blank=True, verbose_name='Репортируемый')
    admin = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='reports_done', blank=True, verbose_name='Админ')
    description = models.TextField('Описание конфликта')
    status = models.CharField('Статус', choices=STATUS_CHOICES, default='waiting')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True, null=True)

    class Meta:
        verbose_name = 'Репорт на нарушениe'
        verbose_name_plural = 'Репорты на нарушения'
        ordering = ['-created_at']

    def __str__(self):
        return f"Репорт #{self.id} от {self.user_reporting}"