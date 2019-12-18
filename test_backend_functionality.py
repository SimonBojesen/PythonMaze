import unittest
import backend_functionality

stepcount = 3


class TestBackend(unittest.TestCase):

    def test_increment(self):
        global stepcount
        backend_functionality.increment()
        self.assertEqual(stepcount, 4)

    def test_get_steps(self):
        self.assertNotEqual(backend_functionality.get_steps(), -1)


if __name__ == '__main__':
    unittest.main()
