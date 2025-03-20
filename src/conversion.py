# from enum import Enum
from enum import Enum
import re

# from htmlnode import HTMLNode, LeafNode, ParentNode
from htmlnode import LeafNode, ParentNode
from textnode import TextType, TextNode

def text_node_to_html_node(text_node):
    if (not isinstance(text_node.text, str) or len(text_node.text.strip()) == 0):
        return None
    # if (text_node.text_type != TextType.CODE and text_node.text_type != TextType. ):
    #     text_node.text = text_node.text.replace("\n", " ")
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
            return LeafNode("a", text_node.text, {"href":text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
        case default:
            raise Exception ("unsupported text type")

# convert list of text to list of text_nodes
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    output = []
    for node in old_nodes:
        output.extend(
            split_node(node, delimiter, text_type)
        )
    return output

def split_node(node, delimiter, text_type):
    if (delimiter not in node.text):
        return [node]
    if (node.text_type == TextType.CODE):
        return [node]
    else:
        typeSwitch = type_options(node.text_type, text_type)
        inArr = node.text.split(delimiter)
        if ( len( inArr ) < 2 ):
            raise Exception ("Not enough delimiters")
        outputArr = [] 
        current_type = node.text_type
        for i in range(len(inArr)): 
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

def split_node_image(node):
    imgTuples = extract_markdown_images(node.text)
    if (len(imgTuples)<1):
        return [node]
    wipText = node.text
    onlyNonLinkText = re.sub(r"\!\[.*?\]\(.*?\)","^temp^", wipText)
    outArr = []
    outArr.extend(
        split_node(TextNode( onlyNonLinkText ,node.text_type ),"^",TextType.IMAGE)
    )
    insertTupleIndex = 0
    for i in range( len(outArr)):
        if ( outArr[i].text_type == TextType.IMAGE ):
            outArr[i].text = imgTuples[insertTupleIndex][0]
            outArr[i].url = imgTuples[insertTupleIndex][1]
            insertTupleIndex += 1
    return outArr

def split_nodes_image(old_nodes):
    outputArray = []
    for node in old_nodes:
        outputArray.extend(split_node_image(node))
    return outputArray

def split_node_link(node):
    linkTuples = extract_markdown_links(node.text)
    if (len(linkTuples)<1):
        return [node]
    wipText = node.text
    onlyNonLinkText = re.sub(r"\[.*?\]\(.*?\)","^temp^", wipText)
    outArr = []
    outArr.extend(
        split_node(TextNode( onlyNonLinkText ,node.text_type ),"^",TextType.LINK)
    )
    insertTupleIndex = 0
    for i in range( len(outArr)):
        if ( outArr[i].text_type == TextType.LINK ):
            outArr[i].text = linkTuples[insertTupleIndex][0]
            outArr[i].url = linkTuples[insertTupleIndex][1]
            insertTupleIndex += 1
    return outArr
def split_nodes_link(old_nodes):
    outputArray = []
    if (not isinstance(old_nodes,list)):
        raise Exception("Not List")
    for node in old_nodes:
        outputArray.extend(split_node_link(node))
    return outputArray

def list_to_textnodes(arr):
    outArr = []
    for text in arr:
        outArr.extend(text_to_textnodes(text))
    return outArr

def text_to_textnodes(text):
    outArr = []
    initialNode = TextNode( text, TextType.TEXT )
    # TEXT = "text"
    # CODE = "code"
    outArr = split_nodes_delimiter([initialNode], "`", TextType.CODE)
    # BOLD = "bold"
    outArr = split_nodes_delimiter(outArr, "**", TextType.BOLD)

    # ITALIC = "italic"
    outArr = split_nodes_delimiter(outArr, "_", TextType.ITALIC)
    # IMAGE = "image"
    outArr = split_nodes_image(outArr)
    # LINK = "link"
    outArr = split_nodes_link(outArr)
    return outArr