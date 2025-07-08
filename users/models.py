from django.db import models

STATUS_CHOICES = [
        ('HR', 'сотрудник отдела кадров'),
        ('candidate', 'кандидат'),
    ]

class Users(models.Model):
    """Пользователи"""
    name = models.CharField("Имя и фамилия", max_length=100)
    description = models.TextField("Характеристика")
    type = models.CharField("Тип пользователя", choices=STATUS_CHOICES, default='кандидат')
    interview_count_passed= models.IntegerField("Количество пройденных собеседований на сайте", default=0)
    positive_results = models.IntegerField("Количество положительно пройденных собеседований на сайте", default=0)
    negative_results = models.IntegerField("Количество отрицательно пройденных собеседований на сайте", default=0)
    interview_count_taken = models.IntegerField("Количество проведённых собеседований на сайте", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"