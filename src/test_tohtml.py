import unittest
import main

from textnode import TextNode, TextType
from blocknode import block_to_block_type, BlockType
from conversion import text_node_to_html_node  
from blocktohtml import markdown_to_html_node


class TestBlockNode(unittest.TestCase):
   def test_paragraphs(self):
      md = """
   This is **bolded** paragraph
   text in a p
   tag here

   This is another paragraph with _italic_ text and `code` here

   """

      node = markdown_to_html_node(md)
      html = node.to_html()
      self.assertEqual(
         html,
         "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
      )

   def test_codeblock(self):
      md = """
   ```
   This is text that _should_ remain
   the **same** even with inline stuff
   ```
   """

      node = markdown_to_html_node(md)
      html = node.to_html()
      self.assertEqual(
         html,
         "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
      )

if __name__ == "__main__":
   unittest.main()