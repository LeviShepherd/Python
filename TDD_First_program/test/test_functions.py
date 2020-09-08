import unittest
from TDD_First_program.main import camper_age_input


class MyTestCase(unittest.TestCase):
    def test_convert_to_months(self):
        expected = 60
        actual = camper_age_input.convert_to_months(5)
        self.assertEquals(expected, actual)


if __name__ == '__main__':
    unittest.main()
