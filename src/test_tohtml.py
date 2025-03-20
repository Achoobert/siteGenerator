import unittest
import main

from htmlnode import ParentNode
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
      self.assertIsInstance(node, ParentNode)
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
      self.assertIsInstance(node, ParentNode)
      html = node.to_html()
      self.assertEqual(
         html,
         "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
      )
   def test_quoteblock(self):
      md = """> This is quote that _should_ remain
> the **same** even with inline stuff
"""

      node = markdown_to_html_node(md)
      self.assertIsInstance(node, ParentNode)
      html = node.to_html()
      self.assertEqual(
         html,
         "<div><blockquote>This is quote that <i>should</i> remain\nthe <b>same</b> even with inline stuff</blockquote></div>",
      )
   def test_headerblock(self):
      md = """# This is header that _should_ 
normal text
## Smaller header
normal text
   """

      node = markdown_to_html_node(md)
      self.assertIsInstance(node, ParentNode)
      html = node.to_html()
      self.assertEqual(
         html,
         "<div><h1>This is header that <i>should</i></h1><p>normal text</p><h2>Smaller header</h2><p>normal text</p></div>",
      )
   def test_orderedlistblock(self):
      md = """1. one/three ordered
2. two
3. three"""

      node = markdown_to_html_node(md)
      self.assertIsInstance(node, ParentNode)
      html = node.to_html()
      self.assertEqual(
         html,
         "<div><ol><li>one/three ordered</li><li>two</li><li>three</li></ol></div>",
      )
   def test_listblock(self):
      md = """- one/three. unordered
- two
- three
   """

      node = markdown_to_html_node(md)
      self.assertIsInstance(node, ParentNode)
      html = node.to_html()
      self.assertEqual(
         html,
         "<div><ul><li>one/three. unordered</li><li>two</li><li>three</li></ul></div>",
      )

if __name__ == "__main__":
   unittest.main()