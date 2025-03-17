from enum import Enum

from htmlnode import HTMLNode, LeafNode, ParentNode

class TextType(Enum):
    BOLD = "bold"
    CODE = "code"
    IMAGE = "image"
    ITALIC = "italic"
    LINK = "link"
    TEXT = "text"


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