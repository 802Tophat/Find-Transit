import unittest
import findtransit

class TestFindTransit(unittest.TestCase):

    def test_routes(self):
        self.assertEqual(findtransit.routes("METRO Blue Line"), "901")
        self.assertEqual(findtransit.routes("Route 22"), "22")

    def test_direction(self):
        self.assertEqual(findtransit.direction("South", "901"), "1")
        self.assertEqual(findtransit.direction("North", "901"), "0")

    def test_place_code(self):
        self.assertEqual(findtransit.places("Target Field Station Platform 2", "901", "1"), "TF2")
        self.assertEqual(findtransit.places("Humboldt Ave and 69th Ave", "22", "0"), "69HU")



if __name__ == "__main__":
    unittest.main()