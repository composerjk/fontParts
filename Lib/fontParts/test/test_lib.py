import unittest
import collections


class TestLib(unittest.TestCase):

    def getLib_generic(self):
        lib, _ = self.objectGenerator("lib")
        lib.update({
            "key 1": ["A", "B", "C"],
            "key 2": "x",
            "key 3": [],
            "key 4": 20
        })
        return lib

    # ---
    # len
    # ---

    def test_len_initial(self):
        lib = self.getLib_generic()
        self.assertEqual(
            len(lib),
            4
        )

    def test_len_clear(self):
        lib = self.getLib_generic()
        lib.clear()
        self.assertEqual(
            len(lib),
            0
        )

    # -------
    # Queries
    # -------

    def test_keys(self):
        lib = self.getLib_generic()
        self.assertEqual(
            sorted(lib.keys()),
            ["key 1", "key 2", "key 3", "key 4"]
        )

    def test_contains_found(self):
        lib = self.getLib_generic()
        self.assertTrue("key 4" in lib)

    def test_contains_not_found(self):
        lib = self.getLib_generic()
        self.assertFalse("key five" in lib)

    def test_get_found(self):
        lib = self.getLib_generic()
        self.assertEqual(
            lib["key 1"],
            ["A", "B", "C"]
        )

    # ----
    # Hash
    # ----

    def test_hash(self):
        lib = self.getLib_generic()
        self.assertEqual(
            isinstance(lib, collections.Hashable),
            False
        )

    # --------
    # Equality
    # --------

    def test_object_equal_self(self):
        lib_one = self.getLib_generic()
        self.assertEqual(
            lib_one,
            lib_one
        )

    def test_object_not_equal_other(self):
        lib_one = self.getLib_generic()
        lib_two = self.getLib_generic()
        self.assertNotEqual(
            lib_one,
            lib_two
        )

    def test_object_equal_self_variable_assignment(self):
        lib_one = self.getLib_generic()
        a = lib_one
        self.assertEqual(
            lib_one,
            a
        )

    def test_object_not_equal_other_variable_assignment(self):
        lib_one = self.getLib_generic()
        lib_two = self.getLib_generic()
        a = lib_one
        self.assertNotEqual(
            lib_two,
            a
        )
