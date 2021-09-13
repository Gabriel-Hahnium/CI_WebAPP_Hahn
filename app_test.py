from app import app
import unittest

class ButtonPress_test(unittest.TestCase):

  def test_index(self):
    tester = app.test_client(self)
    response = tester.get('/random_verb')
    self.assertEqual(response.status_code, 200)
    print(response)

if __name__ == '__main__':
    unittest.main()