from django.db import models

# Create your models here.

class Artiles(models.Model):
    title = models.CharField('Назва', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('стаття')
    date=models.DateTimeField('Дата публікації')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'