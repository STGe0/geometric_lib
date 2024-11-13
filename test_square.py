import unittest

from square import area, perimeter;

class SquareAreaTestCases(unittest.TestCase):
    def test_square_int_first(self):
        self.assertEqual(area(10), 10*10)

    def test_square_int_second(self):
        self.assertEqual(area(10000), 10000*10000)

    def test_square_string_first(self):
        with self.assertRaises(TypeError):
            area("3118")

    def test_square_string_second(self):
        with self.assertRaises(TypeError):
            area("Steshkin")

    def test_square_bool_first(self):
        with self.assertRaises(TypeError):
            area(True)  

    def test_square_bool_second(self):
        with self.assertRaises(TypeError):
            area(False)  

    def test_square_negative_int_first(self):
        with self.assertRaises(ValueError):
            area(-333)

    def test_square_negative_int_second(self):
        with self.assertRaises(ValueError):
            area(-777)

    def test_square_zero_int_first(self):
        with self.assertRaises(ValueError):
            area(0)

class SquarePerimeterTestCases(unittest.TestCase):
    def test_square_int_first(self):
        self.assertEqual(perimeter(7), 4*7)

    def test_square_int_second(self):
        self.assertEqual(perimeter(777), 4 * 777)

    def test_square_string_first(self):
        with self.assertRaises(TypeError):
            perimeter("3118")

    def test_square_string_second(self):
        with self.assertRaises(TypeError):
            perimeter("Steshkin")

    def test_square_bool_first(self):
        with self.assertRaises(TypeError):
            perimeter(True)  

    def test_square_bool_second(self):
        with self.assertRaises(TypeError):
            perimeter(False)  

    def test_square_negative_int_first(self):
        with self.assertRaises(ValueError):
            perimeter(-333)

    def test_square_negative_int_second(self):
        with self.assertRaises(ValueError):
            perimeter(-777)

    def test_square_zero_int_first(self):
        with self.assertRaises(ValueError):
            perimeter(0)

if __name__ == '__main__':
    unittest.main()