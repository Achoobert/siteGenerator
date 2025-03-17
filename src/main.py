from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from conversion import text_node_to_html_node, split_nodes_delimiter
from copyDir import moveDirectory

# print("hello world")
a = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
b = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
h = HTMLNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
node2 = HTMLNode(props={
    "href": "https://www.google.com", 
    "target": "_blank",
})
node1 = HTMLNode(props={
    "href": "https://www.google.com", 
    "target": "_blank",
})

class main():

    def text_node_to_html_node(text_node):
        leafType
        match text_node.text_type:
            case TextType.TEXT:
                # TextType.TEXT: This should return a LeafNode with no tag, just a raw text value.
                # return LeafNode(None, text.text)
                leafType = None
            case TextType.BOLD: # = "bold"
                leafType = "b"
            case TextType.ITALIC: # = "italic"
                leafType = "i"
            case TextType.CODE: # = "code"
                leafType = "code"
            case TextType.LINK: # = "link"
                leafType = "a"
                return LeafNode(leafType, text.text, "href")
            case TextType.IMAGE: # = "image"
                leafType = "img"
                return LeafNode(leafType, "", "src", "alt")
        return LeafNode(leafType, text.text)
    # print (a.__eq__(b))
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    # print(node.to_html())
    moveDirectory()
    #    print (node2.__repr__() == node1.__repr__())