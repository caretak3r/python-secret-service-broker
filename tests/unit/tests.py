from app import app, models
from flask import json

class TestSecretsAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_secrets(self):
        response = self.app.get('/secrets')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_get_secret(self):
        response = self.app.get('/secrets/1')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)

    def test_create_secret(self):
        response = self.app.post('/secrets', data=json.dumps({'value': 'secret_value'}), content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['value'], 'secret_value')

    def test_update_secret(self):
        response = self.app.put('/secrets/1', data=json.dumps({'value': 'new_secret_value'}), content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['value'], 'new_secret_value')

    def test_delete_secret(self):
        response = self.app.delete('/secrets/1')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
