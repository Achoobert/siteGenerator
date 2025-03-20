from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from conversion import text_node_to_html_node, split_nodes_delimiter
from generatePage import generate_page
from copyDir import moveDirectory, generateFromDirectory

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

    # print(node.to_html())
    moveDirectory()
    generateFromDirectory()
    # generate_page('./content/index.md', './template.html', './public/index.html')
    #    print (node2.__repr__() == node1.__repr__())