from django.test import TestCase
# Create your tests here.
class HomeTest(TestCase):
    def setUp(self):
        a = 5
        b = 10
    def tearDown(self):
        a,b= 0
    def test_Maps(self):
        return self.assertEqual(self.a+ self.b, 15 )