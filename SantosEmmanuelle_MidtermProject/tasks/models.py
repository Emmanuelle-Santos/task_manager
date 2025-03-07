from django.db import models
from datetime import date

class Task(models.Model):
    STATUS_PENDING = 'Pending'
    STATUS_OVERDUE = 'Overdue'
    STATUS_COMPLETED = 'Completed'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_OVERDUE, 'Overdue'),
        (STATUS_COMPLETED, 'Completed'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(null=True, blank=True)  
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING, editable=False
    )

    def save(self, *args, **kwargs):
        """Automatically update status based on due date before saving."""
        if self.due_date and self.status != self.STATUS_COMPLETED:
            
            if isinstance(self.due_date, str):
                from datetime import datetime
                self.due_date = datetime.strptime(self.due_date, "%Y-%m-%d").date()

            self.status = self.STATUS_OVERDUE if self.due_date < date.today() else self.STATUS_PENDING

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.status}"
