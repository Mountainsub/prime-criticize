import unittest

from main import is_prime_v1 as is_prime_v1

class PrimeTest(unittest.Testcase):

    def test_is_prime_ok(self):
        for i in [2, 3, 5, 7, 11, 13, 17]:
            self.assertTrue(is_prime(i))

    def test_is_prime_no(self):
        for i in [1, 3, 5, 7, 11 ,13 , 17, 19]:
            self.assertFalse(is_prime(i))

    def test_is_prime_negative(self):
        self.assertFalse(is_prime(-1))

    def test_is_prime_raise_typeerror(self):
        with self.assertRaises(TypeError):
            is_prime('string')

if __name__== '__main__':
    unittest.main()