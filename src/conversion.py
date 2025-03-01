# from enum import Enum
from enum import Enum
import re

# from htmlnode import HTMLNode, LeafNode, ParentNode
from htmlnode import LeafNode
from textnode import TextType, TextNode

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, "href")
        case TextType.IMAGE:
            return LeafNode("img", "", "src", "alt")
        case default:
            raise Exception ("unsupported text type")

# convert list of text to list of text_nodes
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    output = []
    for node in old_nodes:
        # print (node.text)
        output.extend(
            split_node(node, delimiter, text_type)
        )
    return output

def split_node(node, delimiter, text_type):
    if (delimiter not in node.text):
        return [node]
    else:
        typeSwitch = type_options(node.text_type, text_type)
        inArr = node.text.split(delimiter)
        if ( len( inArr ) < 2 ):
            raise Exception ("Not enough delimiters")
        outputArr = [] 
        current_type = node.text_type
        for i in range(len(inArr)): 
            # print( len(inArr[i]) )
            if ( len(inArr[i]) == 0):
                current_type = typeSwitch(current_type)
            else:
                outputArr.append(TextNode(inArr[i], current_type))
                current_type = typeSwitch(current_type)
        return outputArr

def type_options (oldType, newType):
    def type_switch(activeType):
        if (activeType == oldType):
            return newType
        elif (activeType == newType):
            return oldType
        raise Exception("activeType is not in expected range")
    return type_switch

def extract_markdown_images(text):
    return re.findall( r"\!\[(.*?)\]\((.*?)\)", text )
def extract_markdown_links(text):
    return re.findall( r"\[(.*?)\]\((.*?)\)", text )

def split_nodes_image(old_nodes):
    # return a list of nodes
    # non-image nodes should be in base node-type
    return []
def split_nodes_link(old_nodes):
    return []

# import re
# text = "I'm a little teapot, short and stout. Here is my handle, here is my spout."
# matches = re.findall(r"teapot", text)
# print(matches) # ['teapot']

# text = "My email is lane@example.com and my friend's email is hunter@example.com"
# matches = re.findall(r"(\w+)@(\w+\.\w+)", text)
# print(matches)  # [('lane', 'example.com'), ('hunter', 'example.com')]