from lab_03_list import IntegerList
from unittest import TestCase, main


class TestIntegerList(TestCase):

    def setUp(self):
        self.list = IntegerList(1, -2, 3, -4)

    def test_init(self):
        l = IntegerList()
        self.assertEqual([], l._IntegerList__data)
        l = IntegerList('asd', 3, 16.5, False, [1, 5, 3])
        self.assertEqual([3], l._IntegerList__data)

    def test_get_data(self):
        self.assertEqual([1, -2, 3, -4], self.list._IntegerList__data)
        result = self.list.get_data()
        self.assertEqual([1, -2, 3, -4], result)

    def test_add_raise_error(self):
        element = 'asd'
        self.assertNotIn(element, self.list._IntegerList__data)

        with self.assertRaises(ValueError) as error:
            self.list.add(element)

        self.assertEqual("Element is not Integer", str(error.exception))
        self.assertNotIn(element, self.list._IntegerList__data)

    def test_add_IntegerList(self):
        self.assertEqual([1, -2, 3, -4], self.list._IntegerList__data)
        result = self.list.add(5)
        self.assertIn(5, self.list._IntegerList__data)
        self.assertEqual([1, -2, 3, -4, 5], result)

    def test_remove_index_raise_error(self):
        index = len(self.list.get_data())
        self.assertEqual([1, -2, 3, -4], self.list._IntegerList__data)
        with self.assertRaises(IndexError) as ex:
            self.list.remove_index(index)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([1, -2, 3, -4], self.list._IntegerList__data)

        index = len(self.list.get_data()) + 1
        self.assertEqual([1, -2, 3, -4], self.list._IntegerList__data)
        with self.assertRaises(IndexError) as ex:
            self.list.remove_index(index)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([1, -2, 3, -4], self.list._IntegerList__data)

    def test_remove_index_success(self):
        self.assertIn(1, self.list._IntegerList__data)
        result = self.list.remove_index(0)
        self.assertNotIn(1, self.list._IntegerList__data)
        self.assertEqual(1, result)

    def test_get_IntegerList_raises(self):
        self.assertEqual([1, -2, 3, -4], self.list._IntegerList__data)
        index = len(self.list._IntegerList__data)
        with self.assertRaises(IndexError) as ex:
            self.list.get(index)

        self.assertEqual([1, -2, 3, -4], self.list._IntegerList__data)
        self.assertEqual("Index is out of range", str(ex.exception))

        index = len(self.list._IntegerList__data) + 1
        with self.assertRaises(IndexError) as ex:
            self.list.get(index)

        self.assertEqual([1, -2, 3, -4], self.list._IntegerList__data)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_IntegerList_success(self):
        self.assertEqual([1, -2, 3, -4], self.list._IntegerList__data)
        result = self.list.get(0)
        self.assertEqual(1, result)
        self.assertEqual([1, -2, 3, -4], self.list._IntegerList__data)

    def test_insert_raises_index_error(self):
        index = len(self.list._IntegerList__data)
        element = 6
        self.assertEqual([1, -2, 3, -4], self.list._IntegerList__data)
        with self.assertRaises(IndexError) as ex:
            self.list.insert(index, element)
        self.assertEqual([1, -2, 3, -4], self.list._IntegerList__data)
        self.assertEqual("Index is out of range", str(ex.exception))

        index = len(self.list._IntegerList__data) + 1
        self.assertEqual([1, -2, 3, -4], self.list._IntegerList__data)
        with self.assertRaises(IndexError) as ex:
            self.list.insert(index, element)
        self.assertEqual([1, -2, 3, -4], self.list._IntegerList__data)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_raises_value_error(self):
        index = 0
        element = 'asd'
        self.assertEqual([1, -2, 3, -4], self.list._IntegerList__data)
        with self.assertRaises(ValueError) as ex:
            self.list.insert(index, element)
        self.assertEqual([1, -2, 3, -4], self.list._IntegerList__data)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_success(self):
        self.assertEqual([1, -2, 3, -4], self.list._IntegerList__data)
        result = self.list.insert(0, 5)
        self.assertEqual([5, 1, -2, 3, -4], self.list._IntegerList__data)
        self.assertIsNone(result)

    def test_get_biggest_IntegerList(self):
        self.assertEqual([1, -2, 3, -4], self.list._IntegerList__data)
        result = self.list.get_biggest()
        self.assertEqual(3, result)
        self.assertEqual([1, -2, 3, -4], self.list._IntegerList__data)

    def test_get_index_IntegerList(self):
        self.assertEqual([1, -2, 3, -4], self.list._IntegerList__data)
        result = self.list.get_index(-2)
        self.assertEqual(1, result)
        self.assertEqual([1, -2, 3, -4], self.list._IntegerList__data)


if __name__ == '__main__':
    main()
