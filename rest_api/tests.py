import datetime

from django.test import TestCase
from django.urls import reverse
from django.core.management import call_command
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Home


TEST_DATA = {
    "home_type": "SingleFamily",
    "address": "123 Test St",
    "city": "West Hills",
    "state": "CA",
    "zipcode": "90210",
    "price": "$2.5M",
    "bedrooms": 4,
    "home_size": 1372,
    "property_size": 10611,
    "year_built": 1956,
    "zillow_id": 19866015,
    "link": "https://www.zillow.com/homedetails/7417-Quimby-Ave-West-Hills-CA-91307/19866015_zpid/",
    "zestimate_amount": 709630,
    "zestimate_last_updated": "2018-08-07",
    "rentzestimate_amount": 2850,
    "rentzestimate_last_updated": "2018-08-07",
    "tax_year": 2017,
    "tax_value": 215083,
}


class HomeModelTest(TestCase):
    def test_model_defaults(self):
        """
        Verify that defaults are set as well as omission of nullable fields
        """
        home = Home(
          home_type='SingleFamily',
          address='123 Test St',
          city='Beverly Hills',
          state='CA',
          zipcode='90210',
          price='$2.5M',
          bedrooms='5',
          home_size=123,
          property_size=1234,
          year_built=1950,
          zillow_id='123456',
          link='https://www.zillow.com/homedetails/123-Test-St-Beverly-Hills-CA-90210/123456_zpid/',
          tax_year=2017,
          tax_value=10000
        )
        self.assertEqual(home.area_unit, 'SqFt')
        self.assertEqual(home.zestimate_last_updated, datetime.date(1970, 1, 1))
        self.assertEqual(home.rentzestimate_last_updated, datetime.date(1970, 1, 1))


class HomeAPITests(APITestCase):

    def test_create_home(self) -> None:
        """
        Test POST requests to create new home
        """
        url = reverse('homes')
        response = self.client.post(url, TEST_DATA, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Home.objects.count(), 1)

    def test_list_homes(self) -> None:
        """
        Test GET req for all homes
        """
        test_home = Home(**TEST_DATA)
        test_home.save()
        url = reverse('homes')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.data[0]
        [self.assertEqual(response_data[key], value) for key, value in TEST_DATA.items()]

    def test_update_home(self):
        """
        Test updating a home's data via PUT req
        """
        test_home = Home(**TEST_DATA)
        test_home.save()
        url = reverse('home-by-id', args=[test_home.id])
        new_data = TEST_DATA.copy()
        new_data['rent_price'] = 500
        response = self.client.put(url, new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Home.objects.get(id=test_home.id).rent_price, 500)

    def test_get_home(self):
        """
        Test fetching a home's data via GET req
        """
        test_home = Home(**TEST_DATA)
        test_home.save()
        url = reverse('home-by-id', args=[test_home.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.data
        [self.assertEqual(response_data[key], value) for key, value in TEST_DATA.items()]

    def test_delete_home(self):
        """
        Test removal of a home via DELETE req
        """
        test_home = Home(**TEST_DATA)
        test_home.save()
        url = reverse('home-by-id', args=[test_home.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Home.objects.count(), 0)


class IngestCSVTest(TestCase):
    def test_ingest_csv_command(self):
        """
        Minimal test for ingestcsv command.
        Basically just makes sure it runs without exceptions and writes to db.
        """
        # test file contains sample data truncated to first 3 elements
        call_command('ingestcsv', file='rest_api/resources/sample_test.csv')
        self.assertEqual(Home.objects.count(), 3)
