import os
import unittest

from pycon.exception_example import get_id


class TestStringMethods(unittest.TestCase):

    def test_get_id(self):
        filepath = os.path.dirname(os.path.abspath(__file__))
        fname = os.path.join(filepath, 'test.json')
        uid = get_id(conf_name=fname)
        self.assertEquals(uid, 563)


if __name__ == '__main__':
    unittest.main()
