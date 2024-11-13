import unittest

from triangle import area, perimeter;

class TriangleAreaTestCases(unittest.TestCase):
    def test_triangle_int_first(self):
        self.assertEqual(area(10, 20), 10 * 20 / 2)

    def test_triangle_int_second(self):
        self.assertEqual(area(10000, 23445), 10000 * 23445 / 2)

    def test_triangle_string_first(self):
        with self.assertRaises(TypeError):
            area("Georgy", "Steshkin")

    def test_triangle_string_second(self):
        with self.assertRaises(TypeError):
            area("Steshkin", 3118)

    def test_triangle_bool_first(self):
        with self.assertRaises(TypeError):
            area(True, True)  

    def test_triangle_bool_second(self):
        with self.assertRaises(TypeError):
            area(False, False)  

    def test_triangle_negative_int_first(self):
        with self.assertRaises(ValueError):
            area(-333, 10)

    def test_triangle_negative_int_second(self):
        with self.assertRaises(ValueError):
            area(-777, -10)

    def test_triangle_zero_int_first(self):
        with self.assertRaises(ValueError):
            area(0, 777)

    def test_triangle_zero_int_second(self):
        with self.assertRaises(ValueError):
            area(12, 0)

class TrianglePerimeterTestCases(unittest.TestCase):
    def test_triangle_int_first(self):
        self.assertEqual(perimeter(4, 5, 6), 4 + 5 + 6)

    def test_triangle_int_second(self):
        self.assertEqual(perimeter(777, 999, 1111), 777 + 999 + 1111)

    def test_triangle_string_first(self):
        with self.assertRaises(TypeError):
            perimeter("Georgy", "Steshkin", "M3118")

    def test_triangle_string_second(self):
        with self.assertRaises(TypeError):
            perimeter("Steshkin", 3118, "Georgy")

    def test_triangle_bool_first(self):
        with self.assertRaises(TypeError):
            perimeter(True)  

    def test_triangle_bool_second(self):
        with self.assertRaises(TypeError):
            perimeter(False)  

    def test_triangle_negative_int_first(self):
        with self.assertRaises(ValueError):
            perimeter(-333, 12, 17)

    def test_triangle_negative_int_second(self):
        with self.assertRaises(ValueError):
            perimeter(-777, -12, -100)

    def test_triangle_zero_int_first(self):
        with self.assertRaises(ValueError):
            perimeter(0, 777, 100)

    def test_triangle_zero_int_second(self):
        with self.assertRaises(ValueError):
            perimeter(12, 0, 11)

if __name__ == '__main__':
    unittest.main()