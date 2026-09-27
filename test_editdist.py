import unittest

from editdist import distance


class EditdistTest(unittest.TestCase):
    def test_known(self) -> None:
        self.assertEqual(distance("", "abc"), 3)
        self.assertEqual(distance("kitten", "sitting"), 3)
        self.assertEqual(distance("same", "same"), 0)


if __name__ == "__main__":
    unittest.main()
