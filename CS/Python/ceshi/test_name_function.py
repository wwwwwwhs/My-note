import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Test case for 'name_function.py'"""

    def test_first_last_name(self):
        """Do names like 'John Doe' work?"""
        formatted_name = get_formatted_name('John', 'Doe')
        self.assertEqual(formatted_name, 'John Doe')

if __name__ == '__main__':
    unittest.main()