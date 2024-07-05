from django.db import models  # type: ignore
from django.contrib.auth import get_user_model  # type: ignore

class Application(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE)
    applicant = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.applicant.username} - {self.job.title}"
