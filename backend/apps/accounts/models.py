from django.contrib.auth.models import AbstractUser # type: ignore
from django.db import models # type: ignore
from django.conf import settings

class Role(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class UserAccount(AbstractUser):
    roles = models.ManyToManyField(Role, related_name='users')  # Adjusted related_name

    class Meta:
        # Ensure this model is linked to the correct app_label
        app_label = 'accounts'

    # Add related_name to avoid clashes with auth.User's groups
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set',  # Example: change related_name to avoid clash
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    # Add related_name to avoid clashes with auth.User's user_permissions
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set',  # Example: change related_name to avoid clash
        help_text='Specific permissions for this user.',
    )

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('jobseeker', 'Jobseeker'),
        ('employer', 'Employer'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='jobseeker')
    roles = models.ManyToManyField(Role, related_name='custom_users')

    def __str__(self):
        return self.username
    
class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message