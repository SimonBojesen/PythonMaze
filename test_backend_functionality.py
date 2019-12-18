import unittest
import backend_functionality


class TestBackend(unittest.TestCase):

    def test_increment(self):
        backend_functionality.increment()
        stepcount = backend_functionality.get_steps()
        self.assertEqual(stepcount, 0)

    def test_get_steps(self):
        # Steps is a global variable in backend_functionality which starts by being -1
        self.assertEqual(backend_functionality.get_steps(), -1)

    def test_reset_steps(self):
        backend_functionality.reset_steps()

        self.assertEqual(backend_functionality.get_steps(), -1)

    def test_make_empty_maze(self):
        self.assertEqual(backend_functionality.make_empty_maze(5, 5), [[[], [], [], [], []], [
                         [], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []], [[], [], [], [], []]])


if __name__ == '__main__':
    unittest.main()
