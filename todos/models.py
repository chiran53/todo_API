from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    STATUS_CHOICE = {
        ('pending', 'pending'),
        ('in_progress', 'In progress'),
        ('completed', 'completed'),
    }
    PRIORITY_CHOICE = {
        ('low', 'low'),
        ('medium', 'medium'),
        ('high', 'high'),
    }

    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='pending')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICE, default='low')
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
