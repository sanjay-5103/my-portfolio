from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Certification(models.Model):
    name = models.CharField(max_length=100)
    issued_by = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    certificate = models.FileField(upload_to='certificates/', blank=True)

    def __str__(self):
        return f"{self.name} - {self.issued_by}"