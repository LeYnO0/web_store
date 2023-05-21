from django.db import models


class CatalogElements(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'
