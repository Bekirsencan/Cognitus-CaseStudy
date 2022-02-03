from django.db import models


class Data(models.Model):
    text = models.TextField()
    label = models.TextField()

    objects = models.Manager()
