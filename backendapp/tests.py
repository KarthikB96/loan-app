from django.test import TestCase
from django.template.defaultfilters import slugify
from backendapp.models import Business,Address,Owners,ApplicationData
import json

class LoanTestCase(TestCase):
    def test_loan_false(self):
        x = {}
        response = self.client.post('/loanapp/',x,format = "json");
        self.assertEqual(response.status_code, 400)

    # def test_status_false(self):
    #     response = self.client.post('/loanapp/',);
    #     self.assertEqual(response.status_code, 200)

class StatusTestCase(TestCase):
    def test_status_false(self):
        response = self.client.get('/status/?filterId=');
        self.assertEqual(response.status_code, 400)

    # def test_status_true(self):
    #     response = self.client.get('/status/?filterId=89707');
    #     self.assertEqual(response.status_code, 200)



# Create your tests here.
class TestCase(TestCase):
    pass