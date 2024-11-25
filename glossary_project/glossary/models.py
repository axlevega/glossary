from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    domain = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Term(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    word = models.CharField(max_length=100)  # Убрали уникальность
    definition = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['project', 'word'], name='unique_project_word')
        ]  # Уникальность на уровне проекта
        verbose_name = 'Term'
        verbose_name_plural = 'Terms'

    def __str__(self):
        return self.word
