import unittest
import math

from circle import area, perimeter;

class CircleAreaTestCases(unittest.TestCase):
    def test_circle_int_first(self):
        self.assertEqual(area(5), math.pi * 5 * 5)

    def test_circle_int_second(self):
        self.assertEqual(area(200), math.pi * 200 * 200)

    def test_circle_string_first(self):
        with self.assertRaises(TypeError):
            area("3118")

    def test_circle_string_second(self):
        with self.assertRaises(TypeError):
            area("Steshkin")

    def test_circle_bool_first(self):
        with self.assertRaises(TypeError):
            area(True)  

    def test_circle_bool_second(self):
        with self.assertRaises(TypeError):
            area(False)  

    def test_circle_negative_int_first(self):
        with self.assertRaises(ValueError):
            area(-333)

    def test_circle_negative_int_second(self):
        with self.assertRaises(ValueError):
            area(-777)

    def test_circle_zero_int(self):
        with self.assertRaises(ValueError):
            area(0)

class CirclePerimeterTestCases(unittest.TestCase):
    def test_circle_int_first(self):
        self.assertEqual(perimeter(7777), 2 * math.pi * 7777)

    def test_circle_int_second(self):
        self.assertEqual(perimeter(728), 2 * math.pi * 728)

    def test_circle_string_first(self):
        with self.assertRaises(TypeError):
            perimeter("3118")

    def test_circle_string_second(self):
        with self.assertRaises(TypeError):
            perimeter("Steshkin")

    def test_circle_bool_first(self):
        with self.assertRaises(TypeError):
            perimeter(True)  

    def test_circle_bool_second(self):
        with self.assertRaises(TypeError):
            perimeter(False)  

    def test_circle_negative_int_first(self):
        with self.assertRaises(ValueError):
            perimeter(-333)

    def test_circle_negative_int_second(self):
        with self.assertRaises(ValueError):
            perimeter(-777)

    def test_circle_zero_int(self):
        with self.assertRaises(ValueError):
            perimeter(0)

if __name__ == '__main__':
    unittest.main()

    