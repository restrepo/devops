import unittest
from devops import devops
class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.pkg = mypkg.mypkg(123)

    def test_var(self):
        self.assertEqual(self.pkg.get(), 123)

if __name__ == '__main__':
    unittest.main()
