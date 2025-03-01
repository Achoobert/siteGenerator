# from enum import Enum
from enum import Enum

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
# 
# node = TextNode("This is text with a `code block` word", TextType.TEXT)
# new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
# [
#     TextNode("This is text with a ", TextType.TEXT),
#     TextNode("code block", TextType.CODE),
#     TextNode(" word", TextType.TEXT),
# ]

# convert list of text to list of text_nodes
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    output = []
    for node in old_nodes:
        print (node.text)
        output.append(
            split_node(node, delimiter, text_type)
        )
    return output

def split_node(node, delimiter, text_type):
    if (delimiter not in node.text):
        return node
    # TODO count number of instances of delimiter in text. Should be "even"
    # if not, should raise error
    # delimitArr = node.text.split(delimiter)
    # if ( len(delimitArr) / 2 % 1):
    #     # 
    else:
        textArr = node.text.split()
        print(textArr)
        outputArr = [] # final list of nodes
        currentNode = None
        for word in textArr: 
            if (delimiter in word): # Either beginning or end of delimited, we need to take action
                #  how to handle single word and multi word
                # TODO remove delimit from word output
                if ( len( word.split(delimiter) ) > 2 ):
                    raise Exception("Too much")
                if (currentNode != None and currentNode.text_type != None and currentNode.text_type == text_type):
                    # close current node
                    currentNode.text = " ".join([currentNode.text, word])
                    outputArr.append(currentNode.copy())
                    currentNode = None
                else:
                    # open new node
                    if (currentNode != None):
                        outputArr.append(currentNode.copy())
                    currentNode = TextNode("".join(word), text_type)
            else:
                if (currentNode == None):
                    currentNode = TextNode("".join(word), None)
                else:
                    currentNode.text = " ".join([currentNode.text, word])
        # Is there a dangling currentNode?
        if (currentNode != None):
            outputArr.append(currentNode)
        return outputArr

# def find_text_delimiter(text, delimiter):
#     splitTextArray = text.split(delimiter)
#     if ( len(splitTextArray) > 2 ):
#         # Word is whole node
#     elif ( len(splitTextArray) == 2 ):
#         if (splitTextArray[0] == "")
#         # start of section
#         elif (splitTextArray[1] == "")
#         # end of section
#         else: 
#             raise Exception("Where is my delimiter?")
#     else 
