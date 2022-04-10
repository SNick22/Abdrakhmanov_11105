from unittest import TestCase, main
import task011, task012


class Test011(TestCase):
    def test_equal(self):
        self.assertEqual(task011.my_new_balance(60000, 13, 20000), 'Azat, your new balance is 52200')

    def test_type(self):
        with self.assertRaises(TypeError) as e:
            task011.my_new_balance(60000.0, '13', False)


class TestCalculate(TestCase):
    def test_equal(self):
        self.assertEqual(task012.calculate(2, '*', 3, '+', 4, '-', 5, '/', 2), 7.5)

    def test_type(self):
        with self.assertRaises(TypeError) as e:
            task012.calculate(3, 4, 3, '+', 4, '-', 5, '/', 2)


class TestCurCalculate(TestCase):
    def test_equal(self):
        self.assertEqual(task012.cur_calculate(2)('*')(3)('+')(4)('-')(5)('/')(2), 7.5)

    def test_type(self):
        with self.assertRaises(TypeError) as e:
            task012.cur_calculate(None)(4)(3)('+')(4)('-')(5)('/')(2)


class TestPartial(TestCase):
    def test_equal(self):
        self.assertEqual(task012.new_func(a2='+', a4='+', a6='+', a8='+'), 16)

    def test_type(self):
        with self.assertRaises(TypeError) as e:
            task012.new_func(a2=3, a4='+', a6='+', a8='+')


if __name__ == '__main__':
    main()
