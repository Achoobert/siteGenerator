import unittest
import main

from textnode import TextNode, TextType
from blocknode import block_to_block_type, BlockType
from conversion import text_node_to_html_node


class TestBlockNode(unittest.TestCase):
    def test_none(self):
        arr = [
            "#This is a chunk of> text#",
            "```This is a chunk of text",
            "This is a chunk of text",
            """2. This is 1 text node
2. this is 2 text node""",
            """- This is 1 text node
this is 2 text node"""
        ]
        for block in arr:
            self.assertIs(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_all(self):
        block1 = block_to_block_type("## This is a text node")
        block2 = block_to_block_type("""```This is a text node```""")
        block3 = block_to_block_type("""- This is 1 text node
- this is 2 text node""")
        block4 = block_to_block_type("""1. This is 1 text node
2. this is 2 text node""")
        block5 = block_to_block_type("""> This is 1 text 
> this is 2 text """)
        self.assertIs(block1, BlockType.HEADING)
        self.assertIs(block2, BlockType.CODE)
        self.assertIs(block3, BlockType.UNORDERED_LIST)
        self.assertIs(block4, BlockType.ORDERED_LIST)
        self.assertIs(block5, BlockType.QUOTE)
    # def test_text(self):
    #     node = TextNode("This is a text node", TextType.TEXT)
    #     html_node = text_node_to_html_node(node)
    #     self.assertEqual(html_node.tag, None)
    #     self.assertEqual(html_node.value, "This is a text node")
    # def test_text(self):
    #     node = TextNode("This is a bold node", TextType.BOLD)
    #     html_node = text_node_to_html_node(node)
    #     self.assertEqual(html_node.tag, "b")
    #     self.assertEqual(html_node.value, "This is a bold node")
    #     self.assertEqual(html_node.to_html(), "<b>This is a bold node</b>")

if __name__ == "__main__":
    unittest.main()