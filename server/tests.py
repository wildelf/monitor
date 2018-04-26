from django.test import TestCase

# Create your tests here.

from server import models
models.Host.objects.create(machine_id='M-001',hostname='wilde')
