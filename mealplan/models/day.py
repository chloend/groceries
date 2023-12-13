from django.db import models


class Day(models.Model):
    day = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.day}"
