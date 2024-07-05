from django.test import TestCase
from django.contrib.auth.models import User
from .models import Job, Company

class JobListingTests(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name='Test Company', description='A test company')
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.job = Job.objects.create(title='Test Job', company=self.company, description='A test job')

    def test_create_job(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post('/jobs/create/', {
            'title': 'New Job',
            'company': self.company.id,
            'description': 'A new job'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Job.objects.filter(title='New Job').exists())

    def test_apply_job(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(f'/jobs/{self.job.id}/apply/', {
            'cover_letter': 'I would like to apply.'
        })
        self.assertEqual(response.status_code, 302)
        # Add further assertions based on your application logic
