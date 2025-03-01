from enum import Enum

from htmlnode import HTMLNode, LeafNode, ParentNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if (other == None):
            return False
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    # def text_node_to_html_node(self, text_node):
    #     leafType = ""
    #     match text_node.text_type:
    #         case TextType.TEXT:
    #             leafType = None
    #         case TextType.BOLD:
    #             leafType = "b"
    #         case TextType.ITALIC:
    #             leafType = "i"
    #         case TextType.CODE:
    #             leafType = "code"
    #         case TextType.LINK:
    #             leafType = "a"
    #             return LeafNode(leafType, text_node.text, "href")
    #         case TextType.IMAGE:
    #             leafType = "img"
    #             return LeafNode(leafType, "", "src", "alt")
    #     return LeafNode(leafType, text_node.text)
