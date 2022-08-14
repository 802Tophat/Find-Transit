import unittest
import findtransit

class TestFindTransit(unittest.TestCase):
    ROUTE = "METRO Blue Line"
    DIRECTION = "1"
    DESTINATION = "Target Field Station Platform 2"

    def test_routes(self):
        result = findtransit.routes('METRO Blue Line')
        self.assertEqual(result, "901")

    def test_direction(self):
        result = findtransit.direction("South", "901")
        self.assertAlmostEqual(result, "1")

    def test_place_code(self):
        result = findtransit.places("Target Field Station Platform 2", "901", "1")
        self.assertEqual(result, "TF2")




if __name__ == "__main__":
    unittest.main()