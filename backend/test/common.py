from django.test import TestCase

class TestingMixin(TestCase):
    def setUp(self):
        """
        Action to run before each unit test begins.
        """ 
        pass

    def tearDown(self) -> None:
        """
        Action to run after each unit test completes.
        """ 
        pass