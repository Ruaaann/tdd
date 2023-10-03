"""
Test Cases for Counter Web Service


Create a service that can keep a track of multiple counters
- API must be RESTful - see the status.py file. Following these guidelines, you can make assumptions about
how to call the web service and assert what it should return.
- The endpoint should be called /counters
- When creating a counter, you must specify the name in the path.
- Duplicate names must return a conflict error code.
- The service must be able to update a counter by name.
- The service must be able to read the counter
"""
from unittest import TestCase

# we need to import the unit under test - counter
from src.counter import app

# we need to import the file that contains the status codes
from src import status

class CounterTest(TestCase):
    """Counter tests"""
    def setUp(self):
        self.client = app.test_client()


    def test_create_a_counter(self):
        """It should create a counter"""
        client = app.test_client()
        result = client.post('/counters/foo')
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)


    def test_duplicate_a_counter(self):
        """It should return an error for duplicates"""
        result = self.client.post('/counters/bar')
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        result = self.client.post('/counters/bar')
        self.assertEqual(result.status_code, status.HTTP_409_CONFLICT)


    def test_update_a_counter(self):
        """It should update a counter"""
        # create a counter
        client = app.test_client()
        result = client.post('/counters/foob')
        # ensure successful return code
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        # Check the counter value as a baseline?
        baseline_val = result.get_json()['foob']
        # Make a call to update the counter that was created
        result = client.put('/counters/foob')
        # Ensure return successful return code
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        # Check that counter value is one more than the baseline you measured
        # in step 3
        self.assertGreater(result.get_json()['foob'], baseline_val)


    def test_read_counter(self):
        """It should read a counter"""
        client = app.test_client()
        result = client.get('/counters/foo')
        # ensure successful return code for GET
        self.assertEqual(result.status_code, status.HTTP_200_OK)
