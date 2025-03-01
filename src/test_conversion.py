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
        print(New_nodeList[0])
        # is now a list of nodes
        self.assertEqual(len(New_nodeList), 1) # one nodes
        self.assertEqual(New_nodeList[0].text_type, TextType.ITALIC)
        self.assertEqual(New_nodeList[0].text, "This is a italic node")
    def test_split_italic(self):
        node = TextNode("This is a _italic_ node", TextType.TEXT)
        New_nodeList = split_nodes_delimiter([node],"_",TextType.ITALIC)
        # is now a list of nodes
        self.assertEqual(len(New_nodeList), 3) # three nodes
        self.assertEqual(New_nodeList[1].text_type, TextType.ITALIC)
        self.assertEqual(New_nodeList[0].text, "This is a ")
        self.assertEqual(New_nodeList[1].text, "italic")
    def test_from_bootdev(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        )
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