import unittest

from editdist import beyond, by_distance, closest, distance, farthest, nearest_count, nearest_distance, only_closest, spread_of, tied, within, within_any, far_count, even_spread


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
        self.assertEqual(beyond("cat", ["cats", "dog"], 1), ["dog"])
        self.assertEqual(nearest_distance("kitten", ["sitting", "kit"]), distance("kitten", "kit"))
        self.assertEqual(tied("cat", ["ca", "cats", "dog"]), ["ca", "cats"])
        self.assertFalse(only_closest("cat", ["ca", "cats", "dog"]))
        self.assertTrue(only_closest("cat", ["cat", "dog"]))
        self.assertEqual(spread_of("cat", ["cat", "dog"]), 3)
        self.assertEqual(nearest_count("cat", ["cat", "dog"]), 1)
        self.assertEqual(nearest_count("cat", ["bat", "hat"]), 2)
        self.assertTrue(within("kitten", "kit", 3))
        self.assertFalse(within("kitten", "sitting", 2))
        with self.assertRaises(ValueError):
            within("a", "b", -1)
        with self.assertRaises(ValueError):
            closest("a", [])


        self.assertEqual(far_count("cat", ["cat", "dog"]), 1)

        self.assertTrue(even_spread("cat", ["cat", "cat"]))
        self.assertFalse(even_spread("cat", ["cat", "dog"]))

if __name__ == "__main__":
    unittest.main()
