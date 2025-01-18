import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10
        return self.distance

    def walk(self):
        self.distance += 5
        return self.distance

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    # walker = Runner('petr')
    def test_walk(self):
        walker = Runner("Петр")
        self.assertEqual((walker.walk() * 10), 50)

    def test_run(self):
        runner = Runner("Захар")
        self.assertEqual((runner.run() * 10), 100)

    def test_challenge(self):
        runner1 = Runner("Галя")
        walker1 = Runner("Валя")
        self.assertNotEqual((runner1.run() * 10), (walker1.walk() * 10))


if __name__ == '__main__':
    unittest.main()
