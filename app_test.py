from app import app
import unittest

# This file performs a simple unit test on the app.py file running the site.
# It checks that a button press successfully runs verb.py to get a new verb and then
# sends it to the specified url path. If it completes, it returns a 200 status code
# indicating that new text is being displayed by the button press.

class ButtonPress_test(unittest.TestCase):

  def test_index(self):
    tester = app.test_client(self)
    response = tester.get('/random_verb')
    self.assertEqual(response.status_code, 200)
    print(response)

if __name__ == '__main__':
    unittest.main()