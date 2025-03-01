import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestNode(unittest.TestCase):
   def test_eqTag(self):
      node = HTMLNode(tag="a")
      node2 = HTMLNode(tag="a")
      self.assertEqual(node, node2)
   def test_eqProps(self):
      node = HTMLNode(props={"href": "https://www.google.com"})
      node2 = HTMLNode(props={"href": "https://www.google.com"})
      self.assertEqual(node, node2)
   # def test_propComplexEq(self):
      node3 = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
      node4 = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
      self.assertEqual(node3, node4)
   def test_HtmlOutput(self):
      nodeNew = HTMLNode(props={"href": "https://www.google.com", "target": "_blank",})
      self.assertEqual(nodeNew.props_to_html(), 'href="https://www.google.com" target="_blank"')
   # def testThrow(self):
   #    nodeError = HTMLNode()
   #    self.assertRaises(expected_exception= "Not Implemented")
   #    node3 = TextNode("This is text", TextType.ITALIC, "https://www.boot.dev")
   #    node4 = TextNode("This is text", TextType.ITALIC, "https://www.boot.dev")
   #    self.assertEqual(node3, node4)
   #    node5 = TextNode("", TextType.CODE, "")
   #    node6 = TextNode("", TextType.CODE, "")
   #    self.assertEqual(node5, node6)
   def test_parent_eq(self):
      node = LeafNode("a", "This is a text node")
      node2 = LeafNode("a", "This is a text node")
      # self.assertEqual(node, node2)
      node3 = ParentNode(
         "p",
         [
            LeafNode("b", "Bold text"),
            LeafNode(None, " Normal text "),
            LeafNode("i", "italic text"),
            LeafNode(None, " Normal text "),
         ],
      )
      self.assertEqual(node3.to_html(), "<p><b>Bold text</b> Normal text <i>italic text</i> Normal text </p>")
      self.assertEqual(node.hasChildren(), False)
      self.assertEqual(node3.hasChildren(), True)


   def test_parents_eq_false(self):
      node = LeafNode("a", "This is a text node")
      nodeOff = LeafNode("a", "This is a node")
      node2 = LeafNode("p", "This is a paragraph node")
      node3 = ParentNode("a", [nodeOff, node2])
      node4 = ParentNode("a", [node, node2])
      self.assertNotEqual(node3, node4)
   # def testThrow(self):
   #    node2 = ParentNode("body", None)
   #    # nodeError = node2.to_html()
   #    with self.assertRaises(Exception: "Invalid parent: no children"):
   #       nodeError = node2.to_html(),
   # 
   def test_eq(self):
      node = LeafNode("a", "This is a text node", )
      node2 = LeafNode("p", "This is a paragraph node")
      node3 = ParentNode("a", [node, node2])
      node4 = ParentNode("a", [node, node2])
      self.assertEqual(node3, node4)
      def test_to_html_with_children(self):
         child_node = LeafNode("span", "child")
         parent_node = ParentNode("div", [child_node])
         self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

   def test_to_html_with_grandchildren(self):
      grandchild_node = LeafNode("b", "grandchild")
      child_node = ParentNode("span", [grandchild_node])
      parent_node = ParentNode("div", [child_node])
      self.assertEqual(
         parent_node.to_html(),
         "<div><span><b>grandchild</b></span></div>",
      )



if __name__ == "__main__":
   unittest.main()