from django.db import models


class PublishedModel(models.Model):
    is_published = models.BooleanField('Опубликовано', default=True)

    class Meta:
        abstract = True
