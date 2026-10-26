import math
import unittest

import circle
import rectangle
import square
import triangle


class CircleTestCase(unittest.TestCase):
    def test_area_docstring_example(self):
        self.assertAlmostEqual(circle.area(5), 78.53981633974483)

    def test_perimeter_docstring_example(self):
        self.assertAlmostEqual(circle.perimeter(9), 56.548667764616276)

    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_unit_radius(self):
        self.assertAlmostEqual(circle.area(1), math.pi)

    def test_perimeter_float(self):
        self.assertAlmostEqual(circle.perimeter(0.5), math.pi)


class RectangleTestCase(unittest.TestCase):
    def test_area_docstring_example(self):
        self.assertEqual(rectangle.area(4, 6), 24)

    def test_perimeter_docstring_example(self):
        self.assertEqual(rectangle.perimeter(2, 3), 10)

    def test_area_zero(self):
        self.assertEqual(rectangle.area(10, 0), 0)

    def test_perimeter_float(self):
        self.assertAlmostEqual(rectangle.perimeter(1.5, 2.5), 8.0)

    def test_perimeter_commutative(self):
        self.assertEqual(rectangle.perimeter(3, 7), rectangle.perimeter(7, 3))


class SquareTestCase(unittest.TestCase):
    def test_area_docstring_example(self):
        self.assertEqual(square.area(5), 25)

    def test_perimeter_docstring_example(self):
        self.assertEqual(square.perimeter(5), 20)

    def test_area_float(self):
        self.assertAlmostEqual(square.area(1.5), 2.25)

    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_float(self):
        self.assertAlmostEqual(square.perimeter(2.5), 10.0)

class TriangleTestCase(unittest.TestCase):
    def test_area_docstring_example(self):
        self.assertAlmostEqual(triangle.area(6, 4), 12.0)

    def test_perimeter_docstring_example(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_area_zero_height(self):
        self.assertEqual(triangle.area(5, 0), 0)

    def test_area_float(self):
        self.assertAlmostEqual(triangle.area(3, 2.5), 3.75)

    def test_perimeter_equilateral(self):
        self.assertEqual(triangle.perimeter(5, 5, 5), 15)


if __name__ == "__main__":
    unittest.main()