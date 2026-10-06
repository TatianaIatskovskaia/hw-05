from unittest import TestCase, main
from my_set.my_set import MySet

class TestMySet(TestCase):
    def setUp(self):
        self.set = MySet()

    def test_add_unique_elements(self):
        self.assertTrue(self.set.add(10))
        self.assertTrue(self.set.add(20))
        self.assertFalse(self.set.add(10))

    def test_contains_element(self):
        self.set.add(170)
        self.assertTrue(170 in self.set)
        self.assertFalse(20 in self.set)

    def test_remove_element(self):
        self.set.add(80)
        self.assertTrue(self.set.remove(80))
        self.assertFalse(self.set.remove(20))

    def test_length(self):
        self.assertEqual(len(self.set), 0)
        self.set.add(170)
        self.assertEqual(len(self.set), 1)
        self.set.add(80)
        self.assertEqual(len(self.set), 2)
        for _ in range(0, 99, 7):
            self.set.add(_)
        self.assertEqual(len(self.set), 17)
        self.set.remove(170)
        self.set.remove(80)
        self.assertEqual(len(self.set), 15)
        self.set.add((15, 80, 170))
        self.assertEqual(len(self.set), 16)

    def test_different_data_types(self):
        self.assertTrue(self.set.add("apple"))
        self.assertTrue(self.set.add("banana"))
        self.assertTrue(self.set.add((1, 2, 3)))  # кортеж

        self.assertTrue("apple" in self.set)
        self.assertFalse("orange" in self.set)

    def test_capacity_resizes(self):
        initial_capacity = self.set.capacity
        for i in range(7):
            self.set.add(i)

        self.assertEqual(self.set.capacity, initial_capacity)

        for i in range(16):
            self.set.add(i)

        self.assertEqual(self.set.capacity, initial_capacity * 2)


if __name__ == '__main__':
    main()