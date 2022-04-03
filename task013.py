import unittest, task011


class Test011(unittest.TestCase):
    def test_type(self):
        self.assertRaises(TypeError, task011.my_new_balance)


if __name__ == '__main__':
    unittest.main()
