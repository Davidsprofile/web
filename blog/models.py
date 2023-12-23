from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class News(models.Model):
    title = models.CharField('Article Name', max_length=100, unique=True)
    text = models.TextField('Main text of article')
    date = models.DateTimeField('Data', default=timezone.now)
    avtor = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE)

    views = models.IntegerField('Views', default=1)
    # sizes = (
    #     ('S', 'Small'),
    #     ('M', 'Medium'),
    #     ('L', 'Large'),
    #     ('XL', 'X large'),
    # )
    #
    # shop_sizes = models.CharField(max_length=2, choices=sizes, default='S')

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
