from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

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
    print(node.to_html())
    #    print (node2.__repr__() == node1.__repr__())