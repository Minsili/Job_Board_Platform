from django.db import models
from django.contrib.auth import get_user_model
from apps.companies.models import Company

STATUS_CHOICES = [
    ('open', 'Open'),
    ('closed', 'Closed'),
    ('pending', 'Pending')
] 

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
    salary = models.CharField(max_length=100, default='Not specified')
    location = models.CharField(max_length=255, default='Not specified')
    requirements = models.TextField(default='Not specified')

    def __str__(self):
        return self.title

    def view_applications(self):
        from applications.models import Application  # Import locally
        return Application.objects.filter(job=self)

