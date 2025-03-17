import unittest
import main
from blocktohtml import extract_title

class TestBlockNode(unittest.TestCase):

    def test_none(self):
        with self.assertRaises( Exception  ):
            extract_title("""## This is a header 2 node""") 
            extract_title("""This is a text node""") 
    def test_all(self):
        header1 = extract_title("""# This is a text node""")
        self.assertEqual(header1, "This is a text node")
        # 
        header2 = extract_title("""```code
here```
# This is header One""")
        self.assertEqual(header2, "This is header One")
        # 
        header3 = extract_title("""

# This is header One""")
        self.assertEqual(header3, "This is header One")

if __name__ == "__main__":
    unittest.main()