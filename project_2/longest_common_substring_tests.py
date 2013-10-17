
import longest_common_substring as lcs
import unittest
import json

class HelloTestCase(unittest.TestCase):

    def setUp(self):
        """
        Sets up the testing environment for the app.
        Will be called before each unit test.
        """
        lcs.app.config['TESTING'] = True
        self.app = lcs.app.test_client()


    def tearDown(self):
        """
        Tears down the unit testing environment for the app.
        Will be called after every unit test.
        """
        pass


    def test_longest_common_substring(self):
        """
        Make sure the root response works
        """
        err_msg = "Incorrect substring returned"
        lc_substr = lcs.longest_common_substring
        self.assertEqual(lc_substr('abc', 'abc'), 'abc', err_msg)
        self.assertEqual(lc_substr('abc', 'def'), '', err_msg)
        self.assertEqual(lc_substr('abcabcabc', 'abc'), 'abc', err_msg)
        self.assertEqual(lc_substr('cba', 'abc'), 'c', err_msg)


    def test_api_call(self):
        err_msg = "API call returning wrong substring"
        json = json.dumps({
            'string1': 'abc',
            'string2': 'abc'
        })
        resp = self.app.post('/lcs', data=json)
        answer = json.loads(resp.data)['longest_common_substring']
        self.assertEqual(answer, 'abc', err_msg)


if __name__ == '__main__':
    unittest.main()

