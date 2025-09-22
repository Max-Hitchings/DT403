import unittest
from app import app

class ApiEndpointsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True


    def test_most_popular_products_new(self):
        response = self.app.get('/api/most_popular_products')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        if data:  # Check only if the list is not empty
            self.assertIn('product_id', data[0])
            self.assertIn('product_name', data[0])
            self.assertIn('total_quantity', data[0])

    def test_revenue_generation(self):
        response = self.app.get('/api/revenue_generation')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('dates', data)
        self.assertIn('revenues', data)
        self.assertIsInstance(data['dates'], list)
        self.assertIsInstance(data['revenues'], list)

    def test_product_category_popularity(self):
        response = self.app.get('/api/product_category_popularity')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('categories', data)
        self.assertIn('sales', data)
        self.assertIsInstance(data['categories'], list)
        self.assertIsInstance(data['sales'], list)

if __name__ == '__main__':
    unittest.main()