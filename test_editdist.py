import unittest

from editdist import by_distance, closest, distance, farthest, within, within_any


class EditdistTest(unittest.TestCase):
    def test_known(self) -> None:
        self.assertEqual(distance("", "abc"), 3)
        self.assertEqual(distance("kitten", "sitting"), 3)
        self.assertEqual(distance("same", "same"), 0)
        self.assertEqual(closest("kitten", ["sitting", "kit"]), "kit")
        self.assertEqual(farthest("kitten", ["sitting", "kit"]), "sitting")
        self.assertEqual(by_distance("kitten", ["sitting", "kit"]), ["kit", "sitting"])
        self.assertTrue(within_any("kitten", ["sitting", "kit"], 3))
        self.assertFalse(within_any("kitten", ["sitting"], 2))
        self.assertTrue(within("kitten", "kit", 3))
        self.assertFalse(within("kitten", "sitting", 2))
        with self.assertRaises(ValueError):
            within("a", "b", -1)
        with self.assertRaises(ValueError):
            closest("a", [])


if __name__ == "__main__":
    unittest.main()
