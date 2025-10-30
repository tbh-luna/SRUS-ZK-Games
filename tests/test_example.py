import unittest
# from unittest.mock import patch


class TestExample(unittest.TestCase):
    def test_this(self):
        results = [True, True, False, True, False]
        self.assertEqual(len(results), 5)


if __name__ == '__main__':
    unittest.main()
