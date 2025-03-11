import unittest
import main

from textnode import TextNode, TextType
from conversion import text_node_to_html_node, split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes, markdown_to_blocks


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
        # print(New_nodeList[0])
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
    def test_split_multi_italic(self):
        node = TextNode("This is an _italic_ ah _node_", TextType.TEXT)
        New_nodeList = split_nodes_delimiter([node],"_",TextType.ITALIC)
        # is now a list of nodes
        self.assertEqual(len(New_nodeList), 4) # four nodes
        self.assertEqual(New_nodeList[1].text_type, TextType.ITALIC)
        self.assertEqual(New_nodeList[3].text_type, TextType.ITALIC)
        self.assertEqual(New_nodeList[0].text, "This is an ")
        self.assertEqual(New_nodeList[1].text, "italic")
        self.assertEqual(New_nodeList[3].text, "node")
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
    def test_split_code(self):
        node = TextNode("This is a **bold** node", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[1].text, "bold")
        # self.assertEqual(new_nodes[1].to_html(), "<b>bold</b>")
    def test_split_bold(self):
        node = TextNode("This is a `bold` node", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[1].text, "bold")
        # self.assertEqual(new_nodes[1].to_html(), "<b>This is a bold node</b>")
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
            [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")],
             matches
        )
        
    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_text_to_textnodes(self):
        new_nodes = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes,
        )
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
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
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