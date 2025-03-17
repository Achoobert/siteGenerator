import unittest
import main

from generatePage import generate_page


class TestBlockNode(unittest.TestCase):
    def test_none(self):
        # generate_page('./content/index.md', './template.html', 'dest_path')
        pass
#         arr = [
#             "#This is a chunk of> text#",
#             "```This is a chunk of text",
#             "This is a chunk of text",
#             """2. This is 1 text node
# 2. this is 2 text node""",
#             """- This is 1 text node
# this is 2 text node"""
#         ]
#         for block in arr:
#             self.assertIs(block_to_block_type(block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()