from unittest import TestCase

from capsules.capsules import capsules

identity = lambda x: x

@capsules
def double(x):
    return x + x

def square(x):
    return x * x
square = capsules(square)

exec('def power(x): return x**x')

class Test_capsules(TestCase):
    def test_non_function(self):
        self.assertRaises(TypeError, capsules, 123)
        try:
            capsules(123)
            self.assertFail()
        except TypeError as error:
            self.assertEqual(str(error), 'input is not a function')

    def test_lambda(self):
        self.assertRaises(ValueError, capsules, identity)
        try:
            capsules(identity)
            self.assertFail()
        except ValueError as error:
            self.assertEqual(str(error), 'lambda functions are not supported')

    def test_no_source(self):
        self.assertRaises(OSError, capsules, power)
        try:
            capsules(power)
            self.assertFail()
        except OSError as error:
            self.assertEqual(str(error), 'could not get source code')

    def test_decorator(self):
        self.assertTrue(double(2) == 4)

    def test_direct(self):
        self.assertTrue(square(3) == 9)
