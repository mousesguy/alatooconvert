from django.db import models

class Document(models.Model):
    document = models.FileField(upload_to='documents/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.description