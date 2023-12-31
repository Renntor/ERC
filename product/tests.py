from django.urls import reverse
from link.models import Link
from product.models import Product
from users.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework import status


class ProductTestCase(APITestCase):

    def setUp(self):
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
        self.product = Product.objects.create(
            link=self.link,
            name='test_product',
            model='test_model',
            release_date='1990-12-01'
        )

    def test_create_product(self):
        response = self.client.post(
            reverse('product:list_create_product'),
            {
                "link": self.link.id,
                'name': "product",
                "model": "model_product",
                "release_date": '2012-02-11'
            }
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {
                "link": self.link.id,
                'name': "product",
                "model": "model_product",
                "release_date": '2012-02-11'
            }
        )

    def test_list_product(self):
        response = self.client.get(
            reverse('product:list_create_product')
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            [{
                "link": self.link.id,
                'name': "test_product",
                "model": "test_model",
                "release_date": '1990-12-01'
            }]
        )

    def test_delete_product(self):
        response = self.client.delete(
            reverse('product:retrieve_update_destroy_product', kwargs={'pk': self.product.id})
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_update_product(self):
        response = self.client.patch(
            reverse('product:retrieve_update_destroy_product', kwargs={'pk': self.product.id}),
            {"name": "new"}
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            response.json(),
            {
                "link": self.link.id,
                'name': "new",
                "model": "test_model",
                "release_date": '1990-12-01'
            }
        )

    def test_detail_product(self):
        response = self.client.get(
            reverse('product:retrieve_update_destroy_product', kwargs={'pk': self.product.id})
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            response.json(),
            {
                "link": self.link.id,
                'name': "test_product",
                "model": "test_model",
                "release_date": '1990-12-01'
            }
        )
