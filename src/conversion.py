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
    # print (outputArray)
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
    # print (outputArray)
    return outputArray

def text_to_textnodes(text):
    outArr = []
    initialNode = TextNode( text, TextType.TEXT )
    # TEXT = "text"
    # BOLD = "bold"
    outArr = split_nodes_delimiter([initialNode], "**", TextType.BOLD)

    # ITALIC = "italic"
    outArr = split_nodes_delimiter(outArr, "_", TextType.ITALIC)
    # CODE = "code"
    outArr = split_nodes_delimiter(outArr, "`", TextType.CODE)
    # IMAGE = "image"
    outArr = split_nodes_image(outArr)
    # LINK = "link"
    outArr = split_nodes_link(outArr)
    return outArr

def stripBlock(text):
    # temporarily remove \n characters, strip(), then restore
    # print ( text)
    newArray = text.split("\n")
    skippedFirst = False
    outString = ""
    for i in range(len(newArray)):
        newText = newArray[i].strip()
        # print (newText)
        if (skippedFirst and len(newText) > 1):
            outString += ("\n"+newText)
        elif (len(newText) > 1):
            outString = newText
            skippedFirst = True
    return outString
def splitBlock(text):
    newArray = text.split("\n\n")
    outArray = []
    for i in range(len(newArray)):
        if ( len(newArray[i]) > 1):
            newText = stripBlock(newArray[i])
            outArray.append(newText)
    return outArray

def markdown_to_blocks(text):

    # blocks = text.split("\n\n")
    blocks = splitBlock(text)
    # blocks = list( map( lambda x: "".join(
    #                 list ( map ( stripBlock, x ))
    #             ), block.split("\n\n") 
    #             ) ) 
    # print (blocks)
    # blocks2 = list( map( stripBlock, blocks ) ) 

    # return (list(filter( lambda data: data != "", blocks )))
    return blocks


