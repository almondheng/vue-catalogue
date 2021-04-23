from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient
import random
import decimal

from .models import Product, User
from vue_catalogue import settings

# Create your tests here.
class ProductTestCase(TestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser('admin', 'admin@admin.com', 'adminTestPassword')
        self.normal_user = User.objects.create_user('normal_user', 'normal_user@gmail.com', 'normalTestPassword')
        self.client = APIClient()

        for i in range(20):
            Product.objects.create(
                name=f'{i}-Product',
                price=f'{decimal.Decimal(random.randrange(155, 38967))/100}'
            )

    def test_cannot_list_products_without_auth(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, 401)

    # test admin
    def test_admin_can_list_all_products(self):
        self.client.force_authenticate(self.admin)
        response = self.client.get('/api/products/')
        self.assertContains(response, 'count')
        self.assertEqual(response.data['count'], 20)

    def test_admin_can_list_paginated_products(self):
        self.client.force_authenticate(self.admin)
        response = self.client.get('/api/products/')
        self.assertContains(response, 'results')
        self.assertEqual(len(response.data['results']), settings.REST_FRAMEWORK['PAGE_SIZE'])

    def test_admin_can_list_next_paginated_products(self):
        self.client.force_authenticate(self.admin)
        response = self.client.get('/api/products/')
        self.assertContains(response, 'results')
        self.assertContains(response, 'next')
        next_response = self.client.get(response.data['next'])
        self.assertEqual(len(next_response.data['results']), settings.REST_FRAMEWORK['PAGE_SIZE'])

    def test_admin_can_retrieve_one_product(self):
        self.client.force_authenticate(self.admin)
        response = self.client.get('/api/products/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], 1)

    def test_admin_cannot_retrieve_non_existent_product(self):
        self.client.force_authenticate(self.admin)
        response = self.client.get('/api/products/88/')
        self.assertEqual(response.status_code, 404)

    def test_admin_can_create_products(self):
        self.client.force_authenticate(self.admin)
        response = self.client.post('/api/products/', {'name': 'product test', 'price': 25.00}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['id'], 21)

        response = self.client.get('/api/products/21/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], 21)

    def test_admin_can_update_products(self):
        self.client.force_authenticate(self.admin)
        new_product = self.client.post('/api/products/', {'name': 'product test 2', 'price': 50.00}, format='json')
        new_product_id = new_product.json()['id']
        response = self.client.patch(f'/api/products/{new_product_id}/', {'name': 'product test updated', 'price': 100.00}, format='json')
        self.assertEqual(response.json()['id'], new_product_id)
        self.assertEqual(response.json()['name'], 'product test updated')
        self.assertEqual(response.json()['price'], '100.00')

    def test_admin_can_delete_products(self):
        self.client.force_authenticate(self.admin)
        new_product = self.client.post('/api/products/', {'name': 'product test delete', 'price': 2.00}, format='json')
        new_product_id = new_product.json()['id']
        response = self.client.delete(f'/api/products/{new_product_id}/')
        self.assertEqual(response.status_code, 204)

        response = self.client.delete(f'/api/products/{new_product_id}/')
        self.assertEqual(response.status_code, 404)
    
    # test normal user
    def test_normal_user_can_list_all_products(self):
        self.client.force_authenticate(self.normal_user)
        response = self.client.get('/api/products/')
        self.assertContains(response, 'count')
        self.assertEqual(response.data['count'], 20)

    def test_normal_user_can_list_paginated_products(self):
        self.client.force_authenticate(self.normal_user)
        response = self.client.get('/api/products/')
        self.assertContains(response, 'results')
        self.assertEqual(len(response.data['results']), settings.REST_FRAMEWORK['PAGE_SIZE'])

    def test_normal_user_can_list_next_paginated_products(self):
        self.client.force_authenticate(self.normal_user)
        response = self.client.get('/api/products/')
        self.assertContains(response, 'results')
        self.assertContains(response, 'next')

        next_response = self.client.get(response.data['next'])
        self.assertEqual(len(next_response.data['results']), settings.REST_FRAMEWORK['PAGE_SIZE'])

    def test_normal_user_can_retrieve_one_product(self):
        self.client.force_authenticate(self.normal_user)
        response = self.client.get('/api/products/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], 1)

    def test_normal_user_cannot_retrieve_non_existent_product(self):
        self.client.force_authenticate(self.normal_user)
        response = self.client.get('/api/products/88/')
        self.assertEqual(response.status_code, 404)

    def test_normal_user_cannot_create_products(self):
        self.client.force_authenticate(self.normal_user)
        response = self.client.post('/api/products/', {'name': 'product test', 'price': 25.00}, format='json')
        self.assertEqual(response.status_code, 403)

    def test_normal_user_cannot_update_products(self):
        self.client.force_authenticate(self.normal_user)
        response = self.client.patch('/api/products/1/', {'name': 'product test updated', 'price': 500.00}, format='json')
        self.assertEqual(response.status_code, 403)

    def test_normal_user_cannot_delete_products(self):
        self.client.force_authenticate(self.normal_user)
        response = self.client.delete('/api/products/1/')
        self.assertEqual(response.status_code, 403)
