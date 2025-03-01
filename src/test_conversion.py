import unittest
import main

from textnode import TextNode, TextType
from conversion import text_node_to_html_node, split_nodes_delimiter


class TestConversion(unittest.TestCase):
    def test_text_to_html(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_bold_to_html(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
        self.assertEqual(html_node.to_html(), "<b>This is a bold node</b>")
    # split_nodes_delimiter
    def test_all_italic(self):
        node = TextNode("_This is a italic node_", TextType.TEXT)
        New_nodeList = split_nodes_delimiter([node],"_",TextType.ITALIC)
        # is now a list of nodes
        self.assertEqual(len(New_nodeList), 1) # three nodes
        self.assertEqual(New_nodeList[0].tag, "i")
        self.assertEqual(New_nodeList[0].value, "This is a italic node")
        self.assertEqual(New_nodeList[0].value, "italic")
    # def test_split_italic(self):
    #     node = TextNode("This is a _italic_ node", TextType.TEXT)
    #     New_nodeList = split_nodes_delimiter([node],"_",TextType.ITALIC)
    #     # is now a list of nodes
    #     self.assertEqual(len(New_nodeList), 3) # three nodes
    #     self.assertEqual(New_nodeList[1].tag, "i")
    #     self.assertEqual(New_nodeList[0].value, "This is a")
    #     self.assertEqual(New_nodeList[1].value, "italic")
    #     # self.assertEqual(html_node.to_html(), "<b>This is a bold node</b>")
    # def test_split_code(self):
    #     node = TextNode("This is a bold node", TextType.BOLD)
    #     html_node = text_node_to_html_node(node)
    #     self.assertEqual(html_node.tag, "b")
    #     self.assertEqual(html_node.value, "This is a bold node")
    #     self.assertEqual(html_node.to_html(), "<b>This is a bold node</b>")
    # def test_split_bold(self):
    #     node = TextNode("This is a bold node", TextType.BOLD)
    #     html_node = text_node_to_html_node(node)
    #     self.assertEqual(html_node.tag, "b")
    #     self.assertEqual(html_node.value, "This is a bold node")
    #     self.assertEqual(html_node.to_html(), "<b>This is a bold node</b>")

if __name__ == "__main__":
    unittest.main()