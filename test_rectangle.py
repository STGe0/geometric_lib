import unittest

from rectangle import area, perimeter;

class RectangleAreaTestCases(unittest.TestCase):
    def test_rectangle_int_first(self):
        self.assertEqual(area(10, 20), 10 * 20)

    def test_rectangle_int_second(self):
        self.assertEqual(area(10000, 23445), 10000*23445)

    def test_rectangle_string_first(self):
        with self.assertRaises(TypeError):
            area("Georgy", "Steshkin")

    def test_rectangle_string_second(self):
        with self.assertRaises(TypeError):
            area("Steshkin", 3118)

    def test_rectangle_bool_first(self):
        with self.assertRaises(TypeError):
            area(True, True)  

    def test_rectangle_bool_second(self):
        with self.assertRaises(TypeError):
            area(False, False)  

    def test_rectangle_negative_int_first(self):
        with self.assertRaises(ValueError):
            area(-333, 10)

    def test_rectangle_negative_int_second(self):
        with self.assertRaises(ValueError):
            area(-777, -10)

    def test_rectangle_zero_int_first(self):
        with self.assertRaises(ValueError):
            area(0, 777)

    def test_rectangle_zero_int_second(self):
        with self.assertRaises(ValueError):
            area(12, 0)

class RectanglePerimeterTestCases(unittest.TestCase):
    def test_rectangle_int_first(self):
        self.assertEqual(perimeter(4, 5), 2 * (4 + 5))

    def test_rectangle_int_second(self):
        self.assertEqual(perimeter(777, 999), 2 * (777 + 999))

    def test_rectangle_string_first(self):
        with self.assertRaises(TypeError):
            perimeter("Georgy", "Steshkin")

    def test_rectangle_string_second(self):
        with self.assertRaises(TypeError):
            perimeter("Steshkin", 3118)

    def test_rectangle_bool_first(self):
        with self.assertRaises(TypeError):
            perimeter(True, True)  

    def test_rectangle_bool_second(self):
        with self.assertRaises(TypeError):
            perimeter(False, False)  

    def test_rectangle_negative_int_first(self):
        with self.assertRaises(ValueError):
            perimeter(-333, 12)

    def test_rectangle_negative_int_second(self):
        with self.assertRaises(ValueError):
            perimeter(-777, -12)

    def test_rectangle_zero_int_first(self):
        with self.assertRaises(ValueError):
            perimeter(0, 777)

    def test_rectangle_zero_int_second(self):
        with self.assertRaises(ValueError):
            perimeter(12, 0)

if __name__ == '__main__':
    unittest.main()