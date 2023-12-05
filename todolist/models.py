from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(default=date.today)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return f"({self.id}) {self.title}"