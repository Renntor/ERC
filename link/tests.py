from django.urls import reverse
from link.models import Link
from users.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework import status


class LinkTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.com', password='test', is_active=True)
        self.client.force_authenticate(user=self.user)

        self.link = Link.objects.create(
            name='name_test',
            contact='contact_test',
            email='test@test.test',
            country='country_test',
            city='city_test',
            street='street_test',
            number='10',
            house='house_test',
            structure='FC',
            owner=self.user
        )

    def test_create_link(self):
        response = self.client.post(
            reverse('link:list_create_link'),
            data={
                'name': 'name_test_IE',
                "contact": 'contact_test_IE',
                "email": 'test@test.test',
                "country": "country_test_IE",
                "city": 'city_test_IE',
                "street": 'street_test_IE',
                "number": '1',
                "house": 'house_test_IE',
                "debt": 9.0,
                "structure": 'IE',
                "supplier": self.link.id
            }
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {'id': response.json()['id'], 'name': 'name_test_IE', 'contact': 'contact_test_IE',
             'email': 'test@test.test', 'country': 'country_test_IE', 'city': 'city_test_IE',
             'street': 'street_test_IE', 'number': '1', 'house': 'house_test_IE', 'debt': 9.0,
             'create': response.json()['create'], 'structure': 'IE', 'supplier': self.link.id}

        )

    def test_list_link(self):
        response = self.client.get(
            reverse('link:list_create_link'),
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            response.json(),
            [{'id': self.link.id, 'name': 'name_test', 'contact': 'contact_test',
              'email': 'test@test.test', 'country': 'country_test', 'city': 'city_test',
              'street': 'street_test', 'number': '10', 'house': 'house_test', 'debt': 0.0,
              'create': response.json()[0]['create'], 'structure': 'FC', 'supplier': None}]
        )

    def test_update_link(self):
        response = self.client.patch(
            reverse('link:retrieve_update_destroy_link', kwargs={'pk': self.link.id}),
            {'name': "new_name"}
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'id': self.link.id, 'name': 'new_name', 'contact': 'contact_test',
             'email': 'test@test.test', 'country': 'country_test', 'city': 'city_test',
             'street': 'street_test', 'number': '10', 'house': 'house_test', 'debt': 0.0,
             'create': response.json()['create'], 'structure': 'FC', 'supplier': None}
        )

    def test_detail_link(self):
        response = self.client.get(
            reverse('link:retrieve_update_destroy_link', kwargs={'pk': self.link.id})
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'id': self.link.id, 'name': 'name_test', 'contact': 'contact_test',
             'email': 'test@test.test', 'country': 'country_test', 'city': 'city_test',
             'street': 'street_test', 'number': '10', 'house': 'house_test', 'debt': 0.0,
             'create': response.json()['create'], 'structure': 'FC', 'supplier': None}
        )


    def test_destroy_link(self):
        response = self.client.delete(
            reverse('link:retrieve_update_destroy_link', kwargs={'pk': self.link.id}),
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
