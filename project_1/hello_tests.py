
import hello
import unittest
import random
import string

proper_response = "Hello World"

class HelloTestCase(unittest.TestCase):

    def setUp(self):
        """
        Sets up the testing environment for the app.
        Will be called before each unit test.
        """
        hello.app.config['TESTING'] = True
        self.app = hello.app.test_client()


    def tearDown(self):
        """
        Tears down the unit testing environment for the app.
        Will be called after every unit test.
        """
        pass


    def test_root_response(self):
        """
        Make sure the root response works
        """
        assert self.app.get('/').data == proper_response,(
            "'/' did not return {}".format(proper_response))


    def test_random_response(self):
        """
        Make sure the response works regardless of url
        """
        def rand_string(size=6, chars=string.ascii_uppercase + string.digits):
            return ''.join(random.choice(chars) for x in range(size))

        for x in range(10):
            rand_route = rand_string()
            assert self.app.get('/'+rand_route).data == proper_response,(
                "'/{}' did not return {}".format(rand_route, proper_response))


if __name__ == '__main__':
    unittest.main()

