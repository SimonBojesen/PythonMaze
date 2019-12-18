import unittest
import backend_functionality

stepcount = 3


class TestBackend(unittest.TestCase):

    def test_increment(self):
        stepcount=1
        stepcount_incremented = backend_functionality.increment(stepcount)
        self.assertEqual(stepcount_incremented, 2)

    def test_get_steps(self):
        self.assertNotEqual(backend_functionality.get_steps(), 0)


if __name__ == '__main__':
    unittest.main()
