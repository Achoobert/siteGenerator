import unittest
import main

from textnode import TextNode, TextType
from blocknode import block_to_block_type, BlockType, markdown_to_blocks
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
            a, text = block_to_block_type(block)
            self.assertIs(a, BlockType.PARAGRAPH)

    def test_all(self):
        block1, text = block_to_block_type("## This is a text node")
        block2, text = block_to_block_type("""```This is a text node```""")
        block3, text = block_to_block_type("""- This is 1 text node
- this is 2 text node""")
        block4, text = block_to_block_type("""1. This is 1 text node
2. this is 2 text node""")
        block5, text = block_to_block_type("""> This is 1 text 
> this is 2 text """)
        block6, text = block_to_block_type("""## This is a markdown node""")
        
        self.assertIs(block1, BlockType.HEADING)
        self.assertIs(block2, BlockType.CODE)
        self.assertIs(block3, BlockType.UNORDERED_LIST)
        self.assertIs(block4, BlockType.ORDERED_LIST)
        self.assertIs(block5, BlockType.QUOTE)
        self.assertIs(block6, BlockType.HEADING)
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
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here This is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    def test_markdown_to_three_blocks(self):
        md = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""
        out = ["""# This is a heading""","""This is a paragraph of text. It has some **bold** and _italic_ words inside of it.""","""- This is the first list item in a list block
- This is a list item
- This is another list item"""]
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            out,
        )
    def test_mtb_excessive_newlines(self):
        md = """
    This is **bolded** paragraph






    This is another paragraph with _italic_ text and `code` here
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here",
            ],
        )

if __name__ == "__main__":
    unittest.main()