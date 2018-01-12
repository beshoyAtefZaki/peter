from django.db import models

# Create your models here.

class item (models.Model):
    fi = models.FileField(upload_to="peter/")

    def __str__(self):
        return self.id
