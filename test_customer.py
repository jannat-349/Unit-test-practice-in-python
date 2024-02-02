import unittest
from unittest.mock import patch
from customer import Customer


class TestCustomer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """This class run before all the test cases"""
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        """This class run after all the test cases"""
        print('teardownClass')

    def setUp(self):
        """This function run before every test case, can config database here"""
        print('setUp')
        self.emp_1 = Customer('Jannatul', 'Ferdoush', 50000)
        self.emp_2 = Customer('Sumaya', 'Islam', 60000)

    def tearDown(self):
        """This function run after every test case, can delete database here"""
        print('tearDown\n')

    def test_email(self):
        """tests the email of employee after any change"""
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Jannatul.Ferdoush@email.com')
        self.assertEqual(self.emp_2.email, 'Sumaya.Islam@email.com')

        self.emp_1.first = 'Nusrat'
        self.emp_2.first = 'Mahrufa'

        self.assertEqual(self.emp_1.email, 'Nusrat.Ferdoush@email.com')
        self.assertEqual(self.emp_2.email, 'Mahrufa.Islam@email.com')

    def test_fullname(self):
        """tests the fullname of employee after any change"""
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Jannatul Ferdoush')
        self.assertEqual(self.emp_2.fullname, 'Sumaya Islam')

        self.emp_1.first = 'Nusrat'
        self.emp_2.first = 'Mahrufa'

        self.assertEqual(self.emp_1.fullname, 'Nusrat Ferdoush')
        self.assertEqual(self.emp_2.fullname, 'Mahrufa Islam')

    def test_apply_raise(self):
        """tests the pay amount raised by 5% of the employee"""
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        """tests the monthly_schedule url of the employee"""
        with patch('customer.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Ferdoush/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Islam/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()